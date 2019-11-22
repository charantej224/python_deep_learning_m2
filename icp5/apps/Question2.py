from keras.models import load_model
from keras_preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

model = load_model('lstm.h5')


def predict(input_sentence):
    # sentence = "A lot of good things are happening. We are respected again throughout the world, and that's a great thing"
    max_fatures = 2000
    tokenizer = Tokenizer(num_words=max_fatures, split=' ')
    tokenizer.fit_on_texts(input_sentence)
    X = tokenizer.texts_to_sequences(input_sentence)
    X = pad_sequences(X, maxlen=28)
    sentiment = model.predict(X, batch_size=1, verbose=2)[0]
    print(sentiment)


while True:
    str_input = input("Enter text for sentiment analysis")
    if str_input.lower() != "exit":
        predict(str_input)
    else:
        break
