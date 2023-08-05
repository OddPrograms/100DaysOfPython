from tkinter import *
import requests

def get_joke():
    #Write your code here.
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
    response.raise_for_status()
    data = response.json()
    joke = data["joke"]
    canvas.itemconfig(joke_text, text=joke)

window = Tk()
window.title("This should make you laugh.")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
joke_text = canvas.create_text(150, 207, text="Joke Goes HERE", width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

laughing_crying_face = PhotoImage(file="face_with_tears.png")
joke_button = Button(image=laughing_crying_face, highlightthickness=0, command=get_joke)
joke_button.grid(row=1, column=0)

window.mainloop()
