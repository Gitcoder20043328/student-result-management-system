from tkinter import *

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x480+80+170")
        self.root.config(bg="aqua")
        self.root.focus_force()

# title ----
        title=Label(self.root, text="manage course details",font=("goudy old style", 20, "bold"), bg="#033054", fg="white")

        # widget=====
        lbl_course_name=Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="aqua", fg="black")
        lbl_course_name.place(x=10, y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style", 15, "bold"), bg="aqua", fg="black")
        lbl_duration.place(x=10, y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style", 15, "bold"), bg="aqua", fg="black")
        lbl_charges.place(x=10, y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style", 15, "bold"), bg="aqua", fg="black")
        lbl_description.place(x=10, y=180)


        txt_course_name=Entry(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        txt_course_name.place(x=150, y=60) 
        txt_duration=Entry(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        txt_duration.place(x=150, y=100)    
        txt_charges=Entry(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        txt_charges.place(x=150, y=140)
        txt_description=Entry(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        txt_description.place(x=150, y=180)     

        


if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()



