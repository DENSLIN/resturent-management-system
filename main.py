from TkinterSidebar.sidebar import *
from TkinterSidebar.pages.display_pages import *


#root.resizable(False, False)
#login = Login.login(root)

class main():

    def __init__(self):


        mainscreen = Tk()
        mainscreen.geometry("750x500")


        main_frame = Frame(mainscreen, bg="grey", width=1000, height=750)
        main_frame.place(x=200, y=0)

        def mainscreenOff():
            mainscreen.destroy()
        sidebar = SideBar(mainscreen)
        sidebar.add_spacer("Dashboard")
        sidebar.add_button("Home", lambda: HomePage(main_frame))
        sidebar.add_spacer("Menu")
        sidebar.add_button("update items", lambda: UpdateFoodMenu(main_frame))
        sidebar.add_spacer("Inventory")
        sidebar.add_button("Update inventory",lambda :ManageInventoryPage(main_frame))
        sidebar.add_spacer("Profile")
        sidebar.add_button("Update Manager", lambda: UpdateManagerPage(main_frame))
        sidebar.add_button("Update Worker", lambda: UpdateWorkerPage(main_frame))
        sidebar.add_spacer("settings")
        sidebar.add_button("info Settings", lambda: SettingsPage(main_frame))
        sidebar.add_button("apperaiince", lambda: HomePage(main_frame))
        sidebar.add_button("Log Out", lambda:mainscreenOff(), tab=False)

        sidebar.finish()

        mainscreen.mainloop()

