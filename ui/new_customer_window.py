from Schema import CUSTOMER, db_session
from tkinter import *


def run_query_on_db():
    # print(int(ctype.get()))
    print("Customer inserted.")

    #
    # To Be Completed
    #


def create_new_customer_window():
    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("New customer")

    main_label = Label(master=root, text='New customer').place(x=220, y=50)

    maxCredit_label = Label(root, text="maxCredit").place(x=150, y=100)
    maxCredit = StringVar(master=root)
    maxCredit_text_box = Entry(root, width=20, textvariable=maxCredit).place(x=215, y=100)

    cname_label = Label(root, text="cname").place(x=170, y=130)
    cname = StringVar(master=root)
    cname_text_box = Entry(root, width=20, textvariable=cname).place(x=215, y=130)

    ctype_label = Label(root, text="ctype").place(x=170, y=160)
    ctype = StringVar(master=root, value="0")
    values = {"Shakhsi": "0",
              "Sherkati": "1"}
    # for (text, value) in values.items():
    Radiobutton(root, text="Shakhsi", variable=ctype, value="0").place(x=215, y=160)
    Radiobutton(root, text="Sherkati", variable=ctype, value="1").place(x=290, y=160)

    btn_add = Button(root, text="Add", command=lambda: run_query_on_db(
        cName=cname.get(),
        customerType=ctype.get(),
        maxCredit=maxCredit.get()
    )).place(x=240, y=200)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # show window
    root.geometry('510x350')
    root.mainloop()
