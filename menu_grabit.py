from tkinter import *
import os
import random
informations="In this game, you try to collect\nas many apples (or something\nelse) as possible, while trying\nto watch out for the\nsurrounding enemies who try to kill\nyou. :D Some just walk\naround and some even follow you."
secret1 = "have you ever tried going down\nto the left corner\nwhen you had a score of 24?"
with open("grabit_opt.txt", "r") as folder:
    f_list = folder.readlines()
    # print(f_list)
f_list[0] = f_list[0].replace('\n', '')
if "\n" in f_list[1]:
    f_list[1] = f_list[1].replace('\n', '')
# print(f_list)
root = Tk()
root.iconbitmap(r'grabit_icon.ico')
root.resizable(0,0)
root.title("grabit.py")
root.geometry("400x350")
root.configure(bg="black")
def play():
    root.destroy()
    os.system("grabit.py")
def score():
    def allscores():
        os.system("grabit_allscores.txt")
    score = Toplevel()
    score.iconbitmap(r'grabit_icon.ico')
    score.resizable(0,0)
    score.title("Score")
    score.geometry("220x110")
    score.configure(bg="black")
    bestscore = Label(score, text="best score: "+f_list[0], font=("Comic Sans MS", 20, "bold"), bg="black", fg="white")
    lastscore = Label(score, text="last score: "+f_list[1], font=("Comic Sans MS", 20, "bold"), bg="black", fg="white")
    buttonscore = Button(score, text=":all scores:",  font=("Comic Sans MS", 10, "bold"), bg="black", fg="white", activebackground="gray", activeforeground="black", command=allscores)
    bestscore.pack()
    lastscore.pack()
    buttonscore.pack()
    score.mainloop()
def info():
    global informations, secret_random
    inf = Toplevel()
    inf.iconbitmap(r'grabit_icon.ico')
    def scrtbtn():
        if int(f_list[0])<=150:
            scrtwindow = Toplevel()
            scrtwindow.iconbitmap(r'grabit_icon.ico')
            scrtlabel = Label(scrtwindow, text="You need atleast score 150", font=("Comic Sans MS", 10, "bold"), bg="black", fg="white").pack()
            scrtwindow.mainloop()
        elif int(f_list[0])>=150:
            print("coming soon")
    inf.geometry("500x500")
    inf.resizable(0,0)
    inf.configure(bg="black")
    label = Label(inf, text=informations, font=("Comic Sans MS", 20, "bold"), bg="black", fg="white").pack()
    scrtbutton = Button(inf, text="secret button", font=("Comic Sans MS", 10, "bold"), width=12, bg="black", fg="white", activebackground="gray", activeforeground="black", command=scrtbtn)
    scrtbutton.pack()
    inf.mainloop()
def credit():
    crd = Toplevel()
    crd.iconbitmap(r'grabit_icon.ico')
    crd.resizable(0,0)
    crd.configure(bg="black")
    crd.mainloop()
header = Label(root, text="GRAB IT", font=("Comic Sans MS", 20, "bold"), bg="black", fg="white")
playbutton = Button(root, text="PLAY!", font=("Comic Sans MS", 20, "bold"), width=7, bg="black", fg="white", activebackground="gray", activeforeground="black", command=play)
scorebutton = Button(root, text="score", font=("Comic Sans MS", 20, "bold"), width=7, bg="black", fg="white", activebackground="gray", activeforeground="black", command=score)
infobutton = Button(root, text="info", font=("Comic Sans MS", 20, "bold"), width=7, bg="black", fg="white", activebackground="gray", activeforeground="black", command=info)
creditbutton = Button(root, text="credit", font=("Comic Sans MS", 20, "bold"), width=7, bg="black", fg="white", activebackground="gray", activeforeground="black", command=credit)
header.pack()
playbutton.pack()
scorebutton.pack()
infobutton.pack()
creditbutton.pack()
root.mainloop() 



