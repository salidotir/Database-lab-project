import datetime
from tkinter import *
from ui.show_edit_product_window_tksheet import product_demo
from ui.show_edit_customer_window_tksheet import customer_demo
from ui.show_order_window_tksheet import show_oder_demo
from ui.edit_order_window_tksheet import edit_oder_demo
import ui.new_product_window
import ui.new_customer_window
from Schema import CUSTOMER, ORDER1, db_session

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
        app.mainloop()

    btn_show_orders = Button(root, text="Show orders", command=show_orders).place(x=210, y=228)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    temp_order_id = StringVar()

    def edit_order():
        if len(temp_order_id.get()) > 1:
            oid = int(temp_order_id.get())
            app = edit_oder_demo(oid=oid)
            app.fill_data_from_db()
            app.mainloop()
        else:
            pass

    orders = ORDER1.query.all()
    osid = tuple([i.oid for i in orders]) if len(orders) > 0 else ("No order",)
    order_id_label = Label(root, text='order id: ').place(x=95, y=180)
    order_id_text_box = OptionMenu(root, temp_order_id, *osid).place(x=145, y=175)

    btn_edit_order = Button(root, text="Edit order", command=edit_order).place(x=215, y=178)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    temp_cid1 = StringVar()

    def new_order():
        if len(temp_cid1.get()) > 0:
            cid1 = int(temp_cid1.get())
            o = ORDER1(oDate=datetime.datetime.now(), cid=cid1)
            db_session.add(o)
            db_session.commit()
            root.destroy()
            main()
        else:
            pass

    cs = CUSTOMER.query.all()
    csid = tuple([i.cid for i in cs])
    cid1_label = Label(root, text='cust id: ').place(x=95, y=130)
    cid1_text_box = OptionMenu(root, temp_cid1, *csid).place(x=145, y=125)

    btn_new_order = Button(root, text="New order", command=new_order).place(x=215, y=128)

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