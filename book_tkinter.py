from tkinter import *
import book_database
import tkinter.messagebox as mb
from datetime import datetime as dt
import re

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #print(selected_tuple)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        IndexError

def view_command():
    list1.delete(0,END)
    for row in book_database.view():
        list1.insert(END,row)

def search_command():

    list1.delete(0,END)
    
    for row in book_database.view():
        #lst.append(row[3])
        #print(row[3])
        if (title_text.get().lower() in row[1].lower() and author_text.get().lower() in row[2].lower() and str(year_text.get()) in str(row[3]) and str(isbn_text.get()) in str(row[4])):            
            #print(lst)
            
            list1.insert(END,row)
       # elif author_text.get().lower() in row[2].lower():
        #    print(lst)
    #print(lst)
                
    
def add_command():
  # pattern=re.compile("[0-9]{4}")
   #pattern.match(year_text.get())
   if(int(year_text.get())>dt.now().year):
        mb.showinfo("","Please Enter a valid Year")    
   else:
        pattern=re.compile("[0-9]{13}$")
        pattern.match(isbn_text.get())
        if(pattern.match(isbn_text.get())):
            if(x.isalpha() or x.isspace() for x in author_text.get()):
                book_database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
                list1.delete(0,END)
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                search_command()
                list1.delete(0,(list1.size()-2))
                mb.showinfo("","Value Added")
            else:
                mb.showinfo("","Author name contains Numeric Value!!")
        else:
                    mb.showinfo("","Invalid isbn Number")

        #list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    book_database.delete(selected_tuple[0])
    mb.showinfo("","Entry Deleted!")
    list1.delete(0,END)
def update_command():
   if(int(year_text.get())>dt.now().year):
        mb.showinfo("","Please Enter a valid Year")    
   else:
       pattern=re.compile("[0-9]{13}$")
       pattern.match(isbn_text.get())
       if(pattern.match(isbn_text.get())):
           pattern=re.compile("[a-zA-Z]+([\s][a-zA-Z]^[0-9]+)*")
           pattern.match(author_text.get())
           if(pattern.match(author_text.get())):
               book_database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
               print(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
               mb.showinfo("","Entry Updated successfully")
               list1.delete(0,END)
               e1.delete(0,END)
               e2.delete(0,END)
               e3.delete(0,END)
               e4.delete(0,END)
           else:
               mb.showinfo("","Author name contains Numeric Value!!")
       else:
            mb.showinfo("","Invalid isbn Number")
window=Tk()
window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=8,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(window,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)
b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text=" Delete Selected ",width=12,command=delete_command)
b5.grid(row=6,column=3)

window.mainloop()
