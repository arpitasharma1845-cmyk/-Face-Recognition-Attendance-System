from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector 
# import face_recognition
import dlib
import cv2
import os
import numpy as np
from datetime import datetime
from time import strftime


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state("zoomed")
       
         
        title_lbl= Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="#05036B",)
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #============first image=============== 
        self.img_1 = Image.open("images/img8.0.png")
        self.img_1 = self.img_1.resize((650,700),  Image.Resampling.LANCZOS)
        self.img_1_photo = ImageTk.PhotoImage(self.img_1)

        self.top_label = ttk.Label(self.root, image=self.img_1_photo)
        
        self.top_label.place(x=0, y=43, width=650, height=700)
        
        #============second image===============
        self.img_2 = Image.open("images/img11.png")
        self.img_2 = self.img_2.resize((950,700),  Image.Resampling.LANCZOS)
        self.img_2_photo = ImageTk.PhotoImage(self.img_2)

        self.img_2_label = Label(self.root, image=self.img_2_photo)
        
        self.img_2_label.place(x=650, y=45, width=950, height=700)
          #============Button=============== 
        b1=Button(self.img_2_label, text="Face Recognisation",command=self.face_recog ,cursor="hand2", font=("times new roman", 30, "bold"), bg="#151455", fg="white")
        b1.place(x=150, y=510, width=480, height=100)
        
        
       #===============mark attendence================
    def mark_attendance(self, i,r,d,n):
        file_path = os.path.join(os.path.dirname(__file__), "attendance.csv")
            
            # create set if not exists
        if not hasattr(self, "marked_ids"):
            self.marked_ids = set()

        # already marked → skip
        if i in self.marked_ids:
            return
        
        with open(file_path, "a+",newline="\n") as f:
            f.seek(0)
            
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])
            if (i not in nameList) :
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{n},{d1},{dtString},Present") 
                
                self.marked_ids.add(i)
        
    #===============Face recognisation================
    def face_recog(self):  
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="arpita@1845", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_name from student where student_id=%s", (id,))
                n = my_cursor.fetchone()
                #n="+".join(n)
                n = n[0] if n else "Unknown"
                
                my_cursor.execute("select roll_no from student where student_id=%s",(id,))
                r = my_cursor.fetchone()
                #r="+".join(n)
                r = r[0] if r else "Unknown"

                my_cursor.execute("select department from student where student_id=%s",(id,))
                d = my_cursor.fetchone()
                #d="+".join(n)
                d = d[0] if d else "Unknown"
                
                my_cursor.execute("select student_id from student where student_id=%s",(id,))
                i = my_cursor.fetchone()
                #i="+".join(n)
                i = i[0] if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x,y-100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x,y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll:{r}", (x,y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{d}", (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    
                    self.mark_attendance(i,r,d,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,0,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(
    os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
)
        clf=cv2.face.LBPHFaceRecognizer_create()
        
        
        clf.read(os.path.join(os.path.dirname(__file__), "classifier.xml"))
        video_capture = cv2.VideoCapture(0)
        
        while video_capture.isOpened():
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.putText(img, "Press Q to Exit", (20,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:   # q or ESC
               break
        
        video_capture.release()
        cv2.destroyAllWindows()
        
            
            
            
            
if __name__ == "__main__":
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    app = FaceRecognition(root)
    root.mainloop()
    