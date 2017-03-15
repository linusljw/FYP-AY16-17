**This folder contains the Siamese-CBOW model used to train word embeddings for sentence representations. **

The Siamese Continuous Bag of Words or (C-BOW) model
- Is a neural network based on the Theano framework 
- Is used for efficient estimation of high-quality sentence embeddings.
- It is mainly used to calculate word embeddings optimized across sentences to produce a sentence representation 
- The Siamese C-BOW model is tailored specifically for the task of averaging sentence vectors. This is achieved by directly including the comparisons of sentence embeddings in the cost function of the architecture. 

The format of the input data used for the model was the **Toronto Bookcorpus** format under the **torontobookcorpusutils folder**. The methods/functions used to preprocess the training data can all be found in the **torontobookcorpusutils** folder. 

The **siamese-cbow.py** python file is used to train the model and the **wordEmbeddings** python file is used to retrieve the word embeddings from said model. Modifications have been made to the **wordEmbeddings** file. 

**The hyperparameters used to train the model were a batch size of 100, embedding size of 300 and 1 epoch with shared weights. **
