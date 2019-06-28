
from tensorflow.keras.models import Sequential,load_model
import pickle


name = "picText"
pickle_in = open("data/"+name+".pickle", "rb")
data = pickle.load(pickle_in)


modelName = "textGen12"
model = load_model('models/'+modelName+'.model')

modelNameSave = "textGen23"
model.fit((data[0]), (data[1]), epochs = 1, batch_size = 32)
model.save("models/"+modelNameSave+".model")