from tkinter import *
from course import CourseClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")

        # ---------- Title ----------
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            font=("goudy old style", 20, "italic"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # ---------- MENU ----------
        M_frame = LabelFrame(self.root, text="Menus",
                             font=("times new roman", 15),
                             bg="black")
        M_frame.place(x=10, y=70, width=1340, height=80)

        Button(M_frame, text="Course", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white",command=self.add_course).place(x=20, y=5, width=200, height=40)

        Button(M_frame, text="Students", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white").place(x=240, y=5, width=200, height=40)

        Button(M_frame, text="Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white").place(x=460, y=5, width=200, height=40)

        Button(M_frame, text="View", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white").place(x=680, y=5, width=200, height=40)

        Button(M_frame, text="Logout", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white").place(x=900, y=5, width=200, height=40)

        Button(M_frame, text="Exit", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", command=self.root.destroy)\
               .place(x=1120, y=5, width=200, height=40)

        # ---- TEXT BACKGROUND (instead of image) ----
        self.lbl_bg = Label(
            self.root,
            text="Welcome to Student Result Management System",
            font=("goudy old style", 25, "bold"),
            bg="black",
            fg="white"
        )
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        # ---- Dashboard ----
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]",
                                font=("goudy old style", 20),
                                bd=10, relief=RIDGE,
                                bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]",
                                font=("goudy old style", 20),
                                bd=10, relief=RIDGE,
                                bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]",
                               font=("goudy old style", 20),
                               bd=10, relief=RIDGE,
                               bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # -------- FOOTER ----------
        footer = Label(self.root,
                       text="Student Result Management System\nContact us for feedback",
                       font=("goudy old style", 12),
                       bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

# -------- RUN APP --------
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()