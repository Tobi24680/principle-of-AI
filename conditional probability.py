import re
import numpy as np
data=[
    ("this is spam email",'spam'),
    ("buy one get one free",'spam'),
    ("hlo how are you",'ham'),
    ("congratulation you have won prize",'spam'),
    ("meeting at 3 pm",'ham'),
    ("get discount on your next purchase",'spam'),
]

word_set=set()
for text,label in data:
    words=re.findall(r'\W+',text.lower())
    
word_set.update(words)
word_list=list(word_set)
word_list.sort()

vocab={word:index for index,word in enumerate(word_list)}

spam_count=0
ham_count=0

spam_word_count=np.zeros(len(vocab))
ham_word_count=np.zeros(len(vocab))

for text,label in data:
    words=re.findall('\W+',text.lower())
    
    if label=='spam':
        spam_count+=1
        label_count=spam_word_count
    else:
        ham_count+=1
        label_count=ham_word_count
        
    for word in words:
            if word in vocab:
                word_index=vocab[word]
                label_count[word_index]+=1
total_messages=len(data)
prior_spam=spam_count/total_messages
prior_ham=ham_count/total_messages

input_text="you've won a free vacation!"
input_words=re.findall(r'W+',input_text.lower())

likelihood_spam=1.0
likelihood_ham=1.0
 
for word in input_words:
    if word in vocab:
        word_index=vocab[word]
        likelihood_spam*=(spam_word_count[word_index]+1)/(spam_count+len(vocab))
        likelihood_ham*=(ham_word_count[word_index]+1)/(ham_count+len(vocab))
posterior_spam = (likelihood_spam * prior_spam) / ((likelihood_spam * prior_spam) + (likelihood_ham * prior_ham))
posterior_ham = 1 - posterior_spam                                             
if posterior_spam >posterior_ham:
    print("classified as: spam")
else:
    print("classified as:ham")

