from tksheet import Sheet
import tkinter as tk
from Schema import db_session, PRODUCT

global data
headers = ["pid",
           "pName",
           "price"]
data = []


class product_demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.fill_data_from_db()
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(self.frame,
                           page_up_down_select_row=True,
                           # empty_vertical = 0,
                           headers=headers,
                           column_width=120,
                           startup_select=(0, 1, "rows"),
                           data=data,
                           height=500,  # height and width arguments are optional
                           width=500  # For full startup arguments see DOCUMENTATION.md
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
                                   ("begin_rc_delete_row", self.row_delete)
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
        PRODUCT.query.filter_by(
            **{"pid": self.sheet.get_cell_data(
                event[0],
                0
            )}
        ).update(
            {headers[event[1]]: self.sheet.get_cell_data(
                event[0],
                event[1]
            )}
        )
        db_session.commit()

    def row_delete(self, event):
        print("row deleted")
        print(event)
        print({"pid": self.sheet.get_cell_data(
            event[1][0],
            0
        )})
        PRODUCT.query.filter_by(
            **{"pid": self.sheet.get_cell_data(
                event[1][0],
                0
            )}
        ).delete()
        db_session.commit()

    def fill_data_from_db(self):
        data.clear()
        ps = PRODUCT.query.all()
        k = [[i.to_dict(rules=('-ORDERITEM',)).get(z) for z in headers] for i in ps]
        data.extend(k)


# app = product_demo()
# app.mainloop()
