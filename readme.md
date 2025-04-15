## Clone Repo
```bash
git clone https://github.com/96ibman/FastAPI_sentiment_analysis.git

cd FastAPI_sentiment_analysis
```

## Create Virtual Env
```bash
python -m venv venv
venv/Scripts/activate
```

## Install Requirements
```bash
pip install -r requirements.txt
```

## Run Server
```bash
python app.py
```

## Test API
You can send a POST request using Postman or curl:
```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"I love this movie!\"}"
```
Or Python
```python
import requests
res = requests.post("http://127.0.0.1:8000/analyze", json={"text": "FastAPI is awesome!"})
print(res.json())
```
Sample Result:
```json
{
  "input": "your text",
  "analysis": {
    "label": "POSITIVE",
    "score": 0.7402095794677734
  }
}
```