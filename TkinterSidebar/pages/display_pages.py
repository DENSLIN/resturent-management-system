from ..pages.page import *
from ..data import Data
from TkinterSidebar.scrollbar import *
import tkinter as tk


"""
defualt widget color:

#201F1E
"""
def_bg = "#201F1E"
def_fg = "lightgrey"

class HomePage(Page):
    def __init__(self, parent):
        print("Showning home page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Einstellungen", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)


class UpdateWorkerPage(Page):
    def __init__(self, parent):
        print("Showning home page")

        # init page/ delete old page
        Page.__init__(self, parent)

        buttonEdit = {}
        buttondelete = {}
        workerData = Data.WorkerData.workerData
        UpdateWorkerFrame = Frame(self,width=1000,height=1000,bg="grey")
        UpdateWorkerFrame.pack()
        Label(UpdateWorkerFrame, text='List of workers', font="bold",bg="grey").grid(column=0, row=0, padx=25, pady=20)
        Label(UpdateWorkerFrame, text='Name', font="bold",bg="grey").grid(column=0, row=1, padx=10, pady=10)
        Label(UpdateWorkerFrame, text='passwords', font="bold",bg="grey").grid(column=1, row=1, padx=10, pady=10)
        Label(UpdateWorkerFrame, text='Money', font="bold",bg="grey").grid(column=2, row=1, padx=10, pady=10)
        count = 2

        def deleteworker(name):
            print(name + "deleted")

            UpdateWorkerPage(parent)

        def editworker(name):
            print(name + " edit")
            editWorkerDetails = Tk()
            editWorkerDetails.geometry("400x200")
            Label(editWorkerDetails, text='Edit Details ',font = "bold").grid(column = 0,row = 0,padx = 25,pady=20)
            Label(editWorkerDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(editWorkerDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.insert(0, name)

            def update():
                name = Name.get()
                workerData[1][1]=name
                print(name)
                editWorkerDetails.destroy()
                UpdateWorkerPage(parent)

            Button(editWorkerDetails, text="Save", width=50, command=lambda: update()).grid(column=0, row=2,columnspan=2)
            editWorkerDetails.mainloop()

        def AddNewWorker():
            print("new employee")
            AddNewPage=Tk()
            Label(AddNewPage, text='Edit Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(AddNewPage, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(AddNewPage, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.delete(0, END)
            Label(AddNewPage, text='Password  :- ').grid(column=0, row=2, padx=25, pady=20)
            Pswd = Entry(AddNewPage, width=30,show="*")
            Pswd.grid(column=1, row=2, padx=25, pady=20)
            def update():
                name = Name.get()
                workerData[1][1]=name
                print(name)
                AddNewPage.destroy()
                UpdateWorkerPage(parent)
            Button(AddNewPage,width=50,text="Add Employee",command=lambda:update()).grid(column=0,row =3,pady=20,columnspan=2)
            Pswd.delete(0, END)
            AddNewPage.mainloop()
        for data in workerData:
            Label(UpdateWorkerFrame, text=data[0],bg="grey").grid(column=0, row=count, padx=5, pady=5)
            Label(UpdateWorkerFrame, text="******",bg="grey").grid(column=1, row=count, padx=5, pady=5)
            Label(UpdateWorkerFrame, text=data[2],bg="grey").grid(column=2, row=count, padx=5, pady=5)

            def func(x=data[0]):
                return editworker(x)
            buttonEdit[data[0]] = Button(UpdateWorkerFrame, text='edit', command=func).grid(column=3, row=count)

            def func(x=data[0]):
                return deleteworker(x)
            buttondelete[data[0]] = Button(UpdateWorkerFrame, text='delete', command=func).grid(column=4, row=count)

            count += 1
        Button(UpdateWorkerFrame,text="Add New Employee", width=25, command=lambda: AddNewWorker()).grid(column=0,row=count,columnspan=3)

class UpdateFoodMenu(Page):
    def __init__(self, parent):
        print("Showning settings page")


        # init page/ delete old page
        Page.__init__(self, parent)

        buttonEdit = {}
        buttondelete = {}
        menuData = Data.WorkerData.menuData

        container=Frame(self)
        canvas = tk.Canvas(container,height=500,width= 500,bg='light gray')
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        UpdateMenuFrame = Frame(canvas,bg='light gray')

        UpdateMenuFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=UpdateMenuFrame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        Label(UpdateMenuFrame, text='Menu', font="bold", bg=def_fg).grid(column=0, row=0, padx=25, pady=20)
        Label(UpdateMenuFrame, text='Name', font="bold", bg=def_fg).grid(column=0, row=1, padx=10, pady=10)
        Label(UpdateMenuFrame, text='Quantity', font="bold", bg=def_fg).grid(column=1, row=1, padx=10, pady=10)
        Label(UpdateMenuFrame, text='price', font="bold", bg=def_fg).grid(column=2, row=1, padx=10, pady=10)
        count = 2

        def DeleteFood(id):
            print(menuData[id][0] + "deleted")
            menuData[id][0]='Null'
            UpdateFoodMenu(parent)

        def EditFood(id):
            print(menuData[id][0] + " edit")
            editfoodDetails = Tk()
            Label(editfoodDetails, text='Edit Food Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(editfoodDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(editfoodDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.insert(0,menuData[id][0])
            Label(editfoodDetails, text='Quantity :- ').grid(column=0, row=2, padx=25, pady=20)
            Qty = Entry(editfoodDetails, width=30)
            Qty.grid(column=1, row=2, padx=25, pady=20)
            Qty.insert(0,menuData[id][1])
            Label(editfoodDetails, text='price :- ').grid(column=0, row=3, padx=25, pady=20)
            price = Entry(editfoodDetails, width=30)
            price.grid(column=1, row=3, padx=25, pady=20)
            price.insert(0, menuData[id][2])

            def update():
                name = Name.get()
                menuData[id][0] = str(Name.get())
                menuData[id][1] = int(Qty.get())
                menuData[id][2] = int(price.get())
                print(name)
                editfoodDetails.destroy()
                UpdateFoodMenu(parent)

            Button(editfoodDetails, text="Save", width=50, command=lambda: update()).grid(column=0, row=4,
                                                                                            columnspan=2,pady=25)
            editfoodDetails.mainloop()

        def AddNewFoodPage():
            print("New Food")
            AddNewFoodDetails = Tk()
            Label(AddNewFoodDetails, text='New Food Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(AddNewFoodDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(AddNewFoodDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.delete(0, END)
            Label(AddNewFoodDetails, text='Quantity :- ').grid(column=0, row=2, padx=25, pady=20)
            Qty = Entry(AddNewFoodDetails, width=30)
            Qty.grid(column=1, row=2, padx=25, pady=20)
            Qty.delete(0, END)
            Label(AddNewFoodDetails, text='price :- ').grid(column=0, row=3, padx=25, pady=20)
            price = Entry(AddNewFoodDetails, width=30)
            price.grid(column=1, row=3, padx=25, pady=20)
            price.delete(0, END)

            def update():
                name = Name.get()
                menuData.append([Name.get(), Qty.get(), price.get()])
                print(name)
                AddNewFoodDetails.destroy()
                UpdateFoodMenu(parent)

            Button(AddNewFoodDetails, width=50, text="Add New Food", command=lambda: update()).grid(column=0, row=4, pady=20,
                                                                                             columnspan=2)
            AddNewFoodDetails.mainloop()

        for data in menuData:
            if(data[0]=="Null"):
                count += 1
                continue
            Label(UpdateMenuFrame, text=data[0], bg=def_fg).grid(column=0, row=count, padx=25, pady=20)
            Label(UpdateMenuFrame, text=data[1], bg=def_fg).grid(column=1, row=count, padx=25, pady=20)
            Label(UpdateMenuFrame, text=data[2], bg=def_fg
                  ).grid(column=2, row=count, padx=25, pady=20)

            def func(x=count-2):
                return EditFood(x)

            buttonEdit[data[0]] = Button(UpdateMenuFrame, text='edit', command=func).grid(column=3, row=count, padx=25, pady=20)

            def func(x=count-2):
                return DeleteFood(x)

            buttondelete[data[0]] = Button(UpdateMenuFrame, text='delete', command=func).grid(column=4, row=count, padx=25, pady=20)

            count += 1
        Button(UpdateMenuFrame, text="Add New Food", width=25, command=lambda: AddNewFoodPage()).grid(column=3,
                                                                                                          row=1,
                                                                                                      columnspan=2)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class UpdateManagerPage(Page):
    def __init__(self, parent):
        print("Showning home page")

        # init page/ delete old page
        Page.__init__(self, parent)

        buttonEdit = {}
        buttondelete = {}
        ManagerData = Data.WorkerData.ManagerData
        UpdateManagerFrame = Frame(self,width=1000,height=1000,bg="grey")
        UpdateManagerFrame.pack()
        Label(UpdateManagerFrame, text='List of workers', font="bold",bg="grey").grid(column=0, row=0, padx=25, pady=20)
        Label(UpdateManagerFrame, text='Name', font="bold",bg="grey").grid(column=0, row=1, padx=10, pady=10)
        Label(UpdateManagerFrame, text='passwords', font="bold",bg="grey").grid(column=1, row=1, padx=10, pady=10)
        Label(UpdateManagerFrame, text='Money', font="bold",bg="grey").grid(column=2, row=1, padx=10, pady=10)
        count = 2

        def deletemanager(id):
            print(ManagerData[id][0])
            ManagerData[id][0]="Null"
            UpdateManagerPage(parent)

        def editmanager(name):
            print(name + " edit")
            editWorkerDetails = Tk()
            editWorkerDetails.geometry("400x200")
            Label(editWorkerDetails, text='Edit Details ',font = "bold").grid(column = 0,row = 0,padx = 25,pady=20)
            Label(editWorkerDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(editWorkerDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.insert(0, name)

            def update():
                name = Name.get()
                ManagerData[1][1]=name
                print(name)
                editWorkerDetails.destroy()
                UpdateManagerPage(parent)

            Button(editWorkerDetails, text="Save", width=50, command=lambda: update()).grid(column=0, row=2,columnspan=2)
            editWorkerDetails.mainloop()

        def AddNewManager():
            print("new Manager")
            AddNewPage=Tk()
            Label(AddNewPage, text='Edit Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(AddNewPage, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(AddNewPage, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.delete(0, END)
            Label(AddNewPage, text='Password  :- ').grid(column=0, row=2, padx=25, pady=20)
            Pswd = Entry(AddNewPage, width=30,show="*")
            Pswd.grid(column=1, row=2, padx=25, pady=20)
            def update():
                name = Name.get()
                ManagerData[1][1]=name
                print(name)
                AddNewPage.destroy()
                UpdateManagerPage(parent)
            Button(AddNewPage,width=50,text="Add Manager",command=lambda:update()).grid(column=0,row =3,pady=20,columnspan=2)
            Pswd.delete(0, END)
            AddNewPage.mainloop()
        for data in ManagerData:
            if data[0]=="Null":
                continue
            Label(UpdateManagerFrame, text=data[0],bg="grey").grid(column=0, row=count, padx=5, pady=5)
            Label(UpdateManagerFrame, text="******",bg="grey").grid(column=1, row=count, padx=5, pady=5)
            Label(UpdateManagerFrame, text=data[2],bg="grey").grid(column=2, row=count, padx=5, pady=5)

            def func(x=count-2):
                return editmanager(x)
            buttonEdit[data[0]] = Button(UpdateManagerFrame, text='edit', command=func).grid(column=3, row=count)

            def func(x=count-2):
                return deletemanager(x)
            buttondelete[data[0]] = Button(UpdateManagerFrame, text='delete', command=func).grid(column=4, row=count)

            count += 1
        Button(UpdateManagerFrame,text="Add New Manager", width=25, command=lambda: AddNewManager()).grid(column=0,row=count,columnspan=3)




class SettingsPage(Page):
    def __init__(self, parent):
        print("Showning settings page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Einstellungen", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class ManageInventoryPage(Page):
    def __init__(self, parent):
        print("Showning test page")


        # init page/ delete old page
        Page.__init__(self, parent)

        buttonEdit = {}
        buttondelete = {}
        menuData = Data.WorkerData.inventorydata

        container = Frame(self)
        canvas = tk.Canvas(container, height=500, width=500, bg='light gray')
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        UpdateMenuFrame = Frame(canvas, bg='light gray')

        UpdateMenuFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=UpdateMenuFrame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        Label(UpdateMenuFrame, text='Menu', font="bold", bg=def_fg).grid(column=0, row=0, padx=25, pady=20)
        Label(UpdateMenuFrame, text='Name', font="bold", bg=def_fg).grid(column=0, row=1, padx=10, pady=10)
        Label(UpdateMenuFrame, text='Quantity', font="bold", bg=def_fg).grid(column=1, row=1, padx=10, pady=10)
        Label(UpdateMenuFrame, text='price', font="bold", bg=def_fg).grid(column=2, row=1, padx=10, pady=10)
        count = 2

        def DeleteFood(id):
            print(menuData[id][0] + "deleted")
            menuData[id][0] = 'Null'
            UpdateFoodMenu(parent)

        def EditFood(id):
            print(menuData[id][0] + " edit")
            editfoodDetails = Tk()
            Label(editfoodDetails, text='Edit Food Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(editfoodDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(editfoodDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.insert(0, menuData[id][0])
            Label(editfoodDetails, text='Quantity :- ').grid(column=0, row=2, padx=25, pady=20)
            Qty = Entry(editfoodDetails, width=30)
            Qty.grid(column=1, row=2, padx=25, pady=20)
            Qty.insert(0, menuData[id][1])
            Label(editfoodDetails, text='price :- ').grid(column=0, row=3, padx=25, pady=20)
            price = Entry(editfoodDetails, width=30)
            price.grid(column=1, row=3, padx=25, pady=20)
            price.insert(0, menuData[id][2])

            def update():
                name = Name.get()
                menuData[id][0] = str(Name.get())
                menuData[id][1] = int(Qty.get())
                menuData[id][2] = int(price.get())
                print(name)
                editfoodDetails.destroy()
                UpdateFoodMenu(parent)

            Button(editfoodDetails, text="Save", width=50, command=lambda: update()).grid(column=0, row=4,
                                                                                          columnspan=2, pady=25)
            editfoodDetails.mainloop()

        def AddNewFoodPage():
            print("New Food")
            AddNewFoodDetails = Tk()
            Label(AddNewFoodDetails, text='New Food Details ', font="bold").grid(column=0, row=0, padx=25, pady=20)
            Label(AddNewFoodDetails, text='Name :- ').grid(column=0, row=1, padx=25, pady=20)
            Name = Entry(AddNewFoodDetails, width=30)
            Name.grid(column=1, row=1, padx=25, pady=20)
            Name.delete(0, END)
            Label(AddNewFoodDetails, text='Quantity :- ').grid(column=0, row=2, padx=25, pady=20)
            Qty = Entry(AddNewFoodDetails, width=30)
            Qty.grid(column=1, row=2, padx=25, pady=20)
            Qty.delete(0, END)
            Label(AddNewFoodDetails, text='price :- ').grid(column=0, row=3, padx=25, pady=20)
            price = Entry(AddNewFoodDetails, width=30)
            price.grid(column=1, row=3, padx=25, pady=20)
            price.delete(0, END)

            def update():
                name = Name.get()
                menuData.append([Name.get(), Qty.get(), price.get()])
                print(name)
                AddNewFoodDetails.destroy()
                UpdateFoodMenu(parent)

            Button(AddNewFoodDetails, width=50, text="Add New Food", command=lambda: update()).grid(column=0, row=4,
                                                                                                    pady=20,
                                                                                                    columnspan=2)
            AddNewFoodDetails.mainloop()

        for data in menuData:
            if (data[0] == "Null"):
                count += 1
                continue
            Label(UpdateMenuFrame, text=data[0], bg=def_fg).grid(column=0, row=count, padx=25, pady=20)
            Label(UpdateMenuFrame, text=data[1], bg=def_fg).grid(column=1, row=count, padx=25, pady=20)
            Label(UpdateMenuFrame, text=data[2], bg=def_fg
                  ).grid(column=2, row=count, padx=25, pady=20)

            def func(x=count - 2):
                return EditFood(x)

            buttonEdit[data[0]] = Button(UpdateMenuFrame, text='edit', command=func).grid(column=3, row=count, padx=25,
                                                                                          pady=20)

            def func(x=count - 2):
                return DeleteFood(x)

            buttondelete[data[0]] = Button(UpdateMenuFrame, text='delete', command=func).grid(column=4, row=count,
                                                                                              padx=25, pady=20)

            count += 1
        Button(UpdateMenuFrame, text="Add New Food", width=25, command=lambda: AddNewFoodPage()).grid(column=3,
                                                                                                      row=1,
                                                                                                      columnspan=2)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")