from tkinter import *
from PIL import Image, ImageTk
import itertools

class About:
    def __init__(self, root):
        self.root = root
        self.root.title("About Project")
        self.root.state("zoomed")
        self.root.configure(bg="#0f172a")

        # ================= TITLE =================
        self.colors = itertools.cycle([
            "#00FFFF", "#00FF99", "#FFD700",
            "#FF69B4", "#FFA500", "#7CFC00"
        ])

        self.title_lbl = Label(
            self.root,
            text="SMART ATTENDANCE FACE RECOGNITION SYSTEM",
            font=("times new roman", 32, "bold"),
            bg="#020617",
            fg="cyan",
            pady=15
        )

        self.title_lbl.pack(fill=X)
        self.animate_title()

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="#0f172a")
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # ================= LEFT SIDE =================
        left_frame = Frame(main_frame, bg="#111827", bd=3, relief=RIDGE)
        left_frame.place(x=5, y=20, width=700, height=600)

        Label(
            left_frame,
            text="About The Project",
            font=("times new roman", 26, "bold"),
            bg="#111827",
            fg="#38BDF8"
        ).pack(pady=15)

        about_text = """
The Smart Attendance Face Recognition System is an AI-powered 
attendance management project developed using Python, OpenCV,
Tkinter, MySQL, and Machine Learning concepts.

This system automatically detects and recognizes faces through
a webcam and marks attendance without manual entry.

It eliminates fake attendance, reduces paperwork,
saves time, and improves accuracy in schools,
colleges, and offices.

Main Technologies Used:
• Python
• OpenCV
• Haarcascade Algorithm
• LBPH Face Recognizer
• Tkinter GUI
• MySQL Database
• CSV File Handling

The system can:
✔ Detect faces in real time
✔ Train facial datasets
✔ Recognize registered users
✔ Mark attendance automatically
✔ Store records securely
✔ Manage student information

This project is useful for:
• Colleges
• Schools
• Offices
• Smart Institutions
• Employee Attendance Systems
"""

        text_box = Text(
            left_frame,
            font=("consolas", 13),
            bg="#1E293B",
            fg="white",
            wrap=WORD,
            relief=FLAT,
            padx=15,
            pady=15
        )

        text_box.pack(fill=BOTH, expand=True, padx=15, pady=10)
        text_box.insert(END, about_text)
        text_box.config(state=DISABLED)

        # ================= RIGHT SIDE =================
        right_frame = Frame(main_frame, bg="#111827", bd=3, relief=RIDGE)
        right_frame.place(x=720, y=20, width=590, height=600)

        Label(
            right_frame,
            text="Project Features",
            font=("times new roman", 26, "bold"),
            bg="#111827",
            fg="#4ADE80"
        ).pack(pady=15)

        # ===== Feature Cards =====
        features = [
            ("🎯 Real-Time Detection", "Detects faces instantly using webcam."),
            ("🧠 Smart Recognition", "Recognizes registered users accurately."),
            ("📂 Attendance Storage", "Stores attendance in CSV and MySQL."),
            ("⚡ Fast Processing", "Optimized for quick performance."),
            ("🔒 Secure Data", "Maintains secure student records."),
            ("💻 User Friendly GUI", "Easy and interactive interface.")
        ]

        y_pos = 80

        for title, desc in features:
            card = Frame(
                right_frame,
                bg="#1E293B",
                bd=2,
                relief=RIDGE,
                cursor="hand2"
            )

            card.place(x=30, y=y_pos, width=520, height=70)

            card.bind("<Enter>",
                      lambda e, c=card: c.config(bg="#334155"))

            card.bind("<Leave>",
                      lambda e, c=card: c.config(bg="#1E293B"))

            Label(
                card,
                text=title,
                font=("times new roman", 16, "bold"),
                bg="#1E293B",
                fg="#FACC15"
            ).place(x=15, y=8)

            Label(
                card,
                text=desc,
                font=("consolas", 11),
                bg="#1E293B",
                fg="white"
            ).place(x=15, y=38)

            y_pos += 85

        # ================= FOOTER =================
        footer = Label(
            self.root,
            text="Developed Using Python • OpenCV • Tkinter • MySQL",
            font=("times new roman", 15, "bold"),
            bg="#020617",
            fg="white",
            pady=10
        )

        footer.pack(side=BOTTOM, fill=X)

    # ================= ANIMATION =================
    def animate_title(self):
        self.title_lbl.config(fg=next(self.colors))
        self.root.after(500, self.animate_title)


# ================= RUN =================
if __name__ == "__main__":
    root = Tk()
    obj = About(root)
    root.mainloop()

