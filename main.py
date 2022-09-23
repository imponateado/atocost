from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path


files = os.listdir()

for i in files:
    pages = convert_from_path(i, 500)
    for j in pages:
        output = pytesseract.image_to_string(j)
        print(output)
        print("---------------------------------------")
        n = output.find("Tot. ped.")   
        renomear = output[n+9:n+14]
        os.rename(i, renomear+".pdf")
