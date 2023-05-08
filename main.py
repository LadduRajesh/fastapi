import uvicorn
import numpy as np
#import joblib
from fastapi import FastAPI


app = FastAPI()



@app.get("/")
def index():
    return {"message" : "Hello world"}

@app.get("/{name}")
def get_name(name :str):
    return {f'{name}'}

#@app.post("/predict")

#if __name__ == "__main__":
    #uvicorn.run(app)