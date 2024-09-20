from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "OK"}

@app.post("/chat")
async def chat(prompt: str):
    return {"response": f"You said: {prompt}"}

