#GUI

from tkinter import *
import sqlite3

def sendQuery():
 c.execute(entry.get())
 pastQueries.append(entry.get())
 output.delete('1.0',END)
 output.insert(END,c.fetchall())
 conn.commit()
 entry.delete(0,END)
 prev = (-1)
 
def sendQuery2(event):
 sendQuery()
 
def getPrevious(event):
 global prev
 entry.delete(0,END)
 entry.insert(0,pastQueries[prev])
 if prev+len(pastQueries)>0:
  prev-=1
 
conn = sqlite3.connect('data.db')
c=conn.cursor()

prev = (-1)

root=Tk()
frame1=Frame(root)
label=Label(frame1,text='query')
entry=Entry(frame1,width=100)
output=Text(root)
button=Button(frame1,text='submit',command=sendQuery)
root.bind("<Return>",sendQuery2)
root.bind("<Escape>",quit)
root.bind("<Up>",getPrevious)

label.pack(side=LEFT)
entry.pack(side=LEFT)
button.pack(side=LEFT)
frame1.pack(side=TOP)
output.pack(side=BOTTOM,fill=X)

pastQueries=[]


root.mainloop()
conn.close()