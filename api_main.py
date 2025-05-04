# api_main.py

from fastapi import FastAPI
from pydantic import BaseModel
from recommendation_engine import recommend_assessments
import pandas as pd

app = FastAPI()

# Load product catalog once
catalog_df = pd.read_csv("shl_product_catalogue.csv")

class InputData(BaseModel):
    query: str

@app.post("/recommend")
def recommend(data: InputData):
    recommendations = recommend_assessments(data.query, catalog_df)
    return recommendations.to_dict(orient="records")
