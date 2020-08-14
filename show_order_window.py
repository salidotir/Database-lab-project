from sqlalchemy import create_engine
from tkinter import *

def get_orders_from_db():
    orders = ""

    engine = create_engine('mssql+pyodbc://MHL/fourthDB?driver=SQL Server?Trusted_Connection=yes')
    conn = engine.connect()
    result = engine.execute("select * from order1, order_item where order1.oid=order_item.oid")
    for row in result:
        orders += str(row) + "\n"
    result.close()
    conn.close()

    return orders


def create_order_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Orders")

    main_label = Label(root, text='Orders').place(x=225, y=50)
    tmp = "oid | time | cid | iid | pid | quantity \n" + get_orders_from_db()
    orders_label = Label(root, text=tmp).place(x=90, y=150)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # print(id)

    # show window
    root.geometry('510x350')
    root.mainloop()
