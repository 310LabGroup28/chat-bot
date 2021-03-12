import sys
sys.path.append(sys.path[0]+"\lib")
import tkinter as tk
from responsechatbot import ChatbotResponse as cr


def show_entry_fields():
    print("First Name: %s" % (e1.get()))


def insertContent():
    #record = record + e1.get()
    # "how far is kelowna from vancouver?"
    reply = cr.getResponse(e1.get())
    print(reply)
    T.insert(tk.END, e1.get() + '\n', "odd")
    T.insert(tk.END, reply + '\n', "even")
    e1.delete(0, tk.END)
    

master = tk.Tk()
master.geometry("1000x400")


tk.Label(master, text="Question: ").grid(row=0, column=0)

e1 = tk.Entry(master, width=160)
e1.grid(row=1, column=0, padx=5, pady=5)

send = tk.Button(master, text='Show', command=insertContent)
send.grid(row=3, column=0, sticky=tk.W, pady=5)


record = "========hello, please enter your questions========"
T = tk.Text(master, height=20, width=140)
T.grid(row=5, column=0, sticky=tk.W, pady=4, padx=4)
T.tag_configure("even", background="#ffffff")
T.tag_configure("odd", background="#7bbfea")
T.insert(tk.END, record)



tk.mainloop()

