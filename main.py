from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from click import command
from student import Student
from train import Train
from Face_reco import FaceRecognition
from attendance import Attendance
from about import About
from help import Help
import os


class FaceRecognitionSystem:

    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        
        self.root.title("Face Recognition System")

        # ---------- First Image ----------
        img1 = Image.open(r"images/img1.png")
        img1 = img1.resize((470, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=470, height=130)

        # ---------- Second Image ----------
        img2 = Image.open(r"images/img6.png")
        img2 = img2.resize((470, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=470, y=0, width=470, height=130)

        # ---------- Third Image ----------
        img3 = Image.open(r"images/img2.png")
        img3 = img3.resize((470, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=940, y=0, width=470, height=130)

        # ---------- Background Image ----------
        bgimg = Image.open(r"images/bg.png")
        bgimg = bgimg.resize((1530, 710), Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bgimg)

        bg_lbl = Label(self.root, image=self.photobg)
        bg_lbl.place(x=0, y=130, width=1530, height=710)

        # ---------- Title ----------
        title_lbl = Label(
            bg_lbl,
            text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkblue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ---------- Student Button ----------
        std_img_btn = Image.open(r"images/stud.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.student_photo = ImageTk.PhotoImage(std_img_btn)

        std_btn = Button(bg_lbl, image=self.student_photo, cursor="hand2",command=self.open_student_details)
        std_btn.place(x=200, y=100, width=180, height=180)

        button1 = Button(bg_lbl, text="Student Details",command=self.open_student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        button1.place(x=200, y=280, width=180, height=40)
        
        # --------- Face Detection Button ----------
        face_img_btn = Image.open(r"images/detect.jpg")
        face_img_btn = face_img_btn.resize((180, 180), Image.LANCZOS)
        self.face_photo = ImageTk.PhotoImage(face_img_btn)

        face_btn = Button(bg_lbl, image=self.face_photo, cursor="hand2",command=self.open_face)
        face_btn.place(x=450, y=100, width=180, height=180)

        button2 = Button(bg_lbl, text="Face Detection", cursor="hand2", command=self.open_face,font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        button2.place(x=450, y=280, width=180, height=40)
        
        # --------- Attendance Button ----------
        att_img_btn = Image.open(r"images/attendance.webp")
        att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
        self.attendance_photo = ImageTk.PhotoImage(att_img_btn)

        att_btn = Button(bg_lbl, image=self.attendance_photo, command=self.open_attn,cursor="hand2")
        att_btn.place(x=700, y=100, width=180, height=180)

        button3 = Button(bg_lbl, text="Attendance", cursor="hand2",command=self.open_attn, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        button3.place(x=700, y=280, width=180, height=40)

    #    ---------- Help Button ----------
        help_img_btn = Image.open(r"images/helpdesk.jpg")
        help_img_btn = help_img_btn.resize((180, 180), Image.LANCZOS)
        self.help_photo = ImageTk.PhotoImage(help_img_btn)

        help_btn = Button(bg_lbl, image=self.help_photo, cursor="hand2",command=self.open_help)
        help_btn.place(x=950, y=100, width=180, height=180)

        button4 = Button(bg_lbl, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="green",command=self.open_help, fg="white")
        button4.place(x=950, y=280, width=180, height=40)
        
    #  ---------- Train Button ----------
        train_img_btn = Image.open(r"images/train.jpg")
        train_img_btn = train_img_btn.resize((180, 180), Image.LANCZOS)
        self.train_photo = ImageTk.PhotoImage(train_img_btn)

        train_btn = Button(bg_lbl, image=self.train_photo, cursor="hand2",command=self.open_train)
        train_btn.place(x=200, y=325, width=180, height=180)

        button5 = Button(bg_lbl, text="Train Data", cursor="hand2"  ,command=self.open_train, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        button5.place(x=200, y=505, width=180, height=40)
        
        # --------- Photos Button ----------
        photo_img_btn = Image.open(r"images/pics.jpg")
        photo_img_btn = photo_img_btn.resize((180, 180), Image.LANCZOS)
        self.photo_photo = ImageTk.PhotoImage(photo_img_btn)

        photo_btn = Button(bg_lbl, image=self.photo_photo, cursor="hand2",command=self.open_img)
        photo_btn.place(x=450, y=325, width=180, height=180)

        button6 = Button(bg_lbl, text="Photos", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        button6.place(x=450, y=505, width=180, height=40)

    #   -----------About Button ----------
        about_img_btn = Image.open(r"images/about.jpg")
        about_img_btn = about_img_btn.resize((180, 180), Image.LANCZOS)
        self.about_photo = ImageTk.PhotoImage(about_img_btn)

        about_btn = Button(bg_lbl, image=self.about_photo, cursor="hand2", command=self.open_about)
        about_btn.place(x=700, y=325, width=180, height=180)

        button8 = Button(bg_lbl, text="About", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", command=self.open_about, fg="white")
        button8.place(x=700, y=505, width=180, height=40)



    #   ---------- Exit Button ----------
        exit_img_btn = Image.open(r"images/exitbu.jpg")
        exit_img_btn = exit_img_btn.resize((180, 180), Image.LANCZOS)
        self.exit_photo = ImageTk.PhotoImage(exit_img_btn)

        exit_btn = Button(bg_lbl, image=self.exit_photo,  command=self.iExit,cursor="hand2")
        exit_btn.place(x=950, y=325, width=180, height=180)

        button7 = Button(bg_lbl, text="Exit", cursor="hand2", command=self.iExit, font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        button7.place(x=950, y=505, width=180, height=40)

    
    def open_img(self):
        os.startfile("data")  # Open the "data" folder in the file explorer


# ========================  Function Buttons ==========================
    def open_student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

# =============train def================


    def open_train(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)

# ==================face recognisition===============
    def open_face(self):
       self.new_window = Toplevel(self.root)
       self.app = FaceRecognition(self.new_window)
 
# ==================attendance ===============
    def open_attn(self):
       self.new_window = Toplevel(self.root)
       self.app = Attendance(self.new_window)
 
  
# ==================about ===============
    def open_about(self):
       self.new_window = Toplevel(self.root)
       self.app = About(self.new_window)
 

  
# =================help ===============
    def open_help(self):
       self.new_window = Toplevel(self.root)
       self.app = Help(self.new_window)
 
    # ================= EXIT FUNCTION =================

    def iExit(self):

        iExit = messagebox.askyesno(
            "Face Recognition System",
            "Are you sure you want to exit?"
        )

        if iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()