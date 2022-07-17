from fastapi import FastAPI
import spacy
from typing import List
from pydantic import BaseModel


class Content(BaseModel):
    post_url: str
    content: str


class Payload(BaseModel):
    data: List[Content]


class SingleEntity(BaseModel):
    text: str
    entity_type: str


class Entities(BaseModel):
    post_url: str
    entities: List[SingleEntity]


app = FastAPI()
nlp = spacy.load("en_core_web_sm")


@app.post('/ner-service')
async def get_ner(payload: Payload):
    tokenize_content: List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    document_entities = []
    for doc in tokenize_content:
        document_entities.append([{'text': ent.text, 'entity_type': ent.label_} for ent in doc.ents])
    return document_entities
