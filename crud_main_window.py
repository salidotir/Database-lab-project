from tkinter import *
from ui.show_edit_product_window_tksheet import product_demo
from ui.show_edit_customer_window_tksheet import customer_demo
from ui.show_order_window_tksheet import show_oder_demo
from ui.edit_order_window_tksheet import edit_oder_demo
import ui.new_product_window
import ui.new_customer_window

global id


def main():

    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Market Database")

    main_label = Label(root, text='Market Database').place(x=200, y=50)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_product():
        ui.new_product_window.create_new_product_window()

    btn_new_order = Button(root, text="New product", command=new_product).place(x=305, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_products():
        app = product_demo()
        app.fill_data_from_db()
        app.mainloop()

    btn_show_products = Button(root, text="Show products", command=show_products).place(x=300, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_customer():
        ui.new_customer_window.create_new_customer_window()

    btn_new_order = Button(root, text="New customer", command=new_customer).place(x=300, y=220)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_customers():
        app = customer_demo()
        app.mainloop()

    btn_show_customers = Button(root, text="Show customers", command=show_customers).place(x=296, y=270)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_orders():
        app = show_oder_demo()
        app.fill_data_from_db()
        app.mainloop()

    btn_show_orders = Button(root, text="Show orders", command=show_orders).place(x=210, y=270)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    temp_order_id = StringVar()

    def edit_order():
        if temp_order_id.get() != "":
            app = edit_oder_demo()
            app.oid = int(temp_order_id.get())
            app.fill_data_from_db()
            app.mainloop()
        else:
            pass

    order_id_label = Label(root, text='order id: ').place(x=95, y=225)
    order_id_text_box = Entry(root, width=10, textvariable=temp_order_id).place(x=145, y=225)

    btn_edit_order = Button(root, text="Edit order", command=edit_order).place(x=215, y=220)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    temp_cid1 = StringVar()

    def new_order():
        if temp_cid1.get() != "":
            cid1 = int(temp_cid1.get())
            # add a new order to tale order with current date, identity oid and cid
            #
            # To Be Completed
            #
        else:
            pass

    cid1_label = Label(root, text='cust id: ').place(x=95, y=125)
    cid1_text_box = Entry(root, width=10, textvariable=temp_cid1).place(x=145, y=125)

    btn_new_order = Button(root, text="New order", command=new_order).place(x=215, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    temp_cid2 = StringVar()

    def show_order_total():
        if temp_cid2.get() != "":
            cid2 = int(temp_cid2.get())
            # show order total of current cid
            #
            # To Be Completed
            #
        else:
            pass

    cid2_label = Label(root, text='cust id: ').place(x=95, y=175)
    cid2_text_box = Entry(root, width=10, textvariable=temp_cid2).place(x=145, y=175)

    btn_new_order = Button(root, text="Order total", command=show_order_total).place(x=215, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def exit():
        root.destroy()

    btn_exit = Button(root, text="Exit", command=exit).place(x=145, y=270)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # show window
    root.geometry('475x350')
    root.mainloop()


# call main function
main()
