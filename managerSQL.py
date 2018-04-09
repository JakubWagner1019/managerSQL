#_managerSQL

from tkinter import *
from tkinter import filedialog
import qRegister as qr
import SQLmanager as sql


def sendQuery():
 query=entry.get()
 result=sqlManager.execute(query)
 qreg.addQuery(query)
 output.delete('1.0',END)
 output.insert(END,result)
 entry.delete(0,END)
 
def sendQuery2(event):
 sendQuery()
 
def getOlder(event):
 entry.delete(0,END)
 entry.insert(0,qreg.getOlderQuery()) 
 
def getNewer(event):
 entry.delete(0,END)
 entry.insert(0,qreg.getNewerQuery()) 

def establishConnection():
 file = filedialog.askopenfilename(filetypes=(("Databases","*.db"),("All files","*.*")))
 output.delete('1.0',END)
 sqlManager.reconnect(file)
 output.insert(END,"Established a new connection"+file)
 
sqlManager=sql.SQLmanager('data.db')
qreg=qr.QueryRegister()

root=Tk()

menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="Connection",menu=subMenu)
subMenu.add_command(label="Establish a connection...",command=establishConnection)

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

root.mainloop()
sqlManager.close()