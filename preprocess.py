import numpy as np
import pickle
import re
import random

name = "KerbalSpaceProgramTop"
def ProcessFile(name,seqLen):

    pickle_in = open("text/" + name + ".txt", "rb")
    data = pickle.load(pickle_in)
    return ProcessData(data,seqLen)

def ProcessText(text,seqLen):
    data = []
    data.append(text)

    return ProcessData(data,seqLen,False)


def ProcessData(data,seqLen,save=True):
    for i, _ in enumerate(data):
        data[i] = data[i].lower()
        # data[i] = re.sub("[^a-z0-9\s\.?!']+","", str(data[i]))
        data[i] = re.sub("[^a-z\s\.]+", "", str(data[i]))


    for i, _ in enumerate(data):
        data[i] = list(data[i])
        data[i].append('\0')
        for j, _ in enumerate(data[i]):
            # print(ord(data[i][j]))

            # a = np.zeros(28)#.reshape(1,28)
            a = np.zeros((30, 1))
            if (ord(data[i][j]) >= 97 and ord(data[i][j]) <= 122):
                # print(data[i][j])
                a[ord(data[i][j]) - 97] = 1
            if (data[i][j] == ' '):
                a[26] = 1
            elif (data[i][j] == '.'):
                a[27] = 1
            elif (data[i][j] == '\n'):
                a[28] = 1
            elif (data[i][j] == '\0'):
                a[29] = 1
            data[i][j] = a

    random.shuffle(data)


    dataX = np.array([])
    dataY = np.array([])
    dataX = []
    dataY = []
    # data=data[0:5]
    # data=data[0]
    i = 0
    j = 0
    for i, _ in enumerate(data):
        # print(str(i)+"i")
        seqStartIndex = 0
        for j in range(0, len(data[i]) - 1):
            # print(j)
            if (((j + 1) - seqStartIndex) > seqLen):
                seqStartIndex += 1
                # for k in range(0,(25-(j+1)-seqStartIndex )):
                # data[i][seqStartIndex:(j + 1)] = np.append(data[i][seqStartIndex:(j + 1)], np.zeros( (1, 30) ))
                # print(data[i][seqStartIndex:(j + 1)].shape)
                # print(25-k)

            dataX.append(data[i][seqStartIndex:(j + 1)])
            # dataX=np.append(dataX,np.array(data[i][seqStartIndex:(j+1)]))
            # print(data[i][0])
            dataY.append(data[i][(j + 1)])
            # print(np.array(data[i][(j+1)]))
            # print(np.array(data[i][(j+1)]).shape)
            # dataY=np.append(dataY,np.array(data[i][(j+1)]))

    for i, _ in enumerate(dataX):
        for k in range(0, seqLen - len(dataX[i])):
            # dataX[i] = np.insert(dataX[i],0,np.zeros((1,30)))
            dataX[i].insert(0, np.zeros(((1, 30))))
        for j, _ in enumerate(dataX[i]):
            dataX[i][j] = dataX[i][j].reshape(1, 30)
    #print(dataX[0][0].shape)

   # print()
    dataX = np.array(dataX)
    dataX = dataX.reshape(int(len(dataY)), seqLen, 30)
    dataY = np.array(dataY)
    dataY = dataY.reshape(int(len(dataY)), 30)

    # dataX=dataX.reshape(int(dataY.shape[0]),25,30)
    # print(len(dataX))


    #print(dataX[0])
    #print(dataX.shape)
    #print(dataY.shape)
   # print(len(dataY))
    newData = []
    newData.append(dataX)
    newData.append(dataY)
    if(save):

        pickle_out = open("data/"+name+".pickle", "wb")
        pickle.dump(newData, pickle_out)
    else:
        pass
    return newData

if __name__ == "__main__":
    ProcessFile(name,10)
    #print(ProcessText("The cat sat on the %$%*&"),False)
