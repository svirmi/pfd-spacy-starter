from fastapi import FastAPI
import spacy
from typing import List
from pydantic import BaseModel


class Content(BaseModel):
    post_url: str
    content: str


class Payload(BaseModel):
    data: List[Content]


app = FastAPI()
nlp = spacy.load("en_core_web_sm")


@app.post('/ner-service')
async def get_ner(payload: Payload):
    tokenize_content: List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    document_entities = []
    for doc in tokenize_content:
        x = [{'text': ent.text, 'entity_type': ent.label_} for ent in doc.ents]
        print(x)
        document_entities.append(x)
    return document_entities
