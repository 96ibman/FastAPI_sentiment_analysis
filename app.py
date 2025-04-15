from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple FastAPI app that uses Hugging Face Transformers for sentiment analysis.",
    version="1.0.0"
)

sentiment_pipeline = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

@app.post("/analyze")
def analyze_sentiment(input_data: TextInput):
    text = input_data.text
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")

    result = sentiment_pipeline(text)
    return {"input": text, "analysis": result[0]}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)