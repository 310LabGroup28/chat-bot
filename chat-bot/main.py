import tkinter as tk
from tkinter import messagebox
from nltk.corpus import wordnet
import nltk
from responsechatbot import ChatbotResponse as cr
from posTag_spellCheck import SpellCheckPosTag as scpt
from outofscoperesponse import OutOfScope as oos


nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

def show_entry_fields():
    print("First Name: %s" % (e1.get()))


def insertContent():
    reply = ""
    question = e1.get()   
    try:
        reply = cr.getResponse(question)
    except:
        reply = oos.getResponse()

    print(reply)
    T.insert(tk.END, "User: " + question + '\n', "odd")
    T.insert(tk.END, "Chatbot: " + reply + '\n', "even")
    e1.delete(0, tk.END)


def posTagging():
    MsgBox = tk.messagebox.askquestion ('POS Tag','Do you want to check the grammar?')
    if MsgBox == 'yes':
        sentence = e1.get()
        dic = scpt.pos_tagging(sentence)
        tips = 'I found the following POS tags:\n'
        for k in dic:
            tips = tips + str(k) + ' -> ' + str(dic[k]) + '\n'
        if len(dic) == 0:
            tips = 'No POS tags found.\n'    
        T.insert(tk.END, tips, "tip")
        print(tips)
        return


master = tk.Tk()
master.geometry("1132x420")
master.configure(bg='pink') 


tk.Label(master, text="Say something to Chatbot below then press 'Send'", bg='black', fg='pink', font=('Berlin Sans FB Demi', 14), width=104, height=1).grid(row=0, column=0,sticky=tk.W)

e1 = tk.Entry(master, width=172, font=('Times New Roman', 10))
e1.grid(row=1, column=0,sticky=tk.W, padx=5, pady=5)

send = tk.Button(master, text='Send',command=insertContent, width=6, height=1, bg='white', fg='black', font=('Times New Roman', 10)).place(x=1050, y=30)


posTag = tk.Button(master, text='POS tagging', command=posTagging, width=10, height=1, bg='white', fg='black', font=('Times New Roman', 10)).place(x=1049, y=390)

tk.Label(master, text="Designed by UBCO COSC 310 Group 28", bg='pink', font=('MV Boli', 11), width=102, height=1).grid(row=4, column=0,sticky=tk.W)

record = "==================================================================Chat Log==================================================================\n"
T = tk.Text(master, height=20, width=140,)
T.grid(row=3, column=0,sticky=tk.W, pady=4, padx=4)
T.tag_configure("even", background="#ffffff")
T.tag_configure("odd", background="#7bbfea")
T.tag_configure("tip", background="#ccffff")
T.insert(tk.END, record)



tk.mainloop()

