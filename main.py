from fastapi import FastAPI, UploadFile, File
from PIL import Image
from pix2tex.cli import LatexOCR
from io import BytesIO

app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint for making predictions based on an uploaded image file.
    
    :param file: The uploaded image file.
    :type file: UploadFile
    
    :return: A dictionary containing the predicted LaTeX string.
    :rtype: dict
    """
    model = LatexOCR()
    image_data = await file.read()
    img = Image.open(BytesIO(image_data))
    result = model(img)
    return {"latex": result}