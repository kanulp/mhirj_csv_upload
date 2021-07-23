from fastapi import FastAPI, File, UploadFile
from navneet import *
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = insertData(contents)
    return {"file_contents": json_string}