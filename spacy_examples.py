#!pip install spacy
#!python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence. This is another sentence.")
for sent in doc.sents:
    print(sent.text)
type(sent.text)