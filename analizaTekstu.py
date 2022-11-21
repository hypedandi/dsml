!pip install nltk

# tekst do analizy

paragraph="""Taj Mahal is one of the beautiful monuments. It is one of the
wonders of the world. It was built by Shah Jahan in 1631 in memory of his
third beloved wife Mumtaj Mahal."""

# zmiana liter na małe w całym akapicie

print(paragraph.lower())

# Tokenizacja

import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# tokenizacja za pomocą metody sent_tokenize

from nltk.tokenize import sent_tokenize

tokenized_sentences = sent_tokenize(paragraph)
print(tokenized_sentences)

# STOPWORDS usuwanie słów nieinformatywnych przy pomocy NLTK

from nltk.corpus import stopwords
stopwords_set=set(stopwords.words("english"))

filtered_word_list=[]


for word in tokenized_words:
    if word not in stopwords_set:
       filtered_word_list.append(word)
       
print("Lista tokenizowanych słów:", tokenized_words)
print("Lista przefiltrowanych słów:", filtered_word_list)

# PoS tagging

from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = "Taj Mahal is one of the beautiful monument."
sent_tokens = word_tokenize(sentence)
sent_pos = pos_tag(sent_tokens)
print(sent_pos)




