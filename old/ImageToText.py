
import pytesseract
from PIL import Image


img = Image.open('Screenshot (19).png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)
print(result)
with open('textfromimage.txt', mode ='w') as file:
 file.write(result)

