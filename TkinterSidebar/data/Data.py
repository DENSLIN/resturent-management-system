# cur.execute("""CREATE TABLE worker(
#                     Name text,
#                     age integer,
#                     contact integer,
#                     shift text,
#                     password text,
#                     Money integer)""")
#     cur.execute("""CREATE TABLE manager(
#                     Name text,
#                     age integer,
#                     contact integer,
#                     shift text,
#                     password text)""")
#     cur.execute("""CREATE TABLE inv_items(
#                     Name text,
#                     Quantity integer,
#                     ptpp integer,
#                     low integer,
#                     price integer)""")
#     cur.execute("""CREATE TABLE food_items(
#                     Name text,
#                     ingredients text,
#                     price integer)""")

class WorkerData ():
    workerData = [["name1", '******', '200'],
                  ['name 2', '******', '200'],
                  ['name 3', '******', '200'],
                  ['name 4', '******', '200']]
    ManagerData = [["Manager 1", '******', '200'],
                  ['Manager 2', '******', '200'],
                  ['Manager 3', '******', '200'],
                  ['Manager 4', '******', '200']]
    menuData=[["pizza",1,200],
              ["Burger",1,200],
              ["franki",1,80],
              ["tea",1,20],
              ["coffee",1,25],
              ["pizza", 1, 200],
              ["Burger", 1, 200],
              ["franki", 1, 80],
              ["pizza", 1, 200],
              ["Burger", 1, 200],
              ["franki", 1, 80],
              ["tea", 1, 20]
              ]
    inventorydata=[["tomato",4,100],
                   ["potato",4,100],
                   ["onion",4,100],
                   ["",4,100],
                   ["tomato",4,100],
                   ["tomato",4,100],
                   ["tomato",4,100],
                   ["tomato",4,100],
                   ]

    def __init__(self):
        self.workerData1 = [['name 1', '******', '200'],
                            ['name 1', '******', '200'],
                            ['name 1', '******', '200'],
                            ['name 1', '******', '200']]

    def anlist(self):
        return self.workerData1
"""class Login ():
    def __init__(self):

"""
