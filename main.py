from fastapi import FastAPI, File, UploadFile
from crud import *


app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    result = insertData(file)
    return {"result": result}