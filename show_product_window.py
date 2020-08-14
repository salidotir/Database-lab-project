from sqlalchemy import create_engine
from tkinter import *

def get_products_from_db():
    products=""

    engine = create_engine('mssql+pyodbc://MHL/fourthDB?driver=SQL Server?Trusted_Connection=yes')
    conn = engine.connect()
    result = engine.execute("select * from product")
    for row in result:
        products += str(row) + "\n"
    result.close()
    conn.close()

    return products


def create_product_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Products")

    main_label = Label(root, text='Products').place(x=220, y=50)
    tmp = "pid | pname | price \n" + get_products_from_db()
    products_label = Label(root, text=tmp).place(x=170, y=150)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # print(id)

    # show window
    root.geometry('510x350')
    root.mainloop()
