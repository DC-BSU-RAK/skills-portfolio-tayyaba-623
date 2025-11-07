from tkinter import *
from tkvideo import tkvideo
from random import randint
from random import choice
from tkinter import messagebox
import pygame
root = Tk()
root.geometry("950x530")
root.title("Math Quiz")

Question = ""
answer = 0
Final_score = 0
Total_attempt = 0
Question_count = 0
Level = "Easy"

user_answer = StringVar()
# Adding background music
pygame.mixer.init()
pygame.mixer.music.load("Math Quiz/bg_music.mp3")    # Background music idea from youtube video (https://youtube.com/shorts/4s-3l-e3ONc?si=FoMeOMSy9V7Mnxzc)
pygame.mixer.music.play(loops=1)

# Function to play the sound for correct and wrong answer 
def bg_music(user_input):
   pygame.mixer.music.stop()
   if user_input == "Correct":
       pygame.mixer.music.load("Math Quiz/success.mp3")
       pygame.mixer.music.play()
   else:
       pygame.mixer.music.load("Math Quiz/wrong_answer.mp3")  
       pygame.mixer.music.play()

# Function to replay the background music 
def resume_backgroun_music():
    pygame.mixer.music.load("Math Quiz/bg_music.mp3")
    pygame.mixer.music.play(loops=-1)    

# Frame1 for the front page
def frame1():
   global frame_1
   frame_1 = Frame(root, width=950, height=530) # Height and width of the frame1
   frame_1.grid(row=0, column=0)

   lblVideo = Label(frame_1)
   lblVideo.grid(row=0, column=0, columnspan=2)
   player = tkvideo("Math Quiz/Front_video.mp4", lblVideo, loop=1, size=(960,540))
   player.play()

   Start_button = Button(frame_1, text="Start Quiz", font=("Arial", 12, "bold"), height=3, width=10, bg="orange", command=displayMenu)
   Start_button.place(relx=0.5, rely=0.64, anchor="center")

def displayMenu():
   frame_1.grid_forget()  # Hiding the frame1

   global frame_2
   frame_2 = Frame(root, width=950, height=530)
   frame_2.grid(row=0, column=0)

   lblVideo = Label(frame_2)
   lblVideo.grid(row=0, column=0, columnspan=2)
   player = tkvideo("Math Quiz/Menu.mp4", lblVideo, loop=1, size=(960,540))
   player.play()

   # Display title and level buttons
   Label(frame_2, text="LEVEL DIFFICULTY", font=("Verdana", 20, "bold"), bg="antique white").place(relx=0.5, rely=0.2, anchor="center")
   Button(frame_2, text="Easy", bg="orange", font=("Arial", 12, "bold"), command=lambda: level_intro("Easy"), width=15, height=3).place(relx=0.5, rely=0.4, anchor="center")
   Button(frame_2, text="Moderate", bg="orange", font=("Arial", 12, "bold"), command=lambda: level_intro("Moderate"), width=15, height=3).place(relx=0.5, rely=0.55, anchor="center")
   Button(frame_2, text="Advanced", bg="orange", font=("Arial", 12, "bold"), command=lambda: level_intro("Advanced"), width=15, height=3).place(relx=0.5, rely=0.7, anchor="center")

# Frame 3 for the level instructions
def level_intro(level):
    frame_2.grid_forget()

    global frame_3
    frame_3 = Frame(root, width=950, height=530)
    frame_3.grid(row=0, column=0)

    lblVideo = Label(frame_3)
    lblVideo.grid(row=0, column=0, columnspan=2)
    player = tkvideo("Math Quiz/intro.mp4", lblVideo, loop=1, size=(960,540))
    player.play()
    
    if level == "Easy":
       Level_intro = "In this level, you will get single-digit questions. You have two attempts for each questions. Answer correctly on the first try to earn 10 points. If you get it right on the second try, you will receive 5 points"
    elif level == "Moderate":
        Level_intro = "In this level, you will get two-digit questions. You have two attempts for each questions. Answer correctly on the first try to earn 10 points. If you get it right on the second try, you will receive 5 points"
    else:    
        Level_intro = "In this level, you will get four-digit questions. You have two attempts for each questions. Answer correctly on the first try to earn 10 points. If you get it right on the second try, you will receive 5 points"

    intro_box = LabelFrame(frame_3, text=f"{level} Instructions", font=("Verdana", 12, "bold"), bg="lemon chiffon", fg="black", bd=3, relief="ridge", padx=10, pady=10)
    intro_box.place(relx=0.5, rely=0.5, anchor="center", width=550, height=300)

    introduction_label = Label(intro_box, text=Level_intro, wraplength=450, font=("Verdana", 15), bg="lemon chiffon", justify="left")
    introduction_label.pack(anchor="n", fill=BOTH, pady=(10,0))
 
    continue_button = Button(frame_3, text="Start", bg="orange", font=("Verdana", 12, "bold"), command=lambda:select_level(level))
    continue_button.place(relx=0.5, rely=0.66, width= 100, height=60, anchor="center")


def select_level(level):
    global Level, question_label, question_number_label, user_input, button, score_label
    Level = level
    global frame_4
    frame_3.grid_forget()
    frame_4 = Frame(root, width=950, height=530)
    frame_4.grid(row=0, column=0)
    
    lblVideo = Label(frame_4)
    lblVideo.place(x=0, y=0, relwidth=1, relheight=1)
    player = tkvideo("Math Quiz/Menu.mp4", lblVideo, loop=1, size=(960,540))
    player.play()

    # Background box of the Quiz screen
    background_box = Label(frame_4, font=("Verdana", 12, "bold"), bg="lemon chiffon", fg="black", bd=3, relief="ridge", padx=10, pady=10)
    background_box.place(relx=0.5, rely=0.3, anchor="n", width=450, height=300)  

    heading_label = Label(frame_4, text="MATH QUIZ", font=("Verdana", 28, "bold"), bg="lemon chiffon")
    heading_label.place(x=360, y=70)

    question_number_label = Label(frame_4, text=f"Question: {Question_count}/10", font=("Verdana", 12, "bold"), bg="lemon chiffon")
    question_number_label.place(x=480, y=210, anchor="center")

    question_label = Label(frame_4, text="", font=("Verdana", 12, "bold"), bg="lemon chiffon", wraplength=400, justify="center")
    question_label.place(x=430, y=230)

    user_input = Entry(frame_4, textvariable=user_answer, font=("Verdana",12))
    user_input.place(x=400, y=270, width=150, height=30)

    button = Button(frame_4, text="Submit", font=("Verdana", 12, "bold"), bg="orange", command=isCorrect)
    button.place(x=430, y=330, width=100, height=40)

    score_label = Label(frame_4, text=f"Final Score: {Final_score}", font=("Verdana", 12, "bold"), bg="lemon chiffon")
    score_label.place(x=400, y=400)
    display_question()  # Call function to display questions

def randInt():
    if Level == "Easy":
        return randint(1,9)
    elif Level == "Moderate":
        return randint(10, 99)
    else:
        return randint(1000, 9999)
    
def decideoperation():
    return choice(["-", "+", "*", "/"])

def display_question():
    global number_1, number_2, operation, Final_score, answer, Total_attempt, Question_count, question_number_label

    Total_attempt = 1
    user_answer.set("")
    Question_count +=1

    score_label.config(text=f"Final score: {Final_score}")
    if Question_count > 10:
      Grade = grade(Final_score)
      messagebox.showinfo("Great quiz completed", f"Final score: {Final_score} /100 \nYour garde is: {Grade}") # Display result after completing 10 questions
      answer = messagebox.askyesno("Game completed", "Do you want to replay the game?")
      if answer:
          replay_game() # Call function to replay the game
          frame_4.grid_forget()   
          displayMenu()   # Display the level screen 
      else:
         root.destroy()
      return
    
    # Generating random questions
    number_1 = randInt()
    number_2 = randInt()
    operation = decideoperation()

    if operation == "-":
       answer = number_1 - number_2
    elif operation == "+":
        answer = number_1 + number_2
    elif operation == "*":
        answer = number_1 * number_2
    else:
        answer = number_1 / number_2
       
    Question = f"{number_1} {operation} {number_2} = ?"
    question_label.config(text=Question)
    question_number_label.config(text=f"Question: {Question_count}/10")
    score_label.config(text=f"Final score: {Final_score}")

# Function to check user answer
def isCorrect():
    global Final_score, Total_attempt, question_number_label
    
    if float(user_answer.get()) == answer:
        if Total_attempt == 1:
            Final_score += 10
            bg_music("Correct")
            messagebox.showinfo("Correct!", "Correct answer +10 points")  # The message box was created with the help of a class explanation
            resume_backgroun_music()
            display_question()
        else:
           Final_score +=5
           bg_music("Correct")
           messagebox.showinfo("Correct!", "Correct answer +5 points")
           resume_backgroun_music()
           display_question()

    else:     
         if Total_attempt == 1:
             bg_music("Wrong")
             messagebox.showwarning("Incorrect", "Incorrect answer. Try again")
             Total_attempt = 2
             resume_backgroun_music()
         else:
            bg_music("Wrong")
            messagebox.showerror("Incorrect", f"Correct answer is: {answer}")
            resume_backgroun_music()
            display_question()

# Function to check grades
def grade(score):
    if score >= 92:
         return "A+"
    elif score >= 82:
        return "A"
    elif score >= 72:
        return "B+"
    elif score >= 62:
        return  "B"
    elif score >= 52:
        return "C+"
    elif score >= 42:
        return "C"
    elif score >= 32:
        return"D+"
    elif score >= 22:
        return "D"
    else:
        return "F"

# Reset all variables to replay the game 
def replay_game():
    global Question, answer, Final_score, Total_attempt, Question_count, Level
    Question = "" 
    answer = 0
    Final_score = 0
    Total_attempt = 0
    Question_count = 0
    Level = "Easy"
    user_answer.set("")

frame1()
root.mainloop()