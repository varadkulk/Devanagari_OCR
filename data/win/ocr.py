"""https://github.com/tesseract-ocr/tesseract/wiki/Data-Files for Train data"""

import PIL as ig
import pytesseract as pt
from tkinter import filedialog
from tkinter import *
import pyperclip

global n

def tex_remove_add(txt):
        tex.config(state=NORMAL)
        tex.delete('1.0', END)
        tex.insert(INSERT,"Output :\n")
        tex.insert(INSERT,txt)
        tex.see(END)
        tex.config(state=DISABLED)

def return_value(i,language):

        s=''
        global n

        try:
                img = ig.Image.open(i)
                s= pt.image_to_string(img, lang=language)
        except:
                tex_remove_add("Invalid Image")
                return

        tex_remove_add(s)

        if n==0:
                n=1
                copy = Button(window, text="Copy Text", font=(font, font_size), command=pyperclip.copy(s)).pack()

def submit():
 
        if str(langtk.get())=='Select Language':
                 tex_remove_add("Please select the language\n")
 
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

def browse_button():
        filename = filedialog.askopenfilename()

        if filename!='':
                inp.delete('0', END)

        inp.insert(INSERT,filename)

window = Tk()#Start window
window.geometry('1200x630')#Assign its size
window.title("OCR")#Title

try:
        window.iconbitmap('data\\ocr.ico')
except:
        try:
                window.iconbitmap('ocr.ico')
        except:
                pass

n=0

font = "Open Sans"
font_size = 9

imgtk = StringVar()
langtk = StringVar()

title = Label(window, text="OCR", font=(font,20)).pack()

lab = Label(window, text="Image file location", font=(font, font_size)).pack()

inp = Entry(window, width=100,font=(font, font_size),textvariable=imgtk)
inp.config(state=NORMAL)
inp.pack()

browse = Button(text="Browse", font=(font, font_size), command=browse_button).pack()

language_choices = { 'English','Hindi','Marathi','Sanskrit','Gujarati'}
langtk.set('Select Language') 
pop = OptionMenu(window, langtk, *language_choices)
pop.config(font=(font, font_size))
pop.pack()

sub = Button(window, text="Submit", font=(font, font_size), command=submit).pack()

tex=Text(window)
tex.pack(side=TOP, fill=X)
tex.insert(INSERT, "Output:\n")
tex.config(state=DISABLED,font=(font, font_size))

window.mainloop()