from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from matplotlib.pyplot import fill
import mysql.connector 
# import face_recognition
import dlib
import cv2
import os
import numpy as np
from datetime import datetime
from time import strftime


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
       
        self.root.state("zoomed")
       
    #    ============variables=================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_dob = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_photo_sample = StringVar()
         
        # ---------- First Image ----------
        img1 = Image.open(r"images/img7.png")
        img1 = img1.resize((470, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=470, height=130)

        # ---------- Second Image ----------
        img2 = Image.open(r"images/img10.png")
        img2 = img2.resize((470, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=470, y=0, width=470, height=130)

        # ---------- Third Image ----------
        img3 = Image.open(r"images/img9.png")
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
            text="STUDENT ATTENDANCE  SYSTEM ",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="darkblue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=40)
   
   
        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1460, height=550)
  
        
        # ---------- Left Label Frame ----------
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=3, y=2, width=680, height=530)
        
        img_left = Image.open(r"images/img5.png")
        img_left = img_left.resize((670, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=670, height=130)
        
        # ========== Current Course Information Frame ==========
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=670, height=100)
        
        
        #  ========= Department Label and Combobox ==========
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Paramedical", "Information Technology", "Agriculture", "Pharmacy", "Management", "Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1 , padx=10, pady=5)
        
        #  ========= Course Label and Combobox ==========
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "BCA", "MCA", "BBA", "MBA","B.Pharmacy","Bsc","Msc")
        course_combo.current(0)
        course_combo.grid(row=0, column=3 , padx=10, pady=5)
        
        # ========= Year Label and Combobox ==========
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1 , padx=10, pady=5)
        
        # ========= Semester Label and Combobox ==========
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", 'Semester-1',
        'Semester-2',
        'Semester-3',
        'Semester-4',
        'Semester-5',
        'Semester-6',
        'Semester-7',
        'Semester-8' )
        semester_combo.current(0) 
        semester_combo.grid(row=1, column=3 , padx=10, pady=5)
        
         
        #  ===============class StudentDetailsFrame ==================
        student_details_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        student_details_frame.place(x=5, y=235, width=670, height=260)
         
        #  ===============student ID Label and Entry ==================
        student_id_label = Label(student_details_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=5)
        student_id_entry = ttk.Entry(student_details_frame, textvariable=self.var_std_id, font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=5)
        # ==============Student Name Label and Entry ==================
        student_name_label = Label(student_details_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, pady=5)
        student_name_entry = ttk.Entry(student_details_frame, textvariable=self.var_std_name, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5)
        # ==============DOB Label and Entry ==================
        dob_label = Label(student_details_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=1, column=0, padx=10, pady=5)
        dob_entry = ttk.Entry(student_details_frame, textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=1, column=1, padx=10, pady=5)
        # =============Roll Number Label and Entry ==================
        roll_number_label = Label(student_details_frame, text="Roll Number:", font=("times new roman", 12, "bold"), bg="white")
        roll_number_label.grid(row=1, column=2, padx=10, pady=5)
        roll_number_entry = ttk.Entry(student_details_frame, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        roll_number_entry.grid(row=1, column=3, padx=10, pady=5)
         
        #  =============Gender Label and Combobox ==================
        gender_label = Label(student_details_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5)
        gender_combobox = ttk.Combobox(student_details_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=20)
        gender_combobox["values"] = ("Male", "Female", "Other")
        gender_combobox.grid(row=2, column=1, padx=10, pady=5)
        # ===============Email Label and Entry ==================
        email_label = Label(student_details_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5)
        email_entry = ttk.Entry(student_details_frame, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=3, padx=10, pady=5)
        # ==================Address Label and Entry ==================
        address_label = Label(student_details_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=0, padx=10, pady=5)
        address_entry = ttk.Entry(student_details_frame, textvariable=self.var_address, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=10, pady=5)
        # ==================Phone Number Label and Entry ==================
        phone_number_label = Label(student_details_frame, text="Phone Number:", font=("times new roman", 12, "bold"), bg="white")
        phone_number_label.grid(row=3, column=2, padx=10, pady=5)
        phone_number_entry = ttk.Entry(student_details_frame, textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        phone_number_entry.grid(row=3, column=3, padx=10, pady=5)
         
         
        # =================Radio Buttons for Photo Sample ==================
        self.var_photo = StringVar()
        radiobtn1=ttk.Radiobutton(student_details_frame, text="Take Photo Sample", variable=self.var_photo, value="Yes")
        radiobtn1.grid(row=4, column=0, padx=10, pady=5)
        radiobtn2=ttk.Radiobutton(student_details_frame, text="No Photo Sample", variable=self.var_photo, value="No")
        radiobtn2.grid(row=4, column=1, padx=10, pady=5)
        
        # ============================Buttons Frame ==================
        btn_frame = Frame(student_details_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=170, width=655, height=30)
        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"), bg="#151455", fg="white", width=17)
        save_btn.grid(row=0, column=0)
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="#151455", fg="white", width=17)
        update_btn.grid(row=0, column=1)
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="#151455", fg="white", width=17)
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), bg="#151455", fg="white", width=17)
        reset_btn.grid(row=0, column=3)
         
        take_photo_btn = Button(student_details_frame, text="Take Photo Sample", command=self.generate_dataset, font=("times new roman", 13, "bold"), bg="#093D16", fg="white", width=22)
       
        take_photo_btn.place(x=250, y=205, width=200, height=25)
        
            
        # ========== Right Label Frame ==========
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=690, y=2, width=655, height=530)
        img_right = Image.open(r"images/img13.png")
        img_right = img_right.resize((645, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_right = Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=645, height=130)



                # ================search Frame ==================
        table_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold")
        )

        table_frame.place(x=5, y=135, width=645, height=65)

        table_label = Label(
            table_frame,
            text="Search By:",
            font=("times new roman", 12, "bold"),
            bg="white"
        )

        table_label.grid(row=0, column=0, padx=10, pady=5)

        # ---------- SEARCH COMBO ----------
        self.search_combo = ttk.Combobox(
            table_frame,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=15
        )

        self.search_combo["values"] = (
            "Select",
            "Roll Number",
            "Phone Number"
        )

        self.search_combo.current(0)

        self.search_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=5,
            sticky=W
        )

        # ---------- SEARCH ENTRY ----------
        self.search_entry = ttk.Entry(
            table_frame,
            font=("times new roman", 12, "bold"),
            width=20
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
            sticky=W
        )

        # automatic searching while typing
        self.search_entry.bind("<KeyRelease>", self.search_data)

        # ---------- SHOW ALL BUTTON ----------
        show_all_btn = Button(
            table_frame,
            text="Show All",
            command=self.show_all_data,
            font=("times new roman", 12, "bold"),
            bg="#151455",
            fg="white",
            width=10
        )

        show_all_btn.grid(
            row=0,
            column=3,
            padx=10,
            pady=5,
            sticky=W
        )
        
        
        
   
    # ==============Data frame table===================
        data_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        data_frame.place(x=5, y=200, width=645, height=290)
        
        scroll_x = ttk.Scrollbar(data_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(data_frame, column=("id", "roll", "name", "dob", "gender", "email", "phone", "address", "department", "course", "year", "semester", "PhotoSample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("PhotoSample", text="Photo Sample Status")
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
       
        self.student_table.column("id", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=150)
        self.student_table.column("address", width=200)
        self.student_table.column("department", width=150)
        self.student_table.column("course", width=150)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("PhotoSample", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)  # Bind the table selection event to get_cursor method
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # Fetch data from database and display in the table
       
    # ==============================function buttons ==========================   
     
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_dob.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_photo.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        # Insert data into database (implement your database logic here)
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arpita@1845",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("""
INSERT INTO student(
    student_id,
    roll_no,
    student_name,
    dob,
    gender,
    email,
    phone,
    address,
    department,
    course,
    year,
    semester,
    photo_sample
)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""",(
    self.var_std_id.get(),
    self.var_roll.get(),
    self.var_std_name.get(),
    self.var_dob.get(),
    self.var_gender.get(),
    self.var_email.get(),
    self.var_phone.get(),
    self.var_address.get(),
    self.var_dep.get(),
    self.var_course.get(),
    self.var_year.get(),
    self.var_semester.get(),
    self.var_photo.get()

))
            
            conn.commit()
            self.fetch_data()  # Refresh the data in the table after adding a new student
            conn.close()
            messagebox.showinfo("Success", "Student added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding student: {e}")
       
       
    #  =================fetch data======================
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arpita@1845",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                conn.commit()
            conn.close()
            return rows
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching student data: {e}")
            return []
        
      
    # ================= SEARCH FUNCTION =================

    def search_data(self, event=""):

        search_by = self.search_combo.get()
        search_text = self.search_entry.get().strip()

        # if search box empty -> show all data
        if search_text == "":
            self.fetch_data()
            return

        try:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arpita@1845",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()

            # search by roll number
            if search_by == "Roll Number":

                query = """
                SELECT * FROM student
                WHERE roll_no LIKE %s
                """

            # search by phone number
            elif search_by == "Phone Number":

                query = """
                SELECT * FROM student
                WHERE phone LIKE %s
                """

            else:
                return

            value = search_text + "%"

            my_cursor.execute(query, (value,))

            rows = my_cursor.fetchall()

            # clear old table
            self.student_table.delete(
                *self.student_table.get_children()
            )

            # add new searched rows
            for row in rows:

                item = self.student_table.insert(
                    "",
                    END,
                    values=row
                )

                # highlight matching row
                self.student_table.item(
                    item,
                    tags=("match",)
                )

            # highlight color
            self.student_table.tag_configure(
                "match",
                background="yellow"
            )

            conn.close()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Search Error: {str(e)}"
            )  
        
    # ================= SHOW ALL DATA =================

    def show_all_data(self):

        self.search_entry.delete(0, END)

        self.search_combo.current(0)

        self.fetch_data()  
            
        
        
        
    # ===============get cursor======================
    def get_cursor(self, event=""): 
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        if data:
            self.var_std_id.set(data[0])
            self.var_roll.set(data[1])
            self.var_std_name.set(data[2])
            self.var_dob.set(data[3])
            self.var_gender.set(data[4])
            self.var_email.set(data[5]) 
            self.var_phone.set(data[6])
            self.var_address.set(data[7])
            self.var_dep.set(data[8])
            self.var_course.set(data[9])
            self.var_year.set(data[10])
            self.var_semester.set(data[11])
            self.var_photo.set(data[12])
            
    # ================== update function =========================
    
    def update_data(self):

        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_dob.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_photo.get() =="":

            messagebox.showerror("Error", "All fields are required")
            return

        else:
            try:

                update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details?"
                )

                if update > 0:

                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="arpita@1845",
                        database="face_recognizer"
                    )

                    my_cursor = conn.cursor()

                    my_cursor.execute("""
                    UPDATE student SET   
  
                        roll_no=%s,
                        student_name=%s,
                        dob=%s,
                        gender=%s,
                        email=%s,
                        phone=%s,
                        address=%s,
                        department=%s,
                        course=%s,
                        year=%s,
                        semester=%s,
                        photo_sample=%s
                    WHERE student_id=%s
                    """, (
                        
                         self.var_roll.get(),
    self.var_std_name.get(),
    self.var_dob.get(),
    self.var_gender.get(),
    self.var_email.get(),
    self.var_phone.get(),
    self.var_address.get(),
    self.var_dep.get(),
    self.var_course.get(),
    self.var_year.get(),
    self.var_semester.get(),
    self.var_photo.get(),
    self.var_std_id.get()

                    ))
                else:
                    if not update:
                        return
                    

                messagebox.showinfo(
                        "Success",
                        "Student details updated successfully"
                    )
                conn.commit()

                self.fetch_data()

                conn.close()
                    
                    
            except Exception as e:

                messagebox.showerror(
                    "Error",
                    f"Error updating student data: {str(e)}"
                )
#  =======delete function================

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete a record")
            return

        try:
            delete = messagebox.askyesno(
                "Delete",
                "Do you want to delete this student details?"
            )

            if delete > 0:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arpita@1845",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM student WHERE student_id=%s", (self.var_std_id.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details deleted successfully")
            else:
                if not delete:
                    return

        except Exception as e:
            messagebox.showerror("Error", f"Error deleting student data: {str(e)}")

# =============reset function================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_dob.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_photo.set("")
        
        
# =================generate data set or take photo samples=================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_dob.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_photo.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user = "root",
                    password = "arpita@1845",
                    database = "face_recognizer"
                )
                my_cursor = conn.cursor()
               
                my_cursor.execute("""
                    UPDATE student SET   
  
                        roll_no=%s,
                        student_name=%s,
                        dob=%s,
                        gender=%s,
                        email=%s,
                        phone=%s,
                        address=%s,
                        department=%s,
                        course=%s,
                        year=%s,
                        semester=%s,
                        photo_sample=%s
                    WHERE student_id=%s
                    """, (
                        
                         self.var_roll.get(),
    self.var_std_name.get(),
    self.var_dob.get(),
    self.var_gender.get(),
    self.var_email.get(),
    self.var_phone.get(),
    self.var_address.get(),
    self.var_dep.get(),
    self.var_course.get(),
    self.var_year.get(),
    self.var_semester.get(),
    self.var_photo.get(),
    self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data() 
               
                conn.close()

# =========================load predefined data on face frontals from opencv=========================
                                
                # Create data folder automatically
                base_dir = os.path.dirname(os.path.abspath(__file__))
                data_dir = os.path.join(base_dir, "data")
                os.makedirs(data_dir, exist_ok=True)
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None
                
                cap = cv2.VideoCapture(0) 
                cap.set(3, 640)   # Width
                cap.set(4, 480)   # Height
                img_id = 0
                
                student_id = self.var_std_id.get().strip()

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450), interpolation=cv2.INTER_CUBIC)
                        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        
                                    
                        # Improve brightness and contrast
                        clahe = cv2.createCLAHE(
                            clipLimit=2.0,
                            tileGridSize=(8, 8)
                        )
                                    
                        # Sharpen image
                        kernel = np.array([
                            [0, -1, 0],
                            [-1, 5,-1],
                            [0, -1, 0]
                        ])

                        face = cv2.filter2D(face, -1, kernel)

                        # File path             
                        
                        file_name_path = os.path.join(data_dir, f"user.{student_id}.{img_id}.jpg")
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,   f"{img_id}", (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break
                cap.release()
                
                cv2.destroyAllWindows()
                self.reset_data()
                messagebox.showinfo("Result", "Generating data sets completed!!")
            except Exception as e:
                messagebox.showerror("Error", f"Error generating dataset: {str(e)}")






if __name__ == "__main__":
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    app = Student(root)
    root.mainloop()
    