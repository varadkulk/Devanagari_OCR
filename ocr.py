"""https://github.com/tesseract-ocr/tesseract/wiki/Data-Files for reference"""
import PIL as ig
import pytesseract as pt
from tkinter import *
import pyperclip

def return_value(i,language):
        s=''
        try:
                img = ig.Image.open(i)
                s= pt.image_to_string(img, lang=language)
        except:
                tex.config(state=NORMAL)
                tex.insert(INSERT,"Invalid Image\n")
                tex.see(END)
                tex.config(state=DISABLED)
                return
        tex.config(state=NORMAL)
        tex.insert(INSERT,s)
        tex.see(END)
        tex.config(state=DISABLED)
        copy = Button(window, text="Copy Text", font=(font, font_size), command=pyperclip.copy(s)).pack()
        
def submit():
        if str(langtk.get())=='Select Language':
                tex.config(state=NORMAL)
                tex.insert(INSERT,"ERROR\n")
                tex.see(END)
                tex.config(state=DISABLED)
        else:
                if str(langtk.get())=='English':
                        l='eng'#English
                elif str(langtk.get())=='Marathi':
                        l='mar'#Marathi
                elif str(langtk.get())=='Hindi':
                        l='hin'#Hindi
                elif str(langtk.get())=='Sanskrit':
                        l='san'#Sanskrit
                elif str(langtk.get())=='Gujarati':
                        l='guj'#Gujarati'
                return_value(str(imgtk.get()),l)
        
window = Tk()#Start window
window.geometry('1300x650')#Assign its size
window.title("OCR")#Title
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