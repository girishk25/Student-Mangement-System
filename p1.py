from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import socket
import requests
import bs4

root=Tk()
root.title("S.M.S")
root.geometry("500x600+400+200")
root.configure(background='#B6FF33')

def f1():
    adst.deiconify()
    root.withdraw()
    adst_entrno.focus()
    
def f2():
    root.deiconify()
    adst.withdraw()
   
def f3():
    vist.deiconify()
    root.withdraw()
    vist_stdata.delete(1.0,END)
    con=None
    try:
        con=connect("sample.db")  #Name of Db
        cursor=con.cursor()
        sql="select * from student"
        cursor.execute(sql)
        data=cursor.fetchall()
        msg=""
        for d in data:
            msg=msg +"Rno: "+str(d[0]) + " Name: "+str(d[1])+ " Marks: "+str(d[2]) +"\n"
        vist_stdata.insert(INSERT,msg)
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
def f4():
    root.deiconify()
    vist.withdraw()
    
def f5():
    con=None
    try:
        con=connect("sample.db")
        cursor=con.cursor()
        sql="insert into student values('%d','%s','%d')"
        rno=int(adst_entrno.get())
        if rno<1:
            raise Exception("Rno should be Positive")
        name=adst_entname.get()
        if (not name.isalpha()) or (len(name)<2):
            raise Exception("Name should contain alphabets of min length 2")
        marks=int(adst_entmarks.get())
        if (marks<0 or marks>100):
            raise Exception("Marks cannot be less than 0 and more than 100")
        cursor.execute(sql %(rno,name,marks))
        con.commit()
        showinfo("Success","Record Added")
    except Exception as e:
        con.rollback()
        showerror("Issue","Only Integers are allowed")
    finally:
        if con is not None:
            con.close()
        adst_entrno.delete(0,END)
        adst_entname.delete(0,END)
        adst_entmarks.delete(0,END)
        adst_entrno.focus()

def f6():
    updt.deiconify()
    root.withdraw()
    updt_entrno.focus()

def f7():
        root.deiconify()
        updt.withdraw()
        
def f8():
    con=None
    try:
        con=connect("sample.db")
        cursor=con.cursor()
        sql="update student set name='%s', marks='%d' where rno='%d'"
        rno=int(updt_entrno.get())
        if rno<1:
            raise Exception("Rno should be Positive")
        name=updt_entname.get()
        if (not name.isalpha()) or (len(name)<2):
            raise Exception("Name should contain alphabets of min length 2")
        marks=int(updt_entmarks.get())
        if (marks<0 or marks>100):
            raise Exception("Marks cannot be less than 0 and more than 100")
        cursor.execute(sql %(name,marks,rno))
        if cursor.rowcount>0:
            con.commit()
            showinfo("Success","Record Updated")
        else:
            showerror("Error","Record does not exists....")
        
    except Exception as e:
        con.rollback()
        showerror("Updation Issue",e)
    finally:
        if con is not None:
            con.close()
        updt_entrno.delete(0,END)
        updt_entname.delete(0,END)
        updt_entmarks.delete(0,END)
        updt_entrno.focus()
def f9():
    delst.deiconify()
    root.withdraw()
    delst_entrno.focus()
    
def f10():
    root.deiconify()
    delst.withdraw()
    
def f11():
    con=None
    try:
        con=connect("sample.db")      
        cursor=con.cursor()
        sql="delete from student where rno='%d'"
        rno=int(delst_entrno.get())
        cursor.execute(sql%(rno))
        if cursor.rowcount >0:
            con.commit()
            showinfo("Success","Record Deleted")
            delst_entrno.focus()
        else:
            showerror("","Record does not exists....")
            delst_entrno.focus()
    except Exception as e:
        showerror("Deletion Issue: ",e)
        delst_entrno.focus()
        con.rollback()
    finally:
        if con is not None:
            con.close()
        delst_entrno.delete(0,END)

def f12():
    con=None
    try:
        name=[]
        marks=[]
        con=connect("sample.db")
        cursor=con.cursor()
        sql="select name from student"
        cursor.execute(sql)
        rows=cursor.fetchall()
        name=list(itertools.chain(*rows))
        sql="select marks from student"
        cursor.execute(sql)
        rows1=cursor.fetchall()
        marks=list(itertools.chain(*rows1))
        color_1=['red','green','blue']
        plt.bar(name,marks,linewidth=2,color=color_1)
        plt.xlabel("Names")
        plt.ylabel("Marks")
        plt.title("Batch Information")
        plt.show()
    except Exception as e:
        showerror("Chart Issue:",e)
    finally:
        if con is not None:
            con.close()


def f13(lblLocation):
    
    try:
        google_address=("www.google.com",80)
        socket.create_connection(google_address)
        print("CONNECTED to Location")                      #~~~~~~~~
        web_address="https://ipinfo.io/"
        response=requests.get(web_address)
       # print(response) #200....-->correct , 4...-->error
        
        data=response.json()
        print(data)
            
        city_name =data['city']
        print(city_name)
    
        lblLocation.config(text="Location: "+ city_name)
        return city_name
        
    except Exception as e:
        showerror("connection Issue: ",e)

def f14(lblTemp):
    try:
	
        google_address=("www.google.com",80)
        
        socket.create_connection(google_address)
        
        print("Connected to Weather")
        
        city=a
        print("City: ",city)
        a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
        
        a2="&q="+city
        
        a3="&appid=c6e315d09197cec231495138183954bd"
        web_address=a1+a2+a3
        

        response =requests.get(web_address)
        
     
        
        data=response.json()  
        #print(data)        
      
        main =data['main']
       
        temp1=main['temp']
        q=str(temp1)
        print("Temp:",temp1)
        lblTemp.config(text="Temp:"+q)
        
    except OSError as e:
        showerror("Connection Issue: ",e)
    except KeyError as e:
        showinfo("check Location name ",e)

def f15(lblQuotd):
    try:
        web_address="https://www.brainyquote.com/quote_of_the_day"
        res= requests.get(web_address)
        #print(res)
        
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        #print(soup)
        
        info=soup.find_all("img",{"class":"p-qotd"})
        #print(info[0])
        quote=info[0]['alt']
        lblQuotd.config(text="QUOTD: "+quote)
    except Exception as e:
        showerror("Issue: ",e)

   
btnAdd=Button(root,text="Add",width=10,font=("arial",18,"bold"),command=f1)
btnView=Button(root,text="View",width=10,font=("arial",18,"bold"),command=f3)
btnUpdate=Button(root,text="Update",width=10,font=("arial",18,"bold"),command=f6)
btnDelete=Button(root,text="Delete",width=10,font=("arial",18,"bold"),command=f9)
btnCharts=Button(root,text="Charts",width=10,font=("arial",18,"bold"),command=f12)
lblLocation=Label(root,text="Location:",bg="#B6FF33",bd=3,relief="solid",width=20,font=("arial",18,"bold"))
lblTemp=Label(root,text="Temp:",width=10,bg="#B6FF33",bd=3,relief="solid",font=("arial",18,"bold"))
lblQuotd=Label(root,text="QUOTD:",width=100,bg="#B6FF33",bd=3,relief="solid",font=("arial",18,"bold"))



btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)
lblLocation.pack(pady=10,side=LEFT)
a=f13(lblLocation)

lblTemp.pack(pady=10,side=RIGHT)
f14(lblTemp)
lblQuotd.pack(pady=10,side=LEFT)
f15(lblQuotd)
lblQuotd.place(relx=0.0,rely=1.0,anchor='sw')



#For Add student

adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("500x600+400+200")
adst.configure(background='light blue')



adst_lblrno = Label(adst,text="Enter rno",font=("arial",18,"bold"))
adst_entrno = Entry(adst,bd=5,font=("arial",18,"bold"))
adst_lblname =Label(adst,text="Enter Name",font=("arial",18,"bold"))
adst_entname =Entry(adst,bd=5,font=("arial",18,"bold"))
adst_lblmarks =Label(adst,text="Enter Marks",font=("arial",18,"bold"))
adst_entmarks= Entry(adst,bd=5,font=("arial",18,"bold"))
adst_btnsave=Button(adst,text="Save",font=("arial",18,"bold"),command=f5)
adst_btnback=Button(adst,text="Back",font=("arial",18,"bold"),command=f2)

adst_lblrno.pack(pady=10)
adst_entrno.pack(pady=10)
adst_lblname.pack(pady=10)
adst_entname.pack(pady=10)
adst_lblmarks.pack(pady=10)
adst_entmarks.pack(pady=10)
adst_btnsave.pack(pady=10)
adst_btnback.pack(pady=10)

adst.withdraw() 


#for View student

vist =Toplevel(root)
vist.title("View Student")
vist.geometry("500x400+400+200")
vist.configure(background='light blue')



vist_stdata=ScrolledText(vist,width=35,height=10,font=("arial",18,"bold"))  #st-->scrolled text
vist_btnback=Button(vist,text="Back",font=("arial",18,"bold"),command=f4)


vist_stdata.pack(pady=10)
vist_btnback.pack(pady=10)
vist.withdraw()



#For Update student

updt=Toplevel(root)
updt.title("Update Student")
updt.geometry("500x600+400+200")
updt.configure(background='orange')



updt_lblrno = Label(updt,text="Enter rno",font=("arial",18,"bold"))
updt_entrno = Entry(updt,bd=5,font=("arial",18,"bold"))
updt_lblname =Label(updt,text="Enter new Name",font=("arial",18,"bold"))
updt_entname =Entry(updt,bd=5,font=("arial",18,"bold"))
updt_lblmarks =Label(updt,text="Enter new Marks",font=("arial",18,"bold"))
updt_entmarks= Entry(updt,bd=5,font=("arial",18,"bold"))
updt_btnsave=Button(updt,text="Save",font=("arial",18,"bold"),command=f8)
updt_btnback=Button(updt,text="Back",font=("arial",18,"bold"),command=f7)

updt_lblrno.pack(pady=10)
updt_entrno.pack(pady=10)
updt_lblname.pack(pady=10)
updt_entname.pack(pady=10)
updt_lblmarks.pack(pady=10)
updt_entmarks.pack(pady=10)
updt_btnsave.pack(pady=10)
updt_btnback.pack(pady=10)

updt.withdraw() 

#for Delete

delst=Toplevel(root)
delst.title("Delete Student")
delst.geometry("500x400+400+200")
delst.configure(background='light blue')


delst_lblrno = Label(delst,text="Enter rno",font=("arial",18,"bold"))
delst_entrno = Entry(delst,bd=5,font=("arial",18,"bold"))
delst_btndelete=Button(delst,text="Delete",font=("arial",18,"bold"),command=f11)#,command=f11
delst_btnback=Button(delst,text="Back",font=("arial",18,"bold"),command=f10)


delst_lblrno.pack(pady=10)
delst_entrno.pack(pady=10)
delst_btndelete.pack(pady=10)
delst_btnback.pack(pady=10)

delst.withdraw()



root.mainloop()