import nltk
from nltk.corpus import words
nltk.download('words')
english=set(words.words())
def spell_check(test):
    words_to_check=nltk.word_tokenize(test)
    misspelled_words=[word for word in words_to_check if word.lower() not in english]
    return misspelled_words
input_text=input("enter a sequence for spell checking:")
misspelled_words=spell_check(input_text)
if len(misspelled_words)>0:
    print("\n misspeled words:")
    for word in misspelled_words:
        print(word)
else:
    print("no mispelled words")