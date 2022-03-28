from tkinter import *
import main, employee
from TkinterSidebar.pages.page import Page



LoginFrame = Tk()
Label(LoginFrame, text='Edit Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
Label(LoginFrame, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
Name = Entry(LoginFrame, width=30)
Name.grid(column=1, row=1, padx=25, pady=20)
Name.delete(0, END)
Label(LoginFrame, text='Password  :- ').grid(column=0, row=2, padx=25, pady=20)
Pswd = Entry(LoginFrame, width=30, show="*")
Pswd.grid(column=1, row=2, padx=25, pady=20)
Button(LoginFrame, width=50, text="Add Employee", command=lambda: employee.employee()).grid(column=0, row=3, pady=20,
                                                                                         columnspan=2)
Pswd.delete(0, END)
LoginFrame.mainloop()



