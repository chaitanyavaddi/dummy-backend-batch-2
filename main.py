from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home(word):
    endpoint = f"https://api.datamuse.com/words?sp={word}"
    response = requests.get(endpoint)

    data = response.json()
    return data