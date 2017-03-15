import cPickle as pickle

filename = 'test1.txt'
X = open(filename).readlines()
filename2 = 'nlp_dupquestions.p'
newFile = open(filename2 , 'w')

pickle.dump(X, newFile)

newFile.close()
