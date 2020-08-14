from sqlalchemy import create_engine
from tkinter import *

def get_customers_from_db():
    customers=""

    engine = create_engine('mssql+pyodbc://MHL/fourthDB?driver=SQL Server?Trusted_Connection=yes')
    conn = engine.connect()
    result = engine.execute("select * from customer")
    for row in result:
        customers += str(row) + "\n"
    result.close()
    conn.close()

    return customers


def create_customer_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Customers")

    main_label = Label(root, text='Customers').place(x=225, y=50)
    tmp = "cid | cname | ctype \n" + get_customers_from_db()
    customers_label = Label(root, text=tmp).place(x=200, y=150)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # print(id)

    # show window
    root.geometry('510x350')
    root.mainloop()
