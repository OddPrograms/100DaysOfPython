from tkinter import *

def button_clicked():
    new_label = input.get()
    my_label["text"] = new_label
    my_label.config(text=new_label)


def main():
    # Creates a Tkinter GUI Window
    window = Tk()
    # Sets window title
    window.title("My First GUI Program")
    # Sets window size
    window.minsize(width=500, height=300)
    # window.maxsize(width=500, height=300)

    # Forces centered behavior
    # window.grid_columnconfigure((0, 1, 2), weight=1)

    # Padding
    # window.config(padx=100, pady=50)

    # Create a Label
    global my_label # Setting to global due to lack of button command parameter allowance
    my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))
    # Places object into window
    # my_label.pack(side="top")

    # Places based on specific coordinates
    # my_label.place(x=170, y=0)

    my_label.grid(column=0, row=0)


    my_label["text"] = "New Text"
    my_label.config(text="New Text")


    # Create a Button
    button = Button(text="Click Me", command=button_clicked)
    # Places object into window
    # button.pack()
    button.grid(column=1, row=1)

    button_two = Button(text="New Button")
    button_two.grid(column=3, row=0)


    # Create an Entry
    global input
    input = Entry(width=10)
    # input.pack()
    input.grid(column=4, row=2)



    # Loops window to stay open
    window.mainloop()

if __name__ == "__main__":
    main()