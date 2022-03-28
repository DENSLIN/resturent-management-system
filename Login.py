from tkinter import *
import main, employee
from TkinterSidebar.pages.page import Page
import sqlite3 as sq3


try:
    database = sq3.connect('TkinterSidebar/data/hotel_database.db')
    cur = database.cursor()

    cur.execute("""CREATE TABLE worker(
                    Name text,
                    age integer,
                    contact integer,
                    shift text,
                    password text,
                    Money integer)""")
    print ("worker table created")
    cur.execute("""CREATE TABLE manager(
                    Name text,
                    age integer,
                    contact integer,
                    shift text,
                    password text)""")
    print ("worker table created")
    cur.execute("""CREATE TABLE inv_items(
                    Name text,
                    Quantity integer,
                    ptpp integer,
                    low integer,
                    price integer)""")
    print ("worker table created")
    cur.execute("""CREATE TABLE food_items(
                    Name text,
                    ingredients text,
                    price integer)""")
    print ("worker table created")
    database.commit()
    database.close()
    print("table created ")
except sq3.Error:
    print("table is all ready created ")

LoginFrame = Tk()
Label(LoginFrame, text='Edit Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
Label(LoginFrame, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
Name = Entry(LoginFrame, width=30)
Name.grid(column=1, row=1, padx=25, pady=20)
Name.delete(0, END)
Label(LoginFrame, text='Password  :- ').grid(column=0, row=2, padx=25, pady=20)
Pswd = Entry(LoginFrame, width=30, show="*")
Pswd.grid(column=1, row=2, padx=25, pady=20)
Button(LoginFrame, width=50, text="Add Employee", command=lambda: main.main()).grid(column=0, row=3, pady=20,
                                                                                         columnspan=2)
Pswd.delete(0, END)
LoginFrame.mainloop()



