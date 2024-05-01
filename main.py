from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return "Hello, the retriever is working"


@app.post("/qa")
async def section(request: Request):

    data = await request.json()

    from book_metadata_retriever import answer
    answer = answer(data["Question"])

    return {"Answer": answer}



