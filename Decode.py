import numpy as np
import random
import pickle
from tensorflow.keras.models import Sequential,load_model
import preprocess
#pickle_in=open("data.pickle","rb")
#data=pickle.load(pickle_in)



def decode(data):
    #print(data[0][0])
    comments = []
    for i,_ in enumerate(data):
        comment = []
        for j,_ in enumerate(data[i]):

            #print(data[i][j])
            #print("\n")
            k=0

            for k,_ in enumerate(data[i][j]):
                #print(data[i][j][k])
                #print("\n")
                #pass
                if(data[i][j][k]==1):
                    break
            #if(k==26)
            #print(chr(k+97)+"   "+str(k))
            if(k==26):
                comment.append(' ')
            elif(k==27):
                comment.append('.')
            elif(k==28):
                comment.append('\n')
            elif(k==29):
                comment.append('\0')
            else:
                comment.append(chr(k+97))
            #print(k)
        comments.append(''.join(comment))
        #print(''.join(comment))
    #print(comments[0])
            #else:
                #pass
            #pass
    return comments

def rouletteWheel(output):
    rand = random.random()
    bottom = 0.0
    top = 0.0
    for i, _ in enumerate(output[0]):
        top += output[0][i]
        if(rand <= top):
            return i


def generateText(beforeText=False):
    model = "textGen23"

    seqLen = 5
    model = load_model('models/'+model+'.model')#best 10, 12, 18, 20

    model.summary()

    limit = 1000

    numberComment = 10
    stop = True
    #import preprocess
    textBegining=""
    #print(decode(input)[0])
    if(beforeText):
        text = input("input text: ")
        textBegining = text[:-seqLen]
        text = text[-seqLen:]

        newText = preprocess.ProcessText(text,seqLen)
    for j in range(0,numberComment):
        inputs = np.zeros((1,seqLen , 30))
        if(not beforeText):
            inputs[0][seqLen-1][random.randint(0, seqLen)] = 1
        else:


            #newText = np.array(newText)
           # print("shape "+str(newText[0].shape))
            #print("data "+str(newText[0][newText.shape[0]]))
            #for k in range(0, len(text)):

            inputs[0] = newText[0][newText[0].shape[0]-1]
        #input[0][seqLen - 3][3] = 1
        #input[0][seqLen - 2][0] = 1
        #input[0][seqLen - 1][13] = 1

        #input[0][seqLen - 4][4] = 1
        #input[0][seqLen - 3][12] = 1
        #input[0][seqLen - 2][12] = 1
        #input[0][seqLen - 1][0] = 1
        #input[0][seqLen - 1][25] = 1
        count=0
        para = decode(inputs)[0]
        while((inputs[0][seqLen-1][29] != 1 or not stop) and limit > count):
            decode(inputs)
            out = model.predict(inputs)

            #print(out[0])
            for i in range(0,seqLen-1):
                inputs[0][i]=inputs[0][i+1]
            #input[0][23]=input[0][24]
            inputs[0][seqLen-1] = np.zeros(30)
            #input[0][seqLen-1][np.argmax(out)]=1
            inputs[0][seqLen-1][rouletteWheel(out)] = 1
            #print(input[0][24])
           #decode(input)
            string = decode(inputs)[0]
            #print(string)
            para+=(string[len(string)-1])
            #print()
            #count+=1
            count+=1
        print("generated text "+str(j) + ":\n"+textBegining+para + "\n")

if __name__ == "__main__":
    choice = input("Complete text y/n: ")
    choice = choice.lower()
    if(choice == "y"):
        generateText(True)
    else:
        generateText(False)