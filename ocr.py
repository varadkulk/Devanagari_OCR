from PIL import Image
import pytesseract

img=Image.open("b.jpg")

text=pytesseract.image_to_string(img,lang='eng')

print(text)

https://askubuntu.com/questions/793634/how-do-i-install-a-new-language-pack-for-tesseract-on-16-04
