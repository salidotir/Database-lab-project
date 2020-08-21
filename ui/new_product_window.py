from Schema import PRODUCT, db_session
from tkinter import *


def run_query_on_db(**kwargs):
    p = PRODUCT(**kwargs)
    db_session.add(p)
    db_session.commit()
    print("Product inserted.")


def create_new_product_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("New product")

    main_label = Label(root, text='New product').place(x=220, y=50)

    pname_label = Label(root, text="pName").place(x=160, y=100)
    pname = StringVar(master=root)
    pname_text_box = Entry(root, width=20, textvariable=pname).place(x=215, y=100)

    price_label = Label(root, text="price").place(x=160, y=130)
    p_price = StringVar(master=root)
    price_text_box = Entry(root, width=20, textvariable=p_price).place(x=215, y=130)

    btn_add = Button(root, text="Add", command=lambda: run_query_on_db(
        pName=pname.get(),
        price=p_price.get()
    )).place(x=240, y=160)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.


    # show window
    root.geometry('510x350')
    root.mainloop()
