from tksheet import Sheet
import tkinter as tk

global data
data = [["iid", "product id", "quantity"], [1, 1, 3], [2, 2, 2]]


class edit_oder_demo(tk.Tk):
    def __init__(self):
        # oid will be set in edit_order() function in crud_main_window.py to be called from fill_data_from_db()
        oid = -1

        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(self.frame,
                           page_up_down_select_row=True,
                           # empty_vertical = 0,
                           column_width=120,
                           startup_select=(0, 1, "rows"),
                           data=data,
                           height=500,  # height and width arguments are optional
                           width=550  # For full startup arguments see DOCUMENTATION.md
                           )

        self.sheet.enable_bindings(("single_select",  # "single_select" or "toggle_select"
                                    "drag_select",  # enables shift click selection as well
                                    "column_drag_and_drop",
                                    "row_drag_and_drop",
                                    "column_select",
                                    "row_select",
                                    "column_width_resize",
                                    "double_click_column_resize",
                                    # "row_width_resize",
                                    # "column_height_resize",
                                    "arrowkeys",
                                    "row_height_resize",
                                    "double_click_row_resize",
                                    "right_click_popup_menu",
                                    "rc_select",
                                    # "rc_insert_column",
                                    # "rc_delete_column",
                                    # "rc_insert_row",
                                    "rc_delete_row",
                                    # "hide_columns",
                                    "copy",
                                    # "cut",
                                    # "paste",
                                    # "delete",
                                    "undo",
                                    "edit_cell"))

        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")

        # __________ DISPLAY SUBSET OF COLUMNS __________

        self.sheet.display_subset_of_columns(indexes=[0, 1, 2], enable=True)

        # __________ BINDING A FUNCTIONS TO USER ACTIONS __________

        self.sheet.extra_bindings([("end_edit_cell", self.end_edit_cell),
                                   ("rc_delete_row", self.row_delete)
                                   ])

        # __________ GETTING FULL SHEET DATA __________

        # self.all_data = self.sheet.get_sheet_data()

        # __________ GETTING CELL DATA __________

        # print (self.sheet.get_cell_data(0, 0))

        # __________ GETTING ROW DATA __________

        # print (self.sheet.get_row_data(0)) # only accessible by index

        # __________ GETTING COLUMN DATA __________

        # print (self.sheet.get_column_data(0)) # only accessible by index

    def end_edit_cell(self, event):
        print("cell edited")
        print(event)
        #
        # To Be Completed
        #

    def row_delete(self, event):
        print("row deleted")
        print(event)
        #
        # To Be Completed
        #

    def fill_data_from_db(self):
        # get data from database
        #
        # To Be Completed
        #

        print(self.oid)
        pass


# app = oder_demo()
# app.mainloop()
