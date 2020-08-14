from tkinter import *
import show_product_window
import show_customer_window
import show_order_window
import new_product_window
import new_customer_window
import edit_customer_window
import edit_product_window

global id

def main():

    # initialize tkinter
    root = Tk()

    # set window title
    root.wm_title("Market Database")

    main_label = Label(root, text='Market Database').place(x=200, y=50)
    id_label = Label(root, text='id: ').place(x=200, y=90)
    temp_id = StringVar()
    id_text_box = Entry(root, width=10, textvariable=temp_id).place(x=230, y=90)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_customer():
        new_customer_window.create_new_customer_window()

    btn_new_order = Button(root, text="New customer", command=new_customer).place(x=105, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_order():
        pass

    btn_new_order = Button(root, text="New order", command=new_order).place(x=215, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def new_product():
        new_product_window.create_new_product_window()

    btn_new_order = Button(root, text="New product", command=new_product).place(x=305, y=120)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_customers():
        show_customer_window.create_customer_window()

    btn_show_customers = Button(root, text="Show customers", command=show_customers).place(x=100, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_orders():
        show_order_window.create_order_window()

    btn_show_orders = Button(root, text="Show orders", command=show_orders).place(x=210, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def show_products():
        # if temp_id.get() != "":
        #     id = int(temp_id.get())
        # else:
        #     id = -1
        # product_window.id=id

        show_product_window.create_product_window()

    btn_show_products = Button(root, text="Show products", command=show_products).place(x=300, y=170)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def edit_customers():
        if temp_id.get() != "":
            id = int(temp_id.get())
            edit_customer_window.edited_id = id
            edit_customer_window.create_edit_customer_window()
        else:
            id = -1
            print("You must fill id text box to edit customer!")

    btn_edit_customers = Button(root, text="Edit customers", command=edit_customers).place(x=105, y=220)

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

    def edit_products():
        if temp_id.get() != "":
            id = int(temp_id.get())
            edit_product_window.edited_id = id
            edit_product_window.create_edit_product_window()
        else:
            id = -1
            print("You must fill id text box to edit product!")

    btn_edit_products = Button(root, text="Edit products", command=edit_products).place(x=305, y=220)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    def exit():
        root.destroy()

    btn_exit = Button(root, text="Exit", command=exit).place(x=230, y=270)

    # ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

    # show window
    root.geometry('475x350')
    root.mainloop()


# call main function
main()
