import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.filters import Search_filters

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


search = Search_filters()

@app.get("/autocomplete")
async def autocomplete(query: str = ""):
    result = search.autocomplete(query=query)
    return result

@app.post("/string-query-search")
async def string_query_seach(query: str = ""):
    result = search.string_query_search(query=query)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

