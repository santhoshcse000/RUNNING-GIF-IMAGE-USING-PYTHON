import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk, ImageSequence
import speech_recognition as sr
import threading

# Initialize the main application window
root = tk.Tk()
root.title("Personal Voice Assistant")
root.geometry("500x500")

# Load the GIF
gif_path = "LEXI DESIGN.gif"  # Replace with your GIF file path
gif = Image.open(gif_path)

# Create a Label widget to display the GIF
lbl = Label(root)
lbl.pack()

def animate_gif():
    # Function to animate GIF
    for img in ImageSequence.Iterator(gif):
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        lbl.image = img
        lbl.update()
        root.after(100)  # Adjust speed here

def listen():
    # Function to listen for voice commands
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            # Add your command handling logic here
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")

# Run the GIF animation in a separate thread
gif_thread = threading.Thread(target=animate_gif)
gif_thread.start()

# Run the voice assistant in a separate thread
voice_thread = threading.Thread(target=listen)
voice_thread.start()

# Run the main application loop
root.mainloop()
