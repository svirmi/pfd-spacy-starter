import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion bitcoins")

for token in doc:
    print(token.text, token.pos_, token.dep_, token.ent_type_)