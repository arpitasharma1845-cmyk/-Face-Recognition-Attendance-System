from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import dlib
import cv2
import os
import numpy as np
from datetime import datetime
from time import strftime


class FaceRecognition:

    def __init__(self, root):

        self.root = root
        self.root.title("AI Face Recognition Attendance System")
        self.root.state("zoomed")
        self.root.config(bg="#0b1220")

        # ================= HEADER =================
        header = Frame(self.root, bg="#111827", height=70)
        header.pack(fill=X)

        title_lbl = Label(
            header,
            text="AI FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Montserrat", 28, "bold"),
            bg="#111827",
            fg="white"
        )

        title_lbl.pack(pady=12)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="#0b1220")
        main_frame.pack(fill=BOTH, expand=True)

        # ================= LEFT PANEL =================
        left_frame = Frame(
            main_frame,
            bg="#111827",
            bd=0
        )

        left_frame.place(x=5, y=5, width=600, height=600)

        left_title = Label(
            left_frame,
            text="Face Detection Preview",
            font=("Montserrat", 18, "bold"),
            bg="#111827",
            fg="white"
        )

        left_title.pack(pady=15)

        # ================= IMAGE 1 =================
        self.img_1 = Image.open("images/img8.0.png")
        self.img_1 = self.img_1.resize((440, 450), Image.Resampling.LANCZOS)
        self.img_1_photo = ImageTk.PhotoImage(self.img_1)

        self.top_label = Label(
            left_frame,
            image=self.img_1_photo,
            bd=0
        )

        self.top_label.pack(pady=10)

        # ================= STATUS FRAME =================
        status_frame = Frame(
            left_frame,
            bg="#111827",
           
        )

        status_frame.pack(fill=X, padx=20, pady=15)

        self.status_lbl = Label(
            status_frame,
            text="System Ready",
            font=("Montserrat", 14, "bold"),
            bg="#111827",
            fg="#22c55e"
        )

        self.status_lbl.pack(pady=5, padx=5)

        # ================= RIGHT PANEL =================
        right_frame = Frame(
            main_frame,
            bg="#111827",
            bd=0
        )

        right_frame.place(x=540, y=5, width=800, height=600)

        right_title = Label(
            right_frame,
            text="Live Recognition Panel",
            font=("Montserrat", 18, "bold"),
            bg="#111827",
            fg="white"
        )

        right_title.pack(pady=15)

        # ================= IMAGE 2 =================
        self.img_2 = Image.open("images/img11.png")
        self.img_2 = self.img_2.resize((820, 450), Image.Resampling.LANCZOS)
        self.img_2_photo = ImageTk.PhotoImage(self.img_2)

        self.img_2_label = Label(
            right_frame,
            image=self.img_2_photo,
            bd=0
        )

        self.img_2_label.pack(pady=10)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(
            right_frame,
            bg="#111827"
        )

        btn_frame.pack(pady=20)

        # ================= FACE BUTTON =================
        b1 = Button(
            btn_frame,
            text="START FACE RECOGNITION",
            command=self.face_recog,
            cursor="hand2",
            font=("Montserrat", 18, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0
        )

        b1.pack(ipadx=30, ipady=12)

        # ================= HOVER EFFECT =================
        def on_enter(e):
            b1["bg"] = "#1d4ed8"

        def on_leave(e):
            b1["bg"] = "#2563eb"

        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # ================= FOOTER =================
        footer = Label(
            self.root,
            text="AI Powered Attendance Monitoring System",
            font=("Montserrat", 10),
            bg="#111827",
            fg="gray"
        )

        footer.pack(side=BOTTOM, fill=X)

    # ================= MARK ATTENDANCE =================
    def mark_attendance(self, i, r, d, n):

        file_path = os.path.join(
            os.path.dirname(__file__),
            "attendance.csv"
        )

        if not hasattr(self, "marked_ids"):
            self.marked_ids = set()

        if i in self.marked_ids:
            return

        with open(file_path, "a+", newline="\n") as f:

            f.seek(0)

            myDataList = f.readlines()

            nameList = []

            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])

            if i not in nameList:

                now = datetime.now()

                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")

                f.writelines(
                    f"\n{i},{r},{d},{n},{d1},{dtString},Present"
                )

                self.marked_ids.add(i)

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        self.status_lbl.config(
            text="Camera Started",
            fg="#eab308"
        )

        def draw_boundary(
            img,
            classifier,
            scaleFactor,
            minNeighbors,
            color,
            text,
            clf
        ):

            gray_image = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )

            features = classifier.detectMultiScale(
                gray_image,
                scaleFactor,
                minNeighbors
            )

            coord = []

            for (x, y, w, h) in features:

                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    3
                )

                id, predict = clf.predict(
                    gray_image[y:y + h, x:x + w]
                )

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="arpita@1845",
                    database="face_recognizer"
                )

                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select student_name from student where student_id=%s",
                    (id,)
                )

                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute(
                    "select roll_no from student where student_id=%s",
                    (id,)
                )

                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute(
                    "select department from student where student_id=%s",
                    (id,)
                )

                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute(
                    "select student_id from student where student_id=%s",
                    (id,)
                )

                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                if confidence > 77:

                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 100),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 70),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 40),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    self.mark_attendance(i, r, d, n)

                else:

                    cv2.rectangle(
                        img,
                        (x, y),
                        (x + w, y + h),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):

            coord = draw_boundary(
                img,
                faceCascade,
                1.1,
                10,
                (255, 0, 255),
                "Face",
                clf
            )

            return img

        faceCascade = cv2.CascadeClassifier(
            os.path.join(
                os.path.dirname(__file__),
                "haarcascade_frontalface_default.xml"
            )
        )

        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.read(
            os.path.join(
                os.path.dirname(__file__),
                "classifier.xml"
            )
        )

        video_capture = cv2.VideoCapture(0)

        while video_capture.isOpened():

            ret, img = video_capture.read()

            img = recognize(
                img,
                clf,
                faceCascade
            )

            cv2.putText(
                img,
                "Press Q to Exit",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow(
                "Welcome to Face Recognition",
                img
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q') or key == 13:
                break

        video_capture.release()

        cv2.destroyAllWindows()

        self.status_lbl.config(
            text="System Ready",
            fg="#22c55e"
        )


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    root.protocol(
        "WM_DELETE_WINDOW",
        root.destroy
    )

    app = FaceRecognition(root)

    root.mainloop()