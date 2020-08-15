from tkinter import *
from ui.show_edit_product_window_tksheet import product_demo
from ui.show_edit_customer_window_tksheet import customer_demo
from ui.show_order_window_tksheet import oder_demo
import ui.new_product_window
import ui.new_customer_window

global id


def main():

    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Market Database")

    main_label = Label(root, text='Market Database').place(x=200, y=50)
    id_label = Label(root, text='order id: ').place(x=95, y=225)
    temp_id = StringVar()
    id_text_box = Entry(root, width=10, textvariable=temp_id).place(x=145, y=225)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_customer():
        ui.new_customer_window.create_new_customer_window()

    btn_new_order = Button(root, text="New customer", command=new_customer).place(x=105, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_order():
        pass

    btn_new_order = Button(root, text="New order", command=new_order).place(x=215, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_product():
        ui.new_product_window.create_new_product_window()

    btn_new_order = Button(root, text="New product", command=new_product).place(x=305, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_customers():
        app = customer_demo()
        app.mainloop()

    btn_show_customers = Button(root, text="Show customers", command=show_customers).place(x=100, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_orders():
        app = oder_demo()
        app.mainloop()

    btn_show_orders = Button(root, text="Show orders", command=show_orders).place(x=210, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_products():
        app = product_demo()
        app.mainloop()

    btn_show_products = Button(root, text="Show products", command=show_products).place(x=300, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def edit_order():
        # if temp_id.get() != "":
        #     id = int(temp_id.get())
        # else:
        #     id = -1
        # edit_order_window.id=id

        pass

    btn_edit_order = Button(root, text="Edit order", command=edit_order).place(x=215, y=220)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def exit():
        root.destroy()

    btn_exit = Button(root, text="Exit", command=exit).place(x=328, y=220)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # show window
    root.geometry('475x350')
    root.mainloop()


# call main function
main()
