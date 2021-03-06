# import modules & set up logging
import gensim, logging, os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


sentences = gensim.models.word2vec.LineSentence('path of file to train')

model = gensim.models.Word2Vec(sentences, size=300)

model.save_word2vec_format('stackmodel', binary=True)


