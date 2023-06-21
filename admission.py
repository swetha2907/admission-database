#python database for admission

import sys;
import sqlite3; 
import re   

conn=sqlite3.connect("admissiondb")
cur=conn.cursor()

class  admissiondb:
    try:
        def __init__(self,Uname,dept,cutoff,jeescore):
            self.User_name=Uname
            self.User_dept=dept
            self.User_cutoff=cutoff
            self.User_jeescore=jeescore
        def getUname(self):
            return self.User_name
        def getdept(self):
            return self.User_dept
        def getcutoff(self):
            return self.User_cutoff
        def getjeescore(self):
            return self.User_jeescore
        
    
        def setUname(self,val):
            self.User_name=val 
        def setdept(self,val):
            self.User_dept=val 
        def setcutoff(self,val):
            self.User_cutoff=val
        def setjeescore(self,val):
            self.User_jeescore=val
            
            
    except NameError:
        print("ERROR")
class cls1:
    def general(self):
        print("***************************")
        print("ADMISSION DETAILS")
        print("***************************")
        print("1 Enter admission details")
        print("2 for printdetails")
        n=int(input("Enter your choice:").strip())
        if(n==1):
            self.admission()
        else:
            self.printdetails()
    def admission(self):
        try:
            conn.execute('''drop table admissiondb''')
            conn.execute('''CREATE TABLE admissiondb(Uname TEXT NOT NULL,dept INT NOT NULL,cutoff int not null,jeescore int);''')
            
            
            add=admissiondb(None,None,None,None)
            add.setUname(input("Enter User Name: "))
            add.setdept(input("Choose Department: "))
            add.setcutoff(input("Enter Cutoff: "))
            add.setjeescore(input("Enter JEE score: "))
            conn.execute("insert into admissiondb values(?,?,?,?)",(add.getUname(),add.getdept(),add.getcutoff(),add.getjeescore()))
            cls1.addagain(self)
        except NameError:
            print("ERROR")
        finally:
            conn.commit()
    def printdetails(self):
        
        cur.execute("select * from admissiondb")
        for i in cur.fetchall():
           
            print(i)
    def addagain(self):
        mm=input("Any more admission details to be inserted(y/n)")
        if(mm=='Y' or mm=='y'):
            cls1.general(self)
        
          
st=cls1()
st.general()

