import tkinter
from tkinter import Canvas, PhotoImage

# ********************* CONSTANTS ************************* #
YELLOW = "#f7f5dd"
FONT_NAME = "Bebas Neue"

# *********** GUI ************** #
window = tkinter.Tk()
window.title("Typing Speed Test")
canvas = Canvas(width=600, height=600, bg=YELLOW, highlightthickness=0)
speed_img = PhotoImage(file="speed-test.png")
canvas.create_image(100, 112, image=speed_img)
canvas.create_text(475, 130, text="Speed Test", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.create_text(340, 300, fill="white", font=("Courier", 11, "bold"),
                   text="A weary mother returned from the store,Lugging groceries\n"
                                  "through the kitchen door. Awaiting her arrival was her \n"
                                  "8 year old son, Anxious to relate what his younger \n"
                                  "brother While I was out playing and Dad was on a call,\n"
                                  "had done. T.J. took his crayons and wrote on the wall\n"
                                  "It's on the new paper you just hung in the den.\n"
                                  "I told him you'd be mad at having to do it again.\n"
                                  "She let out a moan and furrowed her brow,\n"
                                  "Where is your little brother right now?\n"
                                  "She emptied her arms and with a purposeful stride,\n"
                                  "She marched to his closet where he had gone to hide.\n"
                                  "She called his full name as she entered his room.\n"
                                  "He trembled with fear--he knew that meant doom\n"
                                  "For the next ten minutes, she ranted and raved.\n")
canvas.pack()

# *********** PROGRAM *********** #
text_list = []
entry = tkinter.Entry(width=50)


def start():
    entry.place(x=265, y=450)
    window.after(6000, submit)


def submit():
    entry.config(state="disabled")
    text_entered = entry.get()
    for text in text_entered:

        text_list.append(text)
    cpm = len(text_list)
    wpm = cpm/5
    canvas.create_text(325, 30, text=f"Your cpm is {cpm} and wpm is {wpm}", fill="white", font=(FONT_NAME, 30, "bold"))

# *********** GUI *********** #


start_button = tkinter.Button(text="Start", command=start)
start_button.place(x=200, y=480)

entry_button = tkinter.Button(text="Submit", command=submit)
entry_button.place(x=265, y=480)

window.mainloop()
