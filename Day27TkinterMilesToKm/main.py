from tkinter import *

def calculate():
    miles = float(input.get())
    km = round(miles * 1.609344, 2)
    kilometers.config(text=f"{km}")


def main():
    window = Tk()
    window.title("Miles to Kilometers")
    window.minsize(width=200, height=80)
    window.maxsize(width=200, height=80)
    window.config(padx=5, pady=0)

    miles_label = Label(text="Miles", font=("Arial", 12))
    miles_label.grid(column=2, row=0)

    is_equal_to = Label(text="is equal to", font=("Arial", 12))
    is_equal_to.grid(column=0, row=1)

    km = Label(text="Km", font=("Arial", 12))
    km.grid(column=2, row=1)

    global kilometers # Setting to global due to lack of button command parameter allowance
    kilometers = Label(text="0", font=("Arial", 12))
    kilometers.grid(column=1, row=1)

    button = Button(text="Click Me", command=calculate)
    button.grid(column=1, row=2)


    # Create an Entry
    global input
    input = Entry(width=10)
    input.grid(column=1, row=0)



    # Loops window to stay open
    window.mainloop()

if __name__ == "__main__":
    main()