import customtkinter as ct
import random

colours = ['Red', 'Blue', 'Green', 'Grey','Yellow', 'Orange',
           'Purple',"Pink","White","Maroon"]
score = 0
time_left = 20
color_used = []
text_used = []
text_color = ""
text = ""
time_loop = None


def select():
    global text, text_color, text_used, color_used
    text_color = random.choice(colours)
    while text_color in color_used:
        text_color = random.choice(colours)

    text = random.choice(colours)
    while text in text_used and text == text_color:
        text = random.choice(colours)


def reset():
    global score, time_left, color_used, text_used, text, text_color
    score = 0
    time_left = 30
    color_used = []
    text_used = []
    text_color = ""
    text = ""
    countdown()
    select()

    scoreLabel.configure(text=f"Score : {score}")
    label.configure(text=text, text_color=text_color)


def popup():
    top = ct.CTkToplevel(root)
    top.geometry("200x100+420+130")
    top.configure(bg="black")

    def response():
        top.destroy()
        reset()

    def close():
        root.destroy()

    top.protocol("WM_DELETE_WINDOW", close)
    b = ct.CTkButton(top, text="Play Again ?",
                     text_font="cambria 10 bold", fg_color="yellow",
                     cursor="hand2", command=response)
    b.pack(pady=30)


def countdown():
    global time_left, time_loop
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text="Time left: "
                              + str(time_left))

        # run the function again after 1 second.
        time_loop = timeLabel.after(1000, countdown)
    else:
        root.after_cancel(time_loop)
        popup()


def check_valid(e):
    global text_color, score
    widget = e.widget
    guess = widget.get()
    print("guess : ", guess.lower())
    print("text_color : ", text_color.lower())
    print("-------------------------")

    if guess.lower() == text_color.lower():
        score += 1
        scoreLabel.configure(text=f"Score : {score}")
        select()
        label.configure(text=text, text_color=text_color)
        widget.delete("0", "end")


select()

root = ct.CTk()
root.configure(bg="black")

# set the title
root.title("COLORGAME")
root.geometry("375x200+340+130")

instructions = ct.CTkLabel(root, text="Type in the colour of the words,"
                                      " and not the word text!",
                           text_color="white",text_font="cambria 10 bold")
instructions.pack()

scoreLabel = ct.CTkLabel(root, text="Score : ",
                         text_color="green",
                         text_font="cambria 10 bold")
scoreLabel.pack()

timeLabel = ct.CTkLabel(root, text="Time left: " +str(time_left),
                        text_font="cambria 10 bold",
                        text_color="Magenta")

timeLabel.pack()

label = ct.CTkLabel(root, text_font="cambria 15 bold",
                    text=text, text_color=text_color)
label.pack()

e = ct.CTkEntry(root)
e.pack()
e.bind("<Return>", check_valid)

countdown()

root.mainloop()
