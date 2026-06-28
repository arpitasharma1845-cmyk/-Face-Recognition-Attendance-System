from tkinter import *
from PIL import Image, ImageTk
import threading

class Help:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Chatbot")
        self.root.state("zoomed")

        # Background
        bg = Image.open("images/traindata.jpg").resize((1530,790))
        self.bg = ImageTk.PhotoImage(bg)
        Label(self.root, image=self.bg).place(x=0, y=0, width=1530, height=790)

        # Title
        Label(self.root, text="HELP CHATBOT",
              font=("times new roman", 30, "bold"),
              bg="black", fg="white").place(x=0, y=0, width=1530, height=50)

        # Frame
        self.frame = Frame(self.root, bg="#0A0942", bd=3, relief=RIDGE)
        self.frame.place(x=400, y=80, width=690, height=500)
        # Chat box
        self.chat = Text(self.frame, bg="#161616", fg="white", font=("consolas", 12))
        self.chat.place(x=10, y=10, width=660, height=400)
        self.chat.config(state=DISABLED)

        # Input
        self.msg = StringVar()
        self.entry = Entry(
    self.frame,
    textvariable=self.msg,
    font=("times new roman", 14)
)

        self.entry.place(x=10, y=420, width=500, height=40)

        # Press Enter to send message
        self.entry.bind("<Return>", self.enter_send)
                
        Button(self.frame, text="Send", command=self.send,
               bg="blue", fg="white").place(x=520, y=420, width=150, height=40)

        self.insert("Bot", "Hello 👋 Ask me about Face Recognition System issues.")
        
        self.last_issue = ""

    def insert(self, sender, text):
        self.chat.config(state=NORMAL)
        self.chat.insert(END, f"\n{sender}: {text}\n")
        self.chat.config(state=DISABLED)
        self.chat.yview(END)

    def send(self):
        msg = self.msg.get().strip()
        if not msg:
            return

        self.insert("You", msg)
        self.msg.set("")

        threading.Thread(target=self.get_reply, args=(msg,)).start()
    
    def enter_send(self, event):
        self.send()    

      
        #   =========Get reply==========
        
    def get_reply(self, msg):
        msg = msg.lower()

        # ===== DOMAIN CHECK =====
        domain_keywords = [ 
    "face", "recognition", "attendance",
    "opencv", "camera", "mysql", "id",
    "data", "classifier", "dataset",
    "training", "image", "csv",
    "database", "model", "haar",
    "detect", "recognize"
]
        if not any(word in msg for word in domain_keywords):
            reply = "❌ Sorry, I only answer questions related to Face Recognition Attendance System."
            self.insert("Bot", reply)
            return
       
                
        # ===== PREDEFINED ANSWERS =====

        if "face not detected" in msg or "not detect" in msg:
            reply = "Make sure camera is working, good lighting is available, and face is clearly visible. Also check Haarcascade file path."
        
       
        elif "unknown person" in msg or "unknown" in msg or "face dont recognize" in msg:
            self.last_issue = "face_not_recognized"

            reply = (
        "The system is unable to recognize your face. "
        "This usually happens when the model is not trained properly "
        "or images are unclear. Try retraining with more clear images."
    )
        elif "wrong id" in msg or "wrong name" in msg:
            self.last_issue = "wrong_id"

            reply = (
                "Your system is showing the wrong ID or name. "
                "This often happens because of incorrect dataset labels "
                "or duplicate IDs."
            )
        elif "someone else name" in msg:
            reply = "Your model is confused due to poor training. Add more images and retrain classifier."

        elif "data not found" in msg:
            reply = "Check MySQL connection and ensure correct query execution. Verify database records exist."

        elif "attendance not saved" in msg or "csv" in msg:
            self.last_issue = "attendance"

            reply = (
                "Attendance is not being stored correctly. "
                "Please check your CSV file path and write permissions."
            )
        elif "name not appear" in msg:
            reply = "Ensure correct ID is fetched from database and written into attendance file."
        elif "id not found" in msg:
            reply = "ID not found means your database does not contain that ID. Check if data is inserted correctly in MySQL and ID matches training data."
        elif "Hello" in msg :
            reply="Hello I'm a Chatbot!! Here to help you. Just tell me your problem"
        
        elif "image not found" in msg or "dataset not found" in msg:
            reply = "Check dataset folder path. Make sure images exist and file names are correct. Also verify your code path is correct."

        elif "model not working" in msg or "classifier not working" in msg:
            reply = "Your trained model file may be missing or outdated. Retrain the model and ensure classifier file path is correct."

        elif "camera not working" in msg or "camera not open" in msg:
            reply = "Check if camera is connected properly. Try changing camera index (0,1). Also ensure no other app is using the camera."

        elif "opencv error" in msg:
            reply = "Check if OpenCV is installed properly. Also verify version compatibility and required DLL files."

        elif "training not working" in msg:
            reply = "Ensure all images are in dataset folder and properly labeled. Also check if training script runs without errors."

        elif "face mismatch" in msg:
            reply = "Face mismatch occurs due to low-quality images or insufficient training data. Add more clear images and retrain."

        elif "duplicate id" in msg:
            reply = "Duplicate ID causes confusion in recognition. Ensure each person has unique ID in database and dataset."

        elif "slow detection" in msg or "lag" in msg:
            reply = "Reduce image resolution or optimize code. High resolution and heavy processing cause delay."

        elif "attendance duplicate" in msg:
            reply = "Check your attendance logic. Ensure entry is written only once per session using condition checks."

        elif "csv not updating" in msg:
            reply = "Make sure file is opened in append mode ('a+') and file path is correct."

        elif "database not connected" in msg:
            reply = "Check MySQL credentials (host, user, password). Also ensure MySQL server is running."

        elif "sql error" in msg:
            reply = "Verify your SQL query syntax and table/column names. Also check database connection."

        elif "image blur" in msg or "low quality image" in msg:
            reply = "Use clear and high-quality images. Avoid blur, low light, or tilted faces."

        elif "multiple faces" in msg:
            reply = "System may confuse identities if multiple faces appear. Try detecting one face at a time."

        elif "haar cascade not working" in msg:
            reply = "Check Haarcascade XML file path. Ensure file exists and is loaded correctly."

        elif "face not recognized after training" in msg:
            reply = "Retrain model after adding images. Also restart system to load updated classifier."

        elif "wrong attendance entry" in msg:
            reply = "Check mapping between recognized ID and database name. Also verify CSV writing logic."

        elif "file path error" in msg:
            reply = "Ensure all file paths (dataset, classifier, CSV) are correct and accessible."

        elif "permission denied" in msg:
            reply = "Run program as administrator or check folder permissions for read/write access."

        elif "empty dataset" in msg:
            reply = "Dataset folder is empty or not loaded. Add images before training."

        elif "training taking too long" in msg:
            reply = "Reduce dataset size or optimize training code. Large datasets increase training time."

        elif "face detection rectangle not showing" in msg:
            reply = "Ensure OpenCV drawing function is correct and frame is displayed properly."

        elif "program crashing" in msg:
            reply = "Check error logs in terminal. Most crashes happen due to missing files or wrong paths."
            
        # ===== FALLBACK (RELATED BUT NOT EXACT) =====
        # else:
        #     reply = ("I understand your issue is related to the system. "
        #     "Here are a few things you can quickly check:\n"
        #     "• Is your dataset properly trained?\n"
        #     "• Is the camera working fine?\n"
        #     "• Are file paths correct?\n"
        #     "• Is database connected?\n"
        #     "If you can be more specific, I’ll help you better."
        # )
        # self.insert("Bot", reply)
        
        
                 
        follow_up_words = [
            "yes",
            "no",
            "still not working",
            "not solved",
            "issue not solved",
            "everything is correct",
            "all correct",
            "still issue",
            "still problem",
            "not fixed"
        ]

        if any(word in msg for word in follow_up_words):

            # ===== FACE NOT RECOGNIZED FOLLOW-UP =====
            if self.last_issue == "face_not_recognized":
                reply = (
                    "If everything looks correct but face recognition still fails, "
                    "then try these advanced checks:\n\n"
                    "• Delete old classifier.xml and retrain model\n"
                    "• Add at least 50-100 clear images per person\n"
                    "• Ensure lighting is good\n"
                    "• Resize image before recognition\n"
                    "• Check confidence value condition in your code\n"
                    "• Restart application after retraining"
                )

            # ===== WRONG ID FOLLOW-UP =====
            elif self.last_issue == "wrong_id":
                reply = (
                    "Wrong ID usually happens because training labels don't match database IDs.\n\n"
                    "Check these:\n"
                    "• Dataset image naming format\n"
                    "• Correct ID stored in MySQL\n"
                    "• Remove duplicate IDs\n"
                    "• Retrain classifier after changing data"
                )

            # ===== ATTENDANCE FOLLOW-UP =====
            elif self.last_issue == "attendance":
                reply = (
                    "If attendance is still not saving:\n\n"
                    "• Check CSV file path\n"
                    "• Ensure file opens with a+ mode\n"
                    "• Verify mark_attendance() function is called\n"
                    "• Check if duplicate prevention logic blocks entry"
                )

            else:
                reply = (
                    "Please explain your issue in more detail so I can help you better."
                )

            self.insert("Bot", reply)
            return
         
        
        
        
    
    
    def auto_ask(self, question):
        self.msg.set(question)
        self.send()
        
# Run
if __name__ == "__main__":
    root = Tk()
    app = Help(root)
    root.mainloop()  