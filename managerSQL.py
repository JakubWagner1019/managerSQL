#_managerSQL

from tkinter import *
import sqlite3
import qRegister as qr

def sendQuery():
 c.execute(entry.get())
 qreg.addQuery(entry.get())
 output.delete('1.0',END)
 output.insert(END,c.fetchall())
 conn.commit()
 entry.delete(0,END)
 
def sendQuery2(event):
 sendQuery()
 
def getOlder(event):
 entry.delete(0,END)
 entry.insert(0,qreg.getOlderQuery()) 
 
def getNewer(event):
 entry.delete(0,END)
 entry.insert(0,qreg.getNewerQuery()) 
 

  
conn = sqlite3.connect('data.db')
c=conn.cursor()

qreg=qr.QueryRegister()

root=Tk()
frame1=Frame(root)
label=Label(frame1,text='query')
entry=Entry(frame1,width=100)
output=Text(root)
button=Button(frame1,text='submit',command=sendQuery)
root.bind("<Return>",sendQuery2)
root.bind("<Escape>",quit)
root.bind("<Up>",getOlder)
root.bind("<Down>",getNewer)


label.pack(side=LEFT)
entry.pack(side=LEFT)
button.pack(side=LEFT)
frame1.pack(side=TOP)
output.pack(side=BOTTOM,fill=X)

pastQueries=[]


root.mainloop()
conn.close()