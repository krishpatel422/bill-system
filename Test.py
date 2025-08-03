from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title('billing slip')
root.geometry('1280x720')
bg_color='#454545'




#======================================================================

c_name=StringVar()
c_phone=StringVar()
c_city=StringVar()
SN=IntVar()
SN.set('')
itm=StringVar()
Serial=StringVar()
Qty=IntVar()
Qty.set('')
Rate=IntVar()
Rate.set('')
Pen=IntVar()
Pen.set('')
Dep=IntVar()
Dep.set('')


bill_no=StringVar()
x=random.randint(1,99999)
bill_no.set(str(x))


l=[]

#======================================================================


def welcome():
    textarea.delete(0.0, END)
    textarea.insert(END, "\t\t Welcome To Pawan Electronic")
    textarea.insert(END, f'\n Bill Number:\t\t{bill_no.get()}')
    textarea.insert(END, f'\n Customer Name:\t\t{c_name.get()}')
    textarea.insert(END, f'\n Phone NO:\t\t{c_phone.get()}')
    textarea.insert(END, f'\n City or Village Name:\t\t{c_city.get()}')
    textarea.insert(END, f"\n========================================================================================================================")
    textarea.insert(END, f'\nS.No\t\tProduct\t       \tSer.No\t           QTY            Rate   \tPending \tDeposite')
    textarea.insert(END, f"\n========================================================================================================================\n")
    textarea.configure(font='arial 10 bold')


def additem():
    n = float(Dep.get())
    q = int(Qty.get())  # Quantity as int
    m = q * n  # Proper multiplication
    l.append(m)
    if itm.get() == '':
        messagebox.showerror('Error', 'Please enter the item')
    else:
        line = f'{SN.get():<15}{itm.get():<18}{Serial.get():<18}{Qty.get():<16}{Rate.get():<15}{Pen.get():<15}{Dep.get()}\n'
        textarea.insert((8.0+float(len(l)-1)), line)


def gbill():
    if c_name.get()=='' or c_phone.get()=='':
        messagebox.showerror('Error','Customer Details are must')
    else:
       tex=textarea.get('8.0',END)
       welcome()
       textarea.insert(END,tex)
       textarea.insert(END, f"\n==============================================================")
       textarea.insert(END, f"\nTotal paybill Amount :\t\t\t{sum(l)}")
       textarea.insert(END, f"\n==============================================================")
       savebill()


def savebill():
    op=messagebox.askyesno('save bill','Do you want to save to the boll')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("bill/"+str(c_name.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showerror('saved',f'bill no:{c_name.get()} saved successfully')
    else:
        return


def clear():

   c_name.set('')
   c_phone.set('')
   SN.set('')
   itm.set('')
   Serial.set('')
   Qty.set('')
   Rate.set('')
   Pen.set('')
   Dep.set('')
   welcome()


def exit():
    op = messagebox.askyesno('Exit','Do you really want to exit')
    if op>0:
        root.destroy()












#======================================================================

title=Label(root,text='billing Software',bg=bg_color, fg='white',font=('times new romman',14 , 'bold'),relief=GROOVE,bd=4)
title.pack(fill=X)

#======================================================================

F1=LabelFrame(root,text='Customer Details',bg=bg_color,fg='#008080',font=('time ner rommon',12,'bold'),relief="groove",bd=4)
F1.place(x=0,y=80,relwidth=1)

#======================================================================

cname_lbl=Label(F1,text='Customer Name', font=('times new rommon',14,'bold'),bg=bg_color ,fg='white')
cname_lbl.grid(row=0,column=0)

cname_txt=Entry(F1,width=12,font='arial 12 bold',relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

#======================================================================

cphone_lbl=Label(F1,text='Phone NO. ', font=('times new rommon',14,'bold'),bg=bg_color ,fg='white')
cphone_lbl.grid(row=0,column=2)

cphone_txt=Entry(F1,width=12,font='arial 12 bold',relief=SUNKEN,textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

#======================================================================

ccity_lbl=Label(F1,text='City or Village Name ', font=('times new rommon',14,'bold'),bg=bg_color ,fg='white')
ccity_lbl.grid(row=0,column=4)

ccity_txt=Entry(F1,width=12,font='arial 12 bold',relief=SUNKEN,textvariable=c_city)
ccity_txt.grid(row=0,column=5,padx=10,pady=5)



#======================================================================



F2=LabelFrame(root,text='product Details',bg=bg_color,fg='#008080',font=('time ner rommon',12,'bold'),relief="groove",bd=4)
F2.place(x=20,y=180,width=800,height=500)

#======================================================================

sn=Label(F2,text='S.No.',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
sn.grid(row=0,column=0, padx=10,pady=5)

sn_txt=Entry(F2,width=3,font='arial 12 bold',textvariable=SN)
sn_txt.grid(row=0,column=1,padx=10,pady=5)

#======================================================================

Itm=Label(F2,text='Product Name',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
Itm.grid(row=1,column=0, padx=30,pady=15)

Itm_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=itm)
Itm_txt.grid(row=1,column=1,padx=30,pady=15)

#======================================================================

serial=Label(F2,text='Serial Number',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
serial.grid(row=1,column=2, padx=10,pady=5)

serial_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=Serial)
serial_txt.grid(row=1,column=3,padx=10,pady=5)

#======================================================================

qty=Label(F2,text=' Product Quantity',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
qty.grid(row=2,column=0, padx=30,pady=15)

qty_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=Qty)
qty_txt.grid(row=2,column=1,padx=30,pady=15)

#======================================================================

rate=Label(F2,text='Product Rate',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
rate.grid(row=2,column=2, padx=10,pady=5)

rate_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=Rate)
rate_txt.grid(row=2,column=3,padx=10,pady=5)

#======================================================================

dep=Label(F2,text='Deposite Amount',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
dep.grid(row=3,column=0, padx=30,pady=15)

dep_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=Dep)
dep_txt.grid(row=3,column=1,padx=30,pady=15)

#======================================================================

pen=Label(F2,text='Pending Amount',font=('times new rommon',14,'bold'),bg=bg_color,fg='white')
pen.grid(row=3,column=2, padx=10,pady=5)

pen_txt=Entry(F2,width=12,font='arial 12 bold',textvariable=Pen)
pen_txt.grid(row=3,column=3,padx=10,pady=5)



#======================================================================



btn1=Button(F2,text='Add item', font='arial 15 bold',padx=5,pady=10,bg='#49f386',width=15,command=additem)
btn1.grid(row=4,column=0,padx=20,pady=30)

btn2=Button(F2,text='Generate Bill', font='arial 15 bold',padx=5,pady=10,bg='#49f386',width=15,command=gbill)
btn2.grid(row=4,column=1,padx=20,pady=30)

btn3=Button(F2,text='Clear', font='arial 15 bold',padx=5,pady=10,bg='#49f386',width=15,command=clear)
btn3.grid(row=5,column=0,padx=20,pady=30)

btn4=Button(F2,text='Exit', font='arial 15 bold',padx=5,pady=10,bg='#49f386',width=15,command=exit)
btn4.grid(row=5,column=1,padx=20,pady=30)



#======================================================================



F3=Frame(root,relief=GROOVE,bd=8)
F3.place(x=900,y=180,width=600,height=550)


bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=4).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()



welcome()

root.mainloop()
