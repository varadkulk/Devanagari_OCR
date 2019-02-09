from PIL import Image
import pytesseract

img=Image.open("x.png")

text=pytesseract.image_to_string(img,lang='0')

print(text)
