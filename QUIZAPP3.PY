import random
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
import sqlite3

# ---------------- DATABASE ---------------- #
conn = sqlite3.connect("quiz1.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    score INTEGER
)
""")
conn.commit()

# ---------------- QUESTIONS ---------------- #
questions = [
{"q":"What is the hardest natural substance on earth?","options":["Gold","Iron","Diamond","Graphite"],"ans":"Diamond"},
{"q":"Who has the power to declare a national emergency in India?","options":["Prime minister","President","Chief justice of India","Defence minister"],"ans":"President"},
{"q":"Who is known as the Father of Python?","options":["Charles Babbage","Guido Van Rossum","Berners's Lee","Alan Turing"],"ans":"Guido Van Rossum"},
{"q":"Founder of Microsoft?","options":["Elon Musk","Steve Jobs","Bill Gates","Mark"],"ans":"Bill Gates"},
{"q":"Which component store data permanently even when computer is turned off?","options":["RAM","ROM","Cache","CPU"],"ans":"ROM"},
{"q":"What does AI stand for?","options":["Automated interface","Algorithmic input","Analog integration","Artificial intelligence"],"ans":"Artificial intelligence"},
{"q":"Which keyword is used to define a function in Python?","options":["func","define","def","function"],"ans":"def"},
{"q":"What does RAM stand for?","options":["Random Access Memory","Read Access Memory","Run Access Memory","Real Access Memory"],"ans":"Random Access Memory"},
{"q":"Which language is used for web apps?","options":["Python","JavaScript","C++","Java"],"ans":"JavaScript"},
{"q":"Which key deletes text?","options":["Enter","Shift","Delete","Ctrl"],"ans":"Delete"},
{"q":"Which is fastest memory?","options":["RAM","ROM","Cache","Hard disk"],"ans":"Cache"},
{"q":"Which is output device?","options":["Keyboard","Mouse","Printer","Scanner"],"ans":"Printer"},
{"q":"Binary numbers use?","options":["0 and 1","1 and 2","2 and 3","3 and 4"],"ans":"0 and 1"},
{"q":"Which data type holds text?","options":["int","str","float","bool"],"ans":"str"},
{"q":"Which keyword handles error?","options":["try","catch","error","fix"],"ans":"try"},
{"q":"What is the full form of CPU?","options":["Central Process Unit","Central Processing Unit","Computer Personal Unit","Central Program Utility"],"ans":"Central Processing Unit"},
{"q":"Which device is used to display output?","options":["Keyboard","Mouse","Monitor","Scanner"],"ans":"Monitor"},
{"q":"Which company developed Windows OS?","options":["Apple","Google","Microsoft","IBM"],"ans":"Microsoft"},
{"q":"What is the brain of the computer?","options":["RAM","CPU","ROM","Keyboard"],"ans":"CPU"},
{"q":"Which memory is temporary?","options":["ROM","Hard Disk","RAM","SSD"],"ans":"RAM"},
{"q":"Which key is used to refresh?","options":["F1","F2","F5","F10"],"ans":"F5"},
{"q":"Which device prints documents?","options":["Monitor","Printer","Keyboard","Mouse"],"ans":"Printer"},
{"q":"What is the full form of USB?","options":["Universal Serial Bus","United System Board","Universal System Bus","Unique Serial Board"],"ans":"Universal Serial Bus"},
{"q":"Which software is used for presentations?","options":["MS Word","MS Excel","MS PowerPoint","Paint"],"ans":"MS PowerPoint"},
{"q":"Which software is used for calculations?","options":["MS Word","MS Excel","Paint","Notepad"],"ans":"MS Excel"},
{"q":"Which part stores files permanently?","options":["RAM","ROM","Hard Disk","Cache"],"ans":"Hard Disk"},
{"q":"Which symbol is used for multiplication in Python?","options":["x","*","+","/"],"ans":"*"},
{"q":"Which keyword is used for decision making?","options":["for","while","if","loop"],"ans":"if"},
{"q":"Which loop works until condition is false?","options":["for","while","switch","if"],"ans":"while"},
{"q":"Which function converts string to integer?","options":["str()","float()","int()","chr()"],"ans":"int()"},
{"q":"Which data type stores decimal numbers?","options":["int","bool","float","str"],"ans":"float"},
{"q":"Which operator gives remainder?","options":["/","%","*","//"],"ans":"%"},
{"q":"Which is a search engine?","options":["Google","Windows","Python","Linux"],"ans":"Google"},
{"q":"What is the shortcut for copy?","options":["Ctrl + X","Ctrl + C","Ctrl + V","Ctrl + Z"],"ans":"Ctrl + C"},
{"q":"What is the shortcut for paste?","options":["Ctrl + X","Ctrl + V","Ctrl + P","Ctrl + C"],"ans":"Ctrl + V"},
{"q":"Which is an example of input device?","options":["Speaker","Printer","Keyboard","Monitor"],"ans":"Keyboard"},
{"q":"Which one is system software?","options":["Windows","MS Word","Chrome","PowerPoint"],"ans":"Windows"},
{"q":"Which one is application software?","options":["Linux","Windows","MS Word","BIOS"],"ans":"MS Word"},
{"q":"Which language is mainly used for web designing?","options":["Python","HTML","C++","Java"],"ans":"HTML"},
{"q":"What does WWW stand for?","options":["World Wide Web","World Web Wide","Wide World Web","Web World Wide"],"ans":"World Wide Web"},
{"q":"Which network covers a small area?","options":["WAN","MAN","LAN","Internet"],"ans":"LAN"},
{"q":"Which key is used to enter new line?","options":["Shift","Ctrl","Enter","Delete"],"ans":"Enter"},
{"q":"Which company developed Python?","options":["Google","Microsoft","Python Software Foundation","IBM"],"ans":"Python Software Foundation"},
{"q":"Which operator is used for assignment?","options":["==","=","!=","<"],"ans":"="},
{"q":"Which function is used to display output in Python?","options":["input()","show()","print()","echo()"],"ans":"print()"},
{"q":"Which keyword is used to define class in Python?","options":["class","object","define","struct"],"ans":"class"},
{"q":"Which symbol is used for list in Python?","options":["()","[]","{}","<>"],"ans":"[]"},
{"q":"Which symbol is used for tuple?","options":["()","[]","{}","<>"],"ans":"()"},
{"q":"Which symbol is used for dictionary?","options":["()","[]","{}","<>"],"ans":"{}"},
{"q":"Which function gives user input?","options":["input()","print()","show()","scan()"],"ans":"input()"},
{"q":"Which keyword skips current loop iteration?","options":["break","pass","continue","stop"],"ans":"continue"},
{"q":"Which statement is used to handle exceptions?","options":["if","error","try","catch"],"ans":"try"},
{"q":"Which company created Android?","options":["Google","Apple","Microsoft","Nokia"],"ans":"Google"},
{"q":"Which storage device is fastest?","options":["Hard Disk","DVD","SSD","Pen Drive"],"ans":"SSD"},
{"q":"Which file extension is used for text files?","options":[".py",".txt",".jpg",".mp3"],"ans":".txt"}
]
# ---------------- GLOBAL VARIABLES ---------------- #
index = 0
score = 0
timer = 15
username = ""
timer_id = None
current_questions = []
# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Smart Quiz Application - Mini Project")

# WINDOW CENTER
window_width = 900
window_height = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#0f172a")                                                                                                                                                                                                                                                                                                                                                                                    

# ---------------- STYLE ---------------- #
style = Style()
style.theme_use("default")
style.configure(
    "TProgressbar",
    thickness=18,
    background="#38bdf8",
    troughcolor="#1e293b"
)

# ---------------- FUNCTIONS ---------------- #
def show_frame(frame):
    frame.tkraise()
def login():
    global username
    username = entry_user.get()
    password = entry_pass.get()
    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Please enter Username and Password"
        )
    else:
        welcome_label.config(
        text=f"Welcome {username}! Ready to test your knowledge?"
)
        
        show_frame(start_frame)
def start_quiz():
    global index, score, current_questions
    index = 0
    score = 0
    current_questions = random.sample(questions, 15)
    show_frame(quiz_frame)
    load_question()
def animate_question():
    question_label.config(fg="yellow")
    root.after(
        300,
        lambda: question_label.config(fg="white")
    )
def load_question():
    global timer, timer_id
    if index < len(current_questions):
        q = current_questions[index]
        question_label.config(text=q["q"])
        # CLEAR OLD OPTION
        var.set(None)
        animate_question()
        options_list = q["options"].copy()
        random.shuffle(options_list)
        for i in range(4):
            options[i].config(
                text=options_list[i],
                value=options_list[i]
            )
        progress["value"] = (
            (index + 1) / len(current_questions)
        ) * 100
        if timer_id:
            root.after_cancel(timer_id)
        timer = 15
        countdown()
    else:
        show_result()
def next_question():
    global index, score
    # CHECK ANSWER
    if var.get() != "":
        if var.get() == current_questions[index]["ans"]:
            score += 1
    # NEXT QUESTION
    index += 1
    # CLEAR OPTION
    var.set(None)
    if index < len(current_questions):
        load_question()
    else:
        show_result()
def countdown():
    global timer, timer_id, index

    if timer <= 5:
        timer_label.config(fg="red")
    else:
        timer_label.config(fg="white")

    timer_label.config(
        text=f"Time Left : {timer} sec"
    )

    if timer > 0:

        timer -= 1

        timer_id = root.after(
            1000,
            countdown
        )
    else:
        index += 1
        var.set(None)

        if index < len(current_questions):
            load_question()
        else:
            show_result()

def show_result():
    if timer_id:
        root.after_cancel(timer_id)

    show_frame(result_frame)

    result_label.config(
        text=f"{username}, Your Score is {score}/15 🎉"
    )

    cursor.execute(
    "INSERT INTO users VALUES(?,?)",
    (username, score)
    )

    conn.commit()

def restart():
    show_frame(start_frame)
def view_scores():
    cursor.execute(
        "SELECT username, score FROM users ORDER BY score DESC LIMIT 5"
    )
    data = cursor.fetchall()
    scores = "🏆 TOP 5 LEADERBOARD 🏆\n\n"
    for row in data:
        scores += f"{row[0]} ➜ {row[1]}\n"
    messagebox.showinfo(
        "Leaderboard",
        scores if data else "No Data Available"
    )

# ---------------- FRAMES ---------------- #

login_frame = tk.Frame(root, bg="#0f172a")
start_frame = tk.Frame(root, bg="#0f172a")
quiz_frame = tk.Frame(root, bg="#0f172a")
result_frame = tk.Frame(root, bg="#0f172a")

for frame in (
    login_frame,
    start_frame,
    quiz_frame,
    result_frame
):
    frame.place(
        relwidth=1,
        relheight=1
    )

# ---------------- LOGIN PAGE ---------------- #

login_box = tk.Frame(
    login_frame,
    bg="#1e293b",
    padx=40,
    pady=40
)

login_box.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

tk.Label(
    login_box,
    text="SMART QUIZ APP",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#1e293b"
).pack(pady=20)

tk.Label(
    login_box,
    text="Username",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e293b"
).pack(anchor="w", pady=(10, 5))

entry_user = tk.Entry(
    login_box,
    font=("Arial", 14),
    width=25
)

entry_user.pack(pady=5)

tk.Label(
    login_box,
    text="Password",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e293b"
).pack(anchor="w", pady=(15, 5))

entry_pass = tk.Entry(
    login_box,
    show="*",
    font=("Arial", 14),
    width=25
)

entry_pass.pack(pady=5)

tk.Button(
    login_box,
    text="Login",
    command=login,
    bg="#38bdf8",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15,
    relief="flat",
    cursor="hand2"
).pack(pady=25)

# ---------------- START PAGE ---------------- #

welcome_label = tk.Label(
    start_frame,
    text="",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0f172a"
)

welcome_label.pack(pady=40)

tk.Label(
    start_frame,
    text="SMART QUIZ APP",
    font=("Arial", 30, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
).pack(pady=20)

tk.Button(
    start_frame,
    text="Start Quiz",
    command=start_quiz,
    bg="#22c55e",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20
).pack(pady=15)

tk.Button(
    start_frame,
    text="Leaderboard",
    command=view_scores,
    bg="#f59e0b",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20
).pack(pady=10)

# ---------------- QUIZ PAGE ---------------- #

question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0f172a",
    wraplength=700,
    justify="center"
)

question_label.pack(pady=40)

progress = Progressbar(
    quiz_frame,
    length=400
)

progress.pack(pady=10)

var = tk.StringVar()

options = []

for i in range(4):

    rb = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=var,
        value="",
        font=("Arial", 14),
        bg="#0f172a",
        fg="white",
        selectcolor="#1e293b",
        activebackground="#0f172a",
        activeforeground="white"
    )

    rb.pack(pady=10)

    options.append(rb)

timer_label = tk.Label(
    quiz_frame,
    text="Time Left : 15 sec",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#0f172a"
)

timer_label.pack(pady=20)

tk.Button(
    quiz_frame,
    text="Next",
    command=next_question,
    bg="#38bdf8",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
).pack(pady=20)

# ---------------- RESULT PAGE ---------------- #

tk.Label(
    result_frame,
    text="QUIZ COMPLETED!",
    font=("Arial", 28, "bold"),
    fg="#22c55e",
    bg="#0f172a"
).pack(pady=40)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 20),
    fg="white",
    bg="#0f172a"
)

result_label.pack(pady=20)

tk.Button(
    result_frame,
    text="Restart",
    command=restart,
    bg="#38bdf8",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
).pack(pady=10)

tk.Button(
    result_frame,
    text="Exit",
    command=root.quit,
    bg="red",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
).pack(pady=10)
# ---------------- START APP ---------------- #
show_frame(login_frame)
root.mainloop()