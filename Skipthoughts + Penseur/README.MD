The **SkipThoughts** model is an unsupervised learning model used for generic, distributed sentence encodings. The **SkipThoughts** model also features vocabulary expansion which allows for a way to encode words not found in the training data into the vector space, making it very extensible.

The main features of the **SkipThoughts** model are:

- Vocabulary expansion used to induce word representations not found in training data
- Encoder/decoder model where encoder maps the input sentence to a sentence vector
- The decoder generates the sentences surrounding the original sentence
- Surrounding sentences used to learn sentence vectors
- Encoder has a bidirectional, unidirectional and combine-skip models (combination of former 2 models)

Steps needed to train the model:

1. Create dictionary from training data
2. Set hyperparameters for training the encoder. Most common parameters used were 300 word dimensionality, 1-2 epochs and 1200 GRU units with a batch size of 64
3. Launch the training. All 3 steps to this point can be accessed from the **training** folder. 
4. Create word2vec model. The script to create the model can be found in the **word2vec** folder.
5. Put the trained encoding model, dictionary and word2vec files in a folder called **data**.
6. Change the relevant file locations in the **tools.py** file in the **training** folder.
7. Place the testing data (in a .pickle format) in the **data** folder.
8. Load the model using Penseur and it will automatically encode the sentences into vectors.



