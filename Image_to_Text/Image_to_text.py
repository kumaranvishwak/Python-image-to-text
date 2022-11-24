
import pytesseract 
from PIL import Image

image_location = input("Enter:")
img = Image.open(image_location)
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
data = pytesseract.image_to_string(img)
print(data)

