from typing import Union
from facebook_scraper import get_profile
from fastapi import FastAPI
import pymongo
from pymongo import MongoClient
client= MongoClient('mongodb+srv://2151998:2151998@cluster0.46axtas.mongodb.net/?retryWrites=true&w=majority')
db = client.scraped
col = db.fb


app = FastAPI()


@app.post("/")
def read_root():
    doc = get_profile("natgeo")
    col.insert_one(dict(doc))
    return doc