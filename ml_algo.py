

def tokensforyou(tokenizer,train_data):
    for item in train_data:

        string_option = str(item)
        # fit the tokenizer on the document
        tokenizer.fit_on_texts(text)
        # print the attributes for the text and encode the doucment
        #print(tokenizer.word_counts)
        #print(tokenizer.word_docs)
        #print(tokenizer.word_index)
        #print(tokenizer.document_count)
        encoded_text = tokenizer.texts_to_matrix(text)
        #print(encoded_text)
    return tokenizer

# Load CSV (using python)
import csv
import numpy
import pandas as pd
from keras.preprocessing.text import text_to_word_sequence
filename = '/Users/grahamwaters/Documents/GitHub Main Repository/KAGGLE_COMPETITIONS/DISASTERS/test.csv'
#reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
df_test = pd.read_csv(filename)
df_test
filename = '/Users/grahamwaters/Documents/GitHub Main Repository/KAGGLE_COMPETITIONS/DISASTERS/train.csv'
#reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
df_train = pd.read_csv(filename)

train_data = pd.array(df_train['text'])
test_data = pd.array(df_test['text'])
#print(train_data)
from keras.preprocessing.text import Tokenizer
# creating tokenizer
tokenizer = Tokenizer()
tokenizer = tokensforyou(tokenizer,train_data)



# define the text 
text = train_data
# tokenizing the text 
tokens = text_to_word_sequence(text)
print("finished")
