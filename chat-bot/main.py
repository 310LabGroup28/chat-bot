import tkinter as tk
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
master.geometry("1000x400")


tk.Label(master, text="Say something to Chatbot below then press 'Send'").grid(row=0, column=0)

e1 = tk.Entry(master, width=160)
e1.grid(row=1, column=0, padx=5, pady=5)

send = tk.Button(master, text='Send', command=insertContent)
send.grid(row=3, column=0, sticky=tk.W, pady=5)

posTag = tk.Button(master, text='POS tagging', command=posTagging)
posTag.grid(row=5, column=0, sticky=tk.W, pady=5)

record = "==========================================================Chat Log==========================================================\n"
T = tk.Text(master, height=20, width=140)
T.grid(row=6, column=0, sticky=tk.W, pady=4, padx=4)
T.tag_configure("even", background="#ffffff")
T.tag_configure("odd", background="#7bbfea")
T.tag_configure("tip", background="#ccffff")
T.insert(tk.END, record)



tk.mainloop()

