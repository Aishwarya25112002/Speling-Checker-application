# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:40:24 2024

@author: hp
"""

from textblob import TextBlob
from tkinter import Tk, Label, Entry, Button

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, "end")
    enter2.insert(0, data)
    
def main_window():
    global enter1, enter2
    win = Tk()  
    win.geometry("600x370")  # Increased width to accommodate larger text
    win.resizable(False, False)  
    win.config(bg="blue")
    win.title("Wscube Tech")
    
    label1 = Label(win, text="Incorrect Spelling", font=("Times New Roman", 25, "bold"), bg="blue", fg="white")
    label1.place(x=100, y=20, height=50, width=400)  # Increased width
    
    enter1 = Entry(win, font=("Times New Roman", 20))
    enter1.place(x=50, y=80, height=50, width=500)  # Increased width
    
    label2 = Label(win, text="Correct Spelling", font=("Times New Roman", 25, "bold"), bg="blue", fg="white")
    label2.place(x=100, y=140, height=50, width=400)  # Increased width
    
    enter2 = Entry(win, font=("Times New Roman", 20))
    enter2.place(x=50, y=200, height=50, width=500)  # Increased width
    
    button = Button(win, text="Done", font=("Times New Roman", 25, "bold"), bg="yellow", command=correct_spelling)
    button.place(x=200, y=280, height=50, width=200)

    win.mainloop()

if __name__ == "__main__":  
    main_window()
