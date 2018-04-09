#_qRegister

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
  