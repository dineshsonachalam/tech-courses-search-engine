#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.filters import SearchFilters
from utils.elasticsearch import Elasticsearch

app = FastAPI()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


search = SearchFilters(index="cs.stanford")
es = Elasticsearch(index="cs.stanford")

@app.get("/autocomplete")
async def autocomplete(query: str = ""):
    if(es.pre_condition_check()):
        result = search.autocomplete(query=query)
        return result
    else:
        return []

@app.post("/string-query-search")
async def string_query_seach(query: str = ""):
    if(es.pre_condition_check()):
        result = search.string_query_search(query=query)
        return result
    else:
        return []


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

