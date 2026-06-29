from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
import re
from main import FaceRecognitionSystem


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Login System")
        self.root.state("zoomed")
        self.root.config(bg="#021e2f")

        # ================= BACKGROUND IMAGE =================
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ================= MAIN FRAME =================
        self.login_frame = Frame(self.root, bg="white", bd=0)
        self.login_frame.place(x=540, y=140, width=400, height=520)

        # ================= TITLE =================
        title = Label(
            self.login_frame,
            text="LOGIN",
            font=("Montserrat", 28, "bold"),
            bg="white",
            fg="#0A66C2"
        )
        title.place(x=130, y=20)

        subtitle = Label(
            self.login_frame,
            text="Welcome Back",
            font=("Montserrat", 14),
            bg="white",
            fg="gray"
        )
        subtitle.place(x=125, y=70)

        # ================= USER IMAGE =================
        self.user_img = Image.open("images/user.jpg")
        self.user_img = self.user_img.resize((25, 25), Image.Resampling.LANCZOS)
        self.user_photo = ImageTk.PhotoImage(self.user_img)

        user_icon = Label(self.login_frame, image=self.user_photo, bg="white")
        user_icon.place(x=40, y=150)

        # ================= USERNAME =================
        username_lbl = Label(
            self.login_frame,
            text="Email",
            font=("Montserrat", 13, "bold"),
            bg="white",
            fg="#333333"
        )
        username_lbl.place(x=80, y=120)

        self.txtuser = ttk.Entry(
            self.login_frame,
            font=("Montserrat", 14)
        )
        self.txtuser.place(x=80, y=150, width=260, height=35)

        # ================= PASSWORD IMAGE =================
        self.pass_img = Image.open("images/password.png")
        self.pass_img = self.pass_img.resize((25, 25), Image.Resampling.LANCZOS)
        self.pass_photo = ImageTk.PhotoImage(self.pass_img)

        pass_icon = Label(self.login_frame, image=self.pass_photo, bg="white")
        pass_icon.place(x=40, y=250)

        # ================= PASSWORD =================
        password_lbl = Label(
            self.login_frame,
            text="Password",
            font=("Montserrat", 13, "bold"),
            bg="white",
            fg="#333333"
        )
        password_lbl.place(x=80, y=220)

        self.txtpass = ttk.Entry(
            self.login_frame,
            show="*",
            font=("Montserrat", 14)
        )
        self.txtpass.place(x=80, y=250, width=260, height=35)

        # ================= SHOW PASSWORD =================
        self.show_var = IntVar()

        show_pass = Checkbutton(
            self.login_frame,
            text="Show Password",
            variable=self.show_var,
            command=self.show_password,
            bg="white",
            font=("Montserrat", 10)
        )
        show_pass.place(x=80, y=295)

        # ================= LOGIN BUTTON =================
        login_btn = Button(
            self.login_frame,
            text="LOGIN",
            command=self.login,
            font=("Montserrat", 15, "bold"),
            bg="#0A66C2",
            fg="white",
            cursor="hand2",
            bd=0,
            activebackground="#004182",
            activeforeground="white"
        )
        login_btn.place(x=80, y=350, width=260, height=45)

        # ================= REGISTER BUTTON =================
        register_btn = Button(
            self.login_frame,
            text="Create New Account",
            command=self.register_window,
            font=("Montserrat", 11, "bold"),
            bg="white",
            fg="#0A66C2",
            bd=0,
            cursor="hand2"
        )
        register_btn.place(x=110, y=420)

        # ================= FORGOT PASSWORD =================
        forgot_btn = Button(
            self.login_frame,
            text="Forgot Password?",
            font=("Montserrat", 10),
            bg="white",
            fg="red",
            bd=0,
            cursor="hand2"
        )
        forgot_btn.place(x=135, y=460)

    # ================= DATABASE CONNECTION =================
    def db_connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="arpita@1845",
            database="face_recognizer"
        )
    
    # ==========validate email===============
    def validate_email(self, email):

        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

        if re.match(pattern, email):
            return True
        else:
            return False
    # ================= SHOW PASSWORD =================
    def show_password(self):
        if self.show_var.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ================= LOGIN FUNCTION =================
    def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
            return

        if not self.validate_email(self.txtuser.get()):
            messagebox.showerror(
                "Error",
                "Please Enter Valid Gmail Address"
            )
            return

        try:
            conn = self.db_connect()
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE email=%s AND password=%s"

            value = (
                self.txtuser.get(),
                self.txtpass.get()
            )

            cursor.execute(query, value)

            row = cursor.fetchone()

            if row is None:
                messagebox.showerror(
                    "Error",
                    "Invalid Email or Password"
                )

            else:
                messagebox.showinfo(
                    "Success",
                    f"Welcome{self.txtuser.get()}"
                )

                self.root.destroy()
                new_root = Tk()
                app = FaceRecognitionSystem(new_root)
                new_root.mainloop()

            conn.close()

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Database Error : {str(es)}"
            )
            
    # ================= REGISTER WINDOW =================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


# ================= REGISTER CLASS =================
class Register:
    def __init__(self, root):

        self.root = root
        self.root.title("Register")
        self.root.geometry("500x580+500+100")
        self.root.config(bg="white")

        title = Label(
            self.root,
            text="REGISTER",
            font=("Montserrat", 25, "bold"),
            bg="white",
            fg="#0A66C2"
        )
        title.pack(pady=20)

        # ================= NAME =================
        Label(
            self.root,
            text="Full Name",
            font=("Montserrat", 13, "bold"),
            bg="white"
        ).place(x=50, y=100)

        self.name = ttk.Entry(self.root, font=("Montserrat", 13))
        self.name.place(x=50, y=130, width=380)

        # ================= EMAIL =================
        Label(
            self.root,
            text="Email",
            font=("Montserrat", 13, "bold"),
            bg="white"
        ).place(x=50, y=190)

        self.email = ttk.Entry(self.root, font=("Montserrat", 13))
        self.email.place(x=50, y=220, width=380)
        
        
        
        # ================= PASSWORD =================
        Label(
            self.root,
            text="Password",
            font=("Montserrat", 13, "bold"),
            bg="white"
        ).place(x=50, y=280)

        self.password = ttk.Entry(
            self.root,
            show="*",
            font=("Montserrat", 13)
        )
        self.password.place(x=50, y=310, width=380)
        
       

        # ================= REGISTER BUTTON =================
        reg_btn = Button(
            self.root,
            text="REGISTER",
            command=self.register_data,
            font=("Montserrat", 15, "bold"),
            bg="#0A66C2",
            fg="white",
            bd=0,
            cursor="hand2"
        )
        reg_btn.place(x=120, y=400, width=250, height=45)
    
    # ================= DATABASE CONNECTION =================
    def db_connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="arpita@1845",
            database="face_recognizer"
        )
    
    def validate_email(self, email):

        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

        if re.match(pattern, email):
            return True
        else:
            return False
        
    # ================= REGISTER DATA =================
    def register_data(self):

        if self.name.get() == "" or self.email.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
            return

        if not self.validate_email(self.email.get()):
            messagebox.showerror(
                "Error",
                "Please Enter Valid Gmail Address"
            )
            return

        if len(self.password.get()) < 6:
            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters"
            )
            return

        try:
            conn = self.db_connect()
            cursor = conn.cursor()

            # CHECK DUPLICATE EMAIL
            cursor.execute(
                "SELECT * FROM users WHERE email=%s",
                (self.email.get(),)
            )

            row = cursor.fetchone()

            if row:
                messagebox.showerror(
                    "Error",
                    "Email already exists"
                )
                conn.close()
                return

            query = """
            INSERT INTO users(name,email,password)
            VALUES(%s,%s,%s)
            """

            value = (
                self.name.get(),
                self.email.get(),
                self.password.get()
            )

            cursor.execute(query, value)

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Registration Successful"
            )

            self.root.destroy()

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Database Error : {str(es)}"
            )



# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()