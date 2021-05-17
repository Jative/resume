from tkinter import *
import tkinter as tk
import pyperclip

root = Tk()
root.geometry("500x510")
root.resizable(False, False)
root.title("Текст-анализатор")
root['bg'] = "gray70"

def paste():
    txt.insert(END, pyperclip.paste()+"\n")

def calc():
    inp = txt.get()
    for i in range(int(inp.count(" ")/2)):
    	inp = inp.replace("  ", " ")
    inp = inp.replace(" ,", ",")
    inp = inp.replace(" .", ".")
    inp = inp.replace(" !", "!")
    inp = inp.replace(" -", "-")
    inp = inp.replace(" –", "–")
    inp = inp.replace(" +", "+")
    inp = inp.replace(" :", ":")
    inp = inp.replace(" ;", ";")
    inp = inp.replace(" ?", "?")
    inp = inp.replace(" /", "/")
    inp = inp.replace(" *", "*")
    inp = inp.replace(" =", "=")
    inp = inp.replace(" (", "(")
    inp = inp.replace(" )", ")")
    inp = inp.replace(" ^", "^")
    inp = inp.replace(" %", "%")
    inp = inp.replace(" $", "$")
    inp = inp.replace(" ~", "~")
    inp = inp.replace(" `", "`")
    inp = inp.replace(" \\", "\\")
    inp = inp.replace(" |", "|")
    inp = inp.replace(" >", ">")
    inp = inp.replace(" <", "<")
    abz = str(inp.count("\n"))
    inp = inp.replace("\n", " ")
    slova = str(inp.count(" "))
    if inp.count(" ") == len(inp):
    	slova = "0"

    info['text'] = "Количество слов в тексте: "+slova+"\nКоличество символов в тексте без пробелов: "+str(len(inp)-inp.count(" "))+"\nКоличество абзацей: "+abz

start = Label(root, text = "Введи текст:", font = "Consolas 10", bg = "gray70")
txt = Text(root, font = "Consolas 8", bg = "gray75", width = 78, height = 25, borderwidth = 1)
scroll = Scrollbar(root, command=txt.yview, width = 12)
btn_paste = Button(root, text = "Вставить скопированный текст!", command = paste, font = "Consolas 10", bg = "gray40", fg = "white", borderwidth = 4)
btn = Button(root, text = "Анализировать!", font = "Consolas 10", command = calc, bg = "gray40", fg = "white", borderwidth = 4)
info = Label(root, text = "", font = "Consolas 10", bg = "gray70")

scroll.pack(side=RIGHT, fill=Y)
start.pack(pady=5)
btn_paste.pack(pady=5)
txt.pack(pady=5)
btn.pack(pady=5)
info.pack(pady=5)

txt.config(yscrollcommand=scroll.set)
root.mainloop()