from tkinter import *
from tkinter import ttk

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x480+80+170")
        self.root.config(bg="aqua")
        self.root.focus_force()

        # title ----
        title = Label(self.root, text="manage course details",
                      font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # widget=====
        lbl_course_name = Label(self.root, text="Course Name",
                                font=("goudy old style", 15, "bold"),
                                bg="aqua", fg="black")
        lbl_course_name.place(x=10, y=60)

        lbl_duration = Label(self.root, text="Duration",
                             font=("goudy old style", 15, "bold"),
                             bg="aqua", fg="black")
        lbl_duration.place(x=10, y=100)

        lbl_charges = Label(self.root, text="Charges",
                            font=("goudy old style", 15, "bold"),
                            bg="aqua", fg="black")
        lbl_charges.place(x=10, y=140)

        lbl_description = Label(self.root, text="Description",
                                font=("goudy old style", 15, "bold"),
                                bg="aqua", fg="black")
        lbl_description.place(x=10, y=180)

        txt_course_name = Entry(self.root, font=("goudy old style", 15, "bold"),
                                bg="lightyellow", fg="black")
        txt_course_name.place(x=150, y=60)

        txt_duration = Entry(self.root, font=("goudy old style", 15, "bold"),
                              bg="lightyellow", fg="black")
        txt_duration.place(x=150, y=100)

        txt_charges = Entry(self.root, font=("goudy old style", 15, "bold"),
                             bg="lightyellow", fg="black")
        txt_charges.place(x=150, y=140)

        txt_description = Entry(self.root, font=("goudy old style", 15, "bold"),
                                bg="lightyellow", fg="black")
        txt_description.place(x=150, y=180)

        #----buttons----
        self.btn_add = Button(self.root, text="Save",
                              font=("goudy old style", 15, "bold"),
                              bg="#21c372", fg="white", cursor="hand2")
        self.btn_add.place(x=150, y=220, width=110, height=40)

        self.btn_update = Button(self.root, text="Update",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#167707", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=220, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#c32121", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=220, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear",
                                font=("goudy old style", 15, "bold"),
                                bg="#c32121", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=220, width=110, height=40)

        # search panel
        self.panel_search = LabelFrame(self.root, text="Search Course",
                                       font=("goudy old style", 15, "bold"),
                                       bg="aqua", fg="black")
        self.panel_search.place(x=700, y=60, width=550, height=100)

        lbl_search_course = Label(self.panel_search, text="Course Name",
                                  font=("goudy old style", 15, "bold"),
                                  bg="aqua", fg="black")
        lbl_search_course.place(x=10, y=10)

        txt_search_course = Entry(self.panel_search,
                                  font=("goudy old style", 15, "bold"),
                                  bg="lightyellow", fg="black")
        txt_search_course.place(x=150, y=10)

        btn_search = Button(self.root, text="Search",
                             font=("goudy old style", 15, "bold"),
                             bg="#21c372", fg="white", cursor="hand2")
        btn_search.place(x=870, y=170, width=110, height=40)

        # contents
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x=700, y=170, width=550, height=300)

        # scrollbars
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)

        # table
        self.coursetable = ttk.Treeview(
            self.C_frame,
            columns=("cid", "name", "duration", "charges", "description"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)

        self.coursetable.pack(fill=BOTH, expand=1)

        self.coursetable.heading("cid", text="Course ID")
        self.coursetable.heading("name", text="Name")
        self.coursetable.heading("duration", text="Duration")
        self.coursetable.heading("charges", text="Charges")
        self.coursetable.heading("description", text="Description")

        self.coursetable["show"] = "headings"

        self.coursetable.column("cid", width=100)
        self.coursetable.column("name", width=100)
        self.coursetable.column("duration", width=100)
        self.coursetable.column("charges", width=100)
        self.coursetable.column("description", width=150)


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()