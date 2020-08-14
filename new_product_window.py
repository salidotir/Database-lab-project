from sqlalchemy import create_engine
from tkinter import *

def run_query_on_db():
    engine = create_engine('mssql+pyodbc://MHL/fourthDB?driver=SQL Server?Trusted_Connection=yes')
    conn = engine.connect()
    engine.execute("set identity_insert product on")
    result = engine.execute("insert into product(pid, pname, price) values('4', 'p4', '4000')")
    result.close()
    conn.close()
    
    print("Product inserted.")


def create_new_product_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("New product")

    main_label = Label(root, text='New product').place(x=220, y=50)

    pid_label = Label(root, text="pid").place(x=160, y=100)
    global pid
    pid = StringVar()
    pid_text_box = Entry(root, width=20, textvariable=pid).place(x=215, y=100)

    pname_label = Label(root, text="pname").place(x=160, y=130)
    global pname
    pname = StringVar()
    pname_text_box = Entry(root, width=20, textvariable=pname).place(x=215, y=130)

    price_label = Label(root, text="price").place(x=160, y=160)
    global price
    price = StringVar()
    price_text_box = Entry(root, width=20, textvariable=price).place(x=215, y=160)

    btn_add = Button(root, text="Add", command=run_query_on_db).place(x=240, y=200)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.


    # show window
    root.geometry('510x350')
    root.mainloop()
