import tkinter as tk
from responsechatbot import ChatbotResponse as cr
from posTag_spellCheck import check, pos_tagging


def show_entry_fields():
    print("First Name: %s" % (e1.get()))


def insertContent():
    reply = ""
    cor = ""
    #    
    try:
        cor = checkSpelling()
        print(cor)
        reply = cr.getResponse( cor )
    except:
        reply = "I'm sorry, I didn't quite understand that.\nTry asking for help to see the scope of my functionality, or try asking another question.\n"

    print(reply)
    T.insert(tk.END, cor + '\n', "odd")
    T.insert(tk.END, reply + '\n', "even")
    e1.delete(0, tk.END)

def checkSpelling():
    sentence = e1.get()
    #print(pos_tagging(sentence))
    dic = check(sentence)
    tips = 'here are some spelling mistakes:\n'
    for k in dic:
        tips = tips + str(k) + ' -> ' + str(dic[k]) + '\n'
        sentence = sentence.replace(k, dic[k])
    if len(dic) == 0:
        tips = 'it seems all spelling are correct\n'    
    T.insert(tk.END, tips + '\n', "tip")
    print(tips)
    return sentence

def posTagging():
    sentence = e1.get()
    dic = pos_tagging(sentence)
    tips = 'here are the POS tagging:\n'
    for k in dic:
        tips = tips + str(k) + ' -> ' + str(dic[k]) + '\n'
    if len(dic) == 0:
        tips = 'it is empty\n'    
    T.insert(tk.END, tips + '\n', "tip")
    print(tips)
    return 

master = tk.Tk()
master.geometry("1000x400")


tk.Label(master, text="Say something to Chatbot below then press 'Send'").grid(row=0, column=0)

e1 = tk.Entry(master, width=160)
e1.grid(row=1, column=0, padx=5, pady=5)

send = tk.Button(master, text='Send', command=insertContent)
send.grid(row=3, column=0, sticky=tk.W, pady=5)

checkSpell = tk.Button(master, text='check spelling', command=checkSpelling)
checkSpell.grid(row=4, column=0, sticky=tk.W, pady=5)

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

