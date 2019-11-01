from keras.layers import Flatten
from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding

from sklearn.datasets import fetch_20newsgroups

newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True, categories=['alt.atheism',
                                                                                'comp.graphics',
                                                                                'comp.os.ms-windows.misc',
                                                                                'comp.sys.ibm.pc.hardware',
                                                                                'comp.sys.mac.hardware',
                                                                                'comp.windows.x',
                                                                                'misc.forsale',
                                                                                'rec.autos',
                                                                                'rec.motorcycles',
                                                                                'rec.sport.baseball',
                                                                                'rec.sport.hockey',
                                                                                'sci.crypt',
                                                                                'sci.electronics',
                                                                                'sci.med',
                                                                                'sci.space',
                                                                                'soc.religion.christian',
                                                                                'talk.politics.guns',
                                                                                'talk.politics.mideast',
                                                                                'talk.politics.misc',
                                                                                'talk.religion.misc'])
# newsgroups_test =fetch_20newsgroups(subset='test', shuffle=True, categories=['sci.space'])

sentences = newsgroups_train.data
y = newsgroups_train.target

# tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
max_review_len = max([len(s.split()) for s in sentences])
vocab_size = len(tokenizer.word_index) + 1
sentences = tokenizer.texts_to_sequences(sentences)
padded_docs = pad_sequences(sentences, maxlen=max_review_len)

le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(padded_docs, y, test_size=0.25, random_state=1000)

print(len(X_train))
# Number of features
# print(input_dim)
model = Sequential()

model.add(Embedding(vocab_size, 50, input_length=max_review_len))
model.add(Flatten())
model.add(layers.Dense(20, activation='sigmoid'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=50, verbose=True, validation_data=(X_test, y_test), batch_size=256)
