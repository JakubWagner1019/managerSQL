#_SQLmanager

import sqlite3

class SQLmanager():
 def __init__(self,file):
  self.connection=sqlite3.connect(file)
  self.cursor=self.connection.cursor()
 def reconnect(self,file):
  self.connection.close()
  self.connection=sqlite3.connect(file)
  self.cursor=self.connection.cursor()
 def execute(self,query):
  self.cursor.execute(query)
  result=self.cursor.fetchall()
  self.connection.commit()
  return result
 def close(self):
  self.connection.close()
  