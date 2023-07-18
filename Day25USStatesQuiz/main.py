import turtle
import pandas

# def get_mouse_click_coordinates(x, y):
#     print(x, y)

def main():
    image = "blank_states_img.gif"

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image)

    # Shows coords for clicked spot on screen.
    # turtle.onscreenclick(get_mouse_click_coordinates)
    # Keeps screen on.
    # turtle.mainloop()

    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's Another State's Name?").title()
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        if answer_state in all_states:
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            state_data = data[data.state == answer_state]
            state.goto(int(state_data.x), int(state_data.y))
            # state.write(answer_state)
            state.write(state_data.state.item())
            guessed_states.append(answer_state)


if __name__ == "__main__":
    main()
