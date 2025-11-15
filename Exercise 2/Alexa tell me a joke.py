from tkinter import *
from tkvideo import tkvideo
import pygame

root = Tk()
root.geometry("920x700")
root.title("Alexa tell me a joke")
root.iconbitmap("Exercise 2/icon.ico")

# background music
pygame.mixer.init()
pygame.mixer.music.load("Exercise 2/background.mp3")
pygame.mixer.music.play(-1)

# Laughing sound for punchline button
laughing_music = pygame.mixer.Sound("Exercise 2/laughing.mp3")

# Text animation
class text_animation:
    def __init__(self, label, text, delay=100):     # This text animation is added by self study through a YouTube video (https://youtu.be/PumkwKsPoM4?si=1a6kvDGthDrYQb4j)
        self.label = label
        self.text = text
        self.delay = delay
        self.index = 0
        self.animation()

    def animation(self):
      if self.index < len(self.text):
        self.label.config(text=self.text[:self.index +1])
        self.index +=1
        self.label.after(self.delay, self.animation) 

# Frame 1 (Front screen)
def front_Screen():
   global frame_1
   frame_1 = Frame(root, width=900, height=970)
   frame_1.grid(row=0, column=0)

   lblVideo = Label(frame_1)
   lblVideo.grid(row=0, column=0, columnspan=2)
   player = tkvideo("Exercise 2/joke.mp4", lblVideo, loop=1, size=(920,970))
   player.play()

   # Start Joke Button
   Start_button = Button(frame_1, text="Start joke", font=("Georgia", 25, "bold"), height=2, width=10, bg="#0066FF", fg="black", command=Home_Page)
   Start_button.place(relx=0.5, rely=0.55, anchor="center")

# Frame 2 (Joke screen)
def Home_Page():
   global frame_2, jokes, text_box_1, text_box_2 
   frame_2 = Frame(root, width=920, height=970)
   frame_2.grid(row=0, column=0)
   
   # background video 
   lblVideo = Label(frame_2)
   lblVideo.grid(row=0, column=0, columnspan=2)
   player = tkvideo("Exercise 2/joke_video.mp4", lblVideo, loop=1, size=(920,970))
   player.play()
   
   jokes = readFile()

   # Heading label
   heading = Label(frame_2, text="JOKE TIME / FUN TIME", font=("Georgia", 25, "bold"), fg="#0066FF", bg="yellow", justify="center")
   heading.place(relx=0.57, rely=0.1, anchor="center")

   # Label for setup
   text_box_1 = Label(frame_2, wraplength=600, font=("Georgia", 15, "bold"), bg="yellow", highlightbackground="black", justify="center", height=3)
   text_box_1.place(relx=0.55, rely=0.2, anchor="center")

   # Label for punchline
   text_box_2 = Label(frame_2, wraplength=600, font=("Georgia", 15, "bold"), bg="yellow", highlightbackground="black", justify="center", height=3)
   text_box_2.place(relx=0.55, rely=0.32, anchor="center")

   # Joke button
   button = Button(frame_2, text="Alexa tell me a joke", font=("Georgia", 15, "bold"), bg="#0066FF", fg="white", command=display_joke, width=20, height=2)
   button.place(relx=0.41, rely=0.43, anchor="center")

   # punchline button
   punch_button = Button(frame_2, text="Show punchline", font=("Georgia", 15, "bold"), bg="#0066FF", fg="white", command=display_punchline, width=20, height=2)
   punch_button.place(relx=0.75, rely=0.43, anchor="center")

   # New joke button
   new_joke_button = Button(frame_2, text="Next joke", font=("Georgia", 15, "bold"), bg="#0066FF", fg="white", command=new_joke, width=20, height=2)
   new_joke_button.place(relx=0.41, rely=0.54, anchor="center")

   # Button to quit the joke screen
   quit_button = Button(frame_2, text="Quit", font=("Georgia", 15, "bold"), bg="#0066FF", fg="white", command=root.destroy, width=20, height=2)
   quit_button.place(relx=0.75, rely=0.54, anchor="center")

# Function to read from file
def readFile():
   jokes = []
   with open('Exercise 2/joke.txt', 'r') as file:
        for joke_line in file:
           joke_line = joke_line.strip()
           if not joke_line:
              continue
           if '?' in joke_line:
            setup, punchline = joke_line.split("?", 1)
            jokes.append((setup.strip() + "?", punchline.strip()))
        else:
             jokes.append(("Here's a joke!", joke_line))
        return jokes
   
joke_number = 0
jokes = readFile()

# Function to display joke
def display_joke():
   global joke_number, jokes, text_box_1, text_box_2
   setup, _ = jokes[joke_number]
   text_box_2.config(text="")
   text_animation(text_box_1, setup, delay=60)

# Function to display punchline
def display_punchline():
   global joke_number, text_box_2
   _, punchline = jokes[joke_number]
   text_animation(text_box_2, punchline, delay=60)
   laughing_music.play()

# Function to display new joke
def new_joke():
   global joke_number, jokes, text_box_1, text_box_2
   joke_number +=1
   if joke_number >= len(jokes):
      joke_number = 0
   setup, _ = jokes[joke_number]
   text_box_2.config(text="")
   text_animation(text_box_1, setup, delay=60)

front_Screen()
root.mainloop()


     