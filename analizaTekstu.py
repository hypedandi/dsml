!pip install nltk

!pip install spacy
!python -m spacy download en

paragraph="""Taj Mahal is one of the beautiful monuments. It is one of the
wonders of the world. It was built by Shah Jahan in 1631 in memory of his
third beloved wife Mumtaj Mahal."""

print(paragraph.lower())

import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import sent_tokenize

tokenized_sentences=sent_tokenize(paragraph)
print(tokenized_sentences)
