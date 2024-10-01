import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('Punkt')
nltk.download('stopwords')
text='natural language is python in the cureent world today'
tokens=word_tokenize(text)
stop_words=set(stopwords.words('english'))
filtered_tokens=[word for word in tokens if word.lower() not in stop_words]
stemmer=PorterStemmer()
stemmed_tokens=[stemmer.stem(word) for word in filtered_tokens]
print("original text\n",text)
print("tokenized text\n",tokens)
print("after stop word removal\n",filtered_tokens)
print("after stemming\n",stemmed_tokens)