from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector 
import cv2
import os
import csv
import numpy as np
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state("zoomed")
        
        #==============variables==================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
               
        #============first image=============== 
        self.img_1 = Image.open("images/img7.png")
        self.img_1 = self.img_1.resize((685,130),  Image.Resampling.LANCZOS)
        self.img_1_photo = ImageTk.PhotoImage(self.img_1)

        self.top_label = Label(self.root, image=self.img_1_photo)
        
        self.top_label.place(x=0, y=0, width=685, height=130)
        
        #============second image===============
        self.img_2 = Image.open("images/img5.png")
        self.img_2 = self.img_2.resize((685,130),  Image.Resampling.LANCZOS)
        self.img_2_photo = ImageTk.PhotoImage(self.img_2)

        self.img_2_label = Label(self.root, image=self.img_2_photo)
        
        self.img_2_label.place(x=685, y=0, width=685, height=130)
        
        
         #===============background image================
        self.bg_image = Image.open("images/img1.png")
        self.bg_image = self.bg_image.resize((1530, 790),  Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=130, width=1530, height=790)
        
        title_lbl= Label(self.bg_label, text=" ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=40)
       
       
        #==============main frame====================  
        main_frame=Frame(self.bg_label, bd=2, bg="white")
        main_frame.place(x=0, y= 45, width=1460, height=520)
        
        #Left side label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=3, y=2, width=680, height=510)
        self.img_left = Image.open("images/img9.png")
        self.img_left = self.img_left.resize((670,130),  Image.Resampling.LANCZOS)
        self.img_left_photo = ImageTk.PhotoImage(self.img_left)

        self.left_label = Label(Left_frame, image=self.img_left_photo)
        self.left_label.place(x=5, y=0, width=670, height=130)
        
        left_inside_frame=LabelFrame(Left_frame, bd=2, bg="white", relief= RIDGE)
        left_inside_frame.place(x=0, y=150, width=670, height=270)
       
         #attendance id 
        attendance_ID_label=Label(left_inside_frame, text="Attendance ID :", font=("times new roman", 12, "bold"), bg="white") 
        attendance_ID_label.grid(row=0, column=0, padx=10, pady=5,sticky=W)
        
        attendance_ID_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_id,width=20)
        attendance_ID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # roll
        roll_label=Label(left_inside_frame, text="Roll No. :", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        roll_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_roll,width=20)
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
         #name
        name_label=Label(left_inside_frame, text="Name :", font=("times new roman", 12, "bold"), bg="white") 
        name_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)
        
        name_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"), textvariable=self.var_atten_name,width=20)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
         #date
        date_label=Label(left_inside_frame, text="Date :", font=("times new roman", 12, "bold"), bg="white") 
        date_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_date ,width=20)
        date_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
         #department 
        department_label=Label(left_inside_frame, text="Department :", font=("times new roman", 12, "bold"), bg="white") 
        department_label.grid(row=2, column=0, padx=10, pady=5,sticky=W)
        
        department_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_dep ,width=20)
        department_entry.grid(row=2, column=1, padx=10,  pady=5, sticky=W)
        #time
        time_label=Label(left_inside_frame, text="Time :", font=("times new roman", 12, "bold"), bg="white") 
        time_label.grid(row=2, column=2, padx=10, pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_time ,width=20)
        time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        #date 
        date_label=Label(left_inside_frame, text="Date :", font=("times new roman", 12, "bold"), bg="white") 
        date_label.grid(row=3, column=0, padx=10,  pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,font=("times new roman", 12, "bold"),textvariable=self.var_atten_date ,width=20)
        date_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
  
    # attendence status
        attendence_status_label=Label(left_inside_frame, text="Attendence Status :", font=("times new roman", 12, "bold"), bg="white") 
        attendence_status_label.grid(row=3, column=2, padx=10, pady=5,sticky=W)
       
        attendance_status_combo=ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"),state="readonly" ,width=17 ,textvariable=self.var_atten_attendance)
        attendance_status_combo["values"]=("Select Attendance Status","Present","Absent" )
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        #button frame 
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=205, width=660, height=35)

        
        save_btn=Button(btn_frame, text="Import csv",command= self.importCsv,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0,padx=1.5)
      
        update_btn=Button(btn_frame, text="Export csv",command= self.exportCsv, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1, padx=1.5)
        
        delete_btn=Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2, padx=1.5)
        
        reset_btn=Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"), bg="blue", fg="white", command=self.reset_data,width=17)
        reset_btn.grid(row=0, column=3,padx=1.5)
        


        #Right side label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=690, y=2, width=655, height=510)
       
        right_inside_frame=LabelFrame(Right_frame, bd=2, bg="white", relief= RIDGE)
        right_inside_frame.place(x=5, y=5, width=645, height=420)
        
        #===========scroll bar=====================
        
        scroll_x=ttk.Scrollbar(right_inside_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame, orient=VERTICAL)
        
        
        self.Attendance_table=ttk.Treeview(right_inside_frame, column=("id","roll", "name", "department", "time", "date", "attendence_status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)  
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)
        
        self.Attendance_table.heading("id", text="Attendance ID")
        self.Attendance_table.heading("roll", text="Roll No.")
        self.Attendance_table.heading("name", text="Name")
        self.Attendance_table.heading("department", text="Department")
        self.Attendance_table.heading("time", text="Time")
        self.Attendance_table.heading("date", text="Date")
        self.Attendance_table.heading("attendence_status", text="Attendance Status")
 
        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("roll",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("department",width=100)        
        self.Attendance_table.column("time",width=100)  
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("attendence_status",width=110)
         
         
        self.Attendance_table["show"]="headings"
        self.Attendance_table.pack(fill=BOTH, expand=1)
        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)
       
       #==================fetch data=============
        
    def fetchData(self,rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows :
            self.Attendance_table.insert("",END,values=i)  
#===========================import csv====================  
    def importCsv(self):  
        global mydata
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All_Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
  #==================export csv=======================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All_Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export," "Your data exported to"+os.path.basename(fln)+"Successfully")
          
        except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    #============get cursor=====================
    def get_cursor(self,event=""):
        cursor_row=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def update_data(self):

        # check selection
        selected = self.Attendance_table.focus()

        if selected == "":
            messagebox.showerror("Error", "Please select a row", parent=self.root)
            return

        # validation
        if (
            self.var_atten_id.get() == "" or
            self.var_atten_roll.get() == "" or
            self.var_atten_name.get() == "" or
            self.var_atten_dep.get() == "" or
            self.var_atten_time.get() == "" or
            self.var_atten_date.get() == "" or
            self.var_atten_attendance.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        values = [
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]

        # update treeview
        self.Attendance_table.item(selected, values=values)

        # update list
        index = self.Attendance_table.index(selected)
        mydata[index] = values

        messagebox.showinfo("Success", "Data updated successfully", parent=self.root)
       
        #=============reset================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
             
          
        
            
if __name__ == "__main__":
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    app = Attendance(root)
    root.mainloop()
   