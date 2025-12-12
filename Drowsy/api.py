# api.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from main import classify_state

app = FastAPI()

@app.get("/detect")
def detect(yawn_score: float = 0.1, eye_score: float = 0.1):
    """
    Contoh endpoint sederhana.
    K6 akan mengakses endpoint ini.
    """
    result = classify_state({"yawn_score": yawn_score, "eye_score": eye_score})
    return {"state": result}
