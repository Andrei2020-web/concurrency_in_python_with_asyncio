'''
Приложение «hello world» на Tkinter
'''
import time
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Hello world app')
window.geometry('400x200')


def say_hello():
    print('Привет!')


hello_button = ttk.Button(window, text='Скажи привет!', command=say_hello)
hello_button.pack()

window.mainloop()
