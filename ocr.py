"""https://github.com/tesseract-ocr/tesseract/wiki/Data-Files for reference"""
from PIL import Image
import pytesseract as pt
x=-1
while x!=0:
    print("\nEnter:")
    print("1. for English")
    print("2. for Marathi")
    print("3. for Hindi")
    print("4. for Sanskrit")
    print("5. for Gujarati")
    print("0. to exit\n")
    text = input ("Input: ")
    x = int(text)
    if x==0:
        print("\nThank You")
    elif x<0 or x>5:
        print("\nWrong input!!!")
    else:
        if x==1:
            language='eng'#English
        elif x==2:
            language='mar'#Marathi
        elif x==3:
            language='hin'#Hindi
        elif x==4:
            language='san'#Sanskrit
        elif x==5:
            language='guj'#Gujarati
        j=0
        i=input("Enter image: ")
        img = Image.open(i)
        while j<=0 or j>5:
            print("\nEnter:")
            print("1. for script output in terminal (Warning: proper font required)")
            print("2. for script output to file")
            print("3. for OSD (result containing information about orientation and script detection)")
            text = input ("Input: ")
            j = int(text)
            if j<=0 or j>4:
                print("\nWrong input!!!")
            else:
                if j==1:
                    print(pt.image_to_string(img, lang=language))
                elif j==2:
                    text = input ("Enter output file: ")
                    f= open(text,"w+",encoding='utf-8')
                    f.write(pt.image_to_string(img, lang=language))
                    f.close()
                    print("Script output to file "+text+" sucessful")
                elif j==3:
                    print(pt.image_to_osd(img))#script info