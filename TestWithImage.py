
from ultralytics import YOLO
import os, shutil
from PIL import Image
shutil.rmtree("output")
model=YOLO("best1.pt")
model.predict(mode="predict", model="bes1.pt",project='output', save=True, show=True,conf=0.1, source=0)

#im = Image.open(r"output/predict/skin (1).jpg")

im.show()