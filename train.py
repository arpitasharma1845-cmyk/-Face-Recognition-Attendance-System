from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import threading


class Train:

    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state("zoomed")
        self.root.configure(bg="#0f172a")

        # ================= TITLE =================
        self.title_lbl = Label(
            self.root,
            text="TRAIN FACE DATASET",
            font=("times new roman", 34, "bold"),
            bg="#020617",
            fg="#4ADE80",
            pady=12
        )

        self.title_lbl.pack(fill=X)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="#0f172a")
        main_frame.pack(fill=BOTH, expand=True)

        # ================= LEFT IMAGE =================
        img = Image.open("images/img4.png")
        img = img.resize((750, 650), Image.Resampling.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)

        left_label = Label(
            main_frame,
            image=self.photoimg,
            bd=0
        )

        left_label.place(x=10, y=10, width=750, height=580)

        # ================= RIGHT PANEL =================
        right_frame = Frame(
            main_frame,
            bg="#111827",
            bd=4,
            relief=RIDGE
        )

        right_frame.place(x=800, y=10, width=500, height=560)

        # ================= HEADING =================
        heading = Label(
            right_frame,
            text="Train Recognition Model",
            font=("times new roman", 28, "bold"),
            bg="#111827",
            fg="#4ADE80"
        )

        heading.pack(pady=20)

        # ================= DESCRIPTION =================
        desc = Label(
            right_frame,
            text=(
                "This module trains the face recognition\n"
                "model using stored dataset images.\n\n"
                "• Reads all dataset images\n"
                "• Converts images to grayscale\n"
                "• Extracts face IDs\n"
                "• Trains LBPH recognizer\n"
                "• Saves trained classifier.xml"
            ),
            font=("consolas", 13),
            bg="#111827",
            fg="white",
            justify=LEFT
        )

        desc.pack(pady=20)

        # ================= STATUS CARD =================
        self.status_lbl = Label(
            right_frame,
            text="Status : Waiting to Start Training",
            font=("times new roman", 16, "bold"),
            bg="#1E293B",
            fg="#FACC15",
            relief=RIDGE,
            padx=15,
            pady=10
        )

        self.status_lbl.pack(pady=20, fill=X, padx=30)

        # ================= PROGRESS BAR =================
        self.progress = ttk.Progressbar(
            right_frame,
            orient=HORIZONTAL,
            length=350,
            mode='indeterminate'
        )

        self.progress.pack(pady=20)

        # ================= TRAIN BUTTON =================
        self.train_btn = Button(
            right_frame,
            text="TRAIN DATA",
            command=self.start_training_thread,
            font=("times new roman", 22, "bold"),
            bg="#16A34A",
            fg="white",
            activebackground="#15803D",
            activeforeground="white",
            cursor="hand2",
            bd=0,
            padx=20,
            pady=12
        )

        self.train_btn.pack(pady=30)

        # Hover Effect
        self.train_btn.bind("<Enter>", self.on_enter)
        self.train_btn.bind("<Leave>", self.on_leave)

        # ================= FOOTER =================
        footer = Label(
            self.root,
            text="Smart Attendance Face Recognition System",
            font=("times new roman", 14, "bold"),
            bg="#020617",
            fg="white",
            pady=8
        )

        footer.pack(side=BOTTOM, fill=X)

    # ================= BUTTON HOVER =================
    def on_enter(self, event):
        self.train_btn.config(bg="#22C55E")

    def on_leave(self, event):
        self.train_btn.config(bg="#16A34A")

    # ================= THREAD =================
    def start_training_thread(self):
        threading.Thread(target=self.train_classifier).start()

    # ================= TRAIN FUNCTION =================
    def train_classifier(self):

        self.status_lbl.config(
            text="Status : Training Started...",
            fg="#38BDF8"
        )

        self.progress.start(10)

        data_dir = "data"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")

        path = [
            os.path.join(data_dir, file)
            for file in sorted(os.listdir(data_dir))
        ]

        faces = []
        ids = []

        for image in path:

            img = Image.open(image).convert('L')

            imageNp = np.array(img, 'uint8')

            filename = os.path.split(image)[1]

            parts = filename.split('.')

            if len(parts) > 1 and parts[1].isdigit():
                id = int(parts[1])
            else:
                continue

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training Dataset", imageNp)

            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ================= VALIDATION =================
        if len(faces) == 0 or len(ids) == 0:

            self.progress.stop()

            self.status_lbl.config(
                text="Status : No Valid Images Found",
                fg="red"
            )

            messagebox.showerror(
                "Error",
                "No valid training images found",
                parent=self.root
            )

            return

        # ================= TRAIN MODEL =================
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces, ids)

        clf.write("classifier.xml")

        cv2.destroyAllWindows()

        self.progress.stop()

        self.status_lbl.config(
            text="Status : Training Completed Successfully",
            fg="#4ADE80"
        )

        messagebox.showinfo(
            "Result",
            "Training datasets completed successfully!",
            parent=self.root
        )


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = Train(root)

    root.mainloop()

