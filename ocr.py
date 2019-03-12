from PIL import Image
import pytesseract

img=Image.open("b.jpg")

text=pytesseract.image_to_string(img,lang='eng')

print(text)
