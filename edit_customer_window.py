from sqlalchemy import create_engine
from tkinter import *

global edited_id


def run_query_on_db():
    # engine = create_engine('mssql+pyodbc://MHL/fourthDB?driver=SQL Server?Trusted_Connection=yes')
    # conn = engine.connect()
    # engine.execute("set identity_insert customer on")
    # result = engine.execute("insert into customer(cid, cname, ctype) values(4, 'cust4', 2)")
    # result.close()
    # conn.close()

    # print(int(ctype.get()))
    print("Customer inserted.")


def create_edit_customer_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Edit customer")

    main_label = Label(root, text='Edit customer').place(x=220, y=50)

    cname_label = Label(root, text="cname").place(x=170, y=100)
    global cname
    cname = StringVar()
    cname_text_box = Entry(root, width=20, textvariable=cname).place(x=215, y=100)

    ctype_label = Label(root, text="ctype").place(x=170, y=130)
    global ctype
    ctype = StringVar(root, "1")
    values = {"Shakhsi": "1",
              "Sherkati": "2"}
    # for (text, value) in values.items():
    Radiobutton(root, text="Shakhsi", variable=ctype, value="1").place(x=215, y=130)
    Radiobutton(root, text="Sherkati", variable=ctype, value="2").place(x=290, y=130)

    btn_add = Button(root, text="Add", command=run_query_on_db).place(x=240, y=160)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # show window
    root.geometry('510x350')
    root.mainloop()
