"""https://github.com/tesseract-ocr/tesseract/wiki/Data-Files for reference"""
import PIL as ig
import pytesseract as pt
from tkinter import *
import pyperclip

def return_value(i,language):
        img = ig.Image.open(i)
        s= pt.image_to_string(img, lang=language)
        tex.config(state=NORMAL)
        tex.insert(INSERT,s)
        tex.see(END)
        tex.config(state=DISABLED)
        copy = Button(window, text="Copy Output", font=(font, font_size), command=pyperclip.copy(s)).pack()
        
def submit():
        lg=str(langtk.get())
        if lg=='English':
                l='eng'#English
        elif lg=='Marathi':
                l='mar'#Marathi
        elif lg=='Hindi':
                l='hin'#Hindi
        elif lg=='Sanskrit':
                l='san'#Sanskrit
        elif lg=='Gujarati':
                l='guj'#Gujarati'
        if l=='':
                pass
        return_value(str(imgtk.get()),l)
        
window = Tk()
window.geometry('800x800+500+300')
window.title("OCR")
window.iconbitmap('favicon.ico')
font = "Product Sans"
font_size = 15
imgtk=StringVar()
langtk = StringVar()
language_choices = { 'English','Hindi','Marathi','Sanskrit','Gujarati'}
langtk.set('Select Language') 
title = Label(window, text="OCR", font=(font,20)).pack()
lab = Label(window, text="Image file location", font=(font, font_size)).pack()
inp = Entry(window, font=(font, font_size),textvariable=imgtk).pack()
pop = OptionMenu(window, langtk, *language_choices)
pop.config(font=(font, font_size))
pop.pack()
sub = Button(window, text="Submit", font=(font, font_size), command=submit).pack()
tex=Text(window)
tex.pack(side=TOP, fill=X)
tex.insert(INSERT, "Output:\n")
tex.config(state=DISABLED,font=(font, 10))
window.mainloop()
