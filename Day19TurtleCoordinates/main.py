from turtle import Turtle, Screen
import random

def main():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    turtle_list = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]

    for turtle_index in range(0, 6):
        new_racer = Turtle(shape="turtle")
        new_racer.color(colors[turtle_index])
        new_racer.penup()
        new_racer.goto(x=-230, y=y_positions[turtle_index])
        turtle_list.append(new_racer)

    user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")


    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")


            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


    screen.exitonclick()

if __name__ == "__main__":
    main()