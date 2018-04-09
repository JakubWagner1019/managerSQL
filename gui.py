#GUI

from tkinter import *
import sqlite3

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

class QueryRegister():
 def __init__(self):
  self.data=[]
  self.pos=0
 def addQuery(self,query):
  self.data.append(query)
  self.pos=len(self.data)
 def getOlderQuery(self):
  if len(self.data)==0:
   return ''
  if self.pos>0:
   self.pos-=1
  return self.data[self.pos]
 def getNewerQuery(self):
  if not self.data:
   return ''
  if self.pos<len(self.data):
   self.pos+=1
  if self.pos==len(self.data):
   return '' 
  return self.data[self.pos]
  

  
conn = sqlite3.connect('data.db')
c=conn.cursor()

qreg=QueryRegister()

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