import turtle as t
import random

screen = t.Screen()
screen.setup(500, 400)


is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -100
for color in colors:
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, y)
    y = new_turtle.ycor() + 33.34
    all_turtles.append(new_turtle)

user_bet = screen.textinput("Make a bet", "Which the turtle will win ? enter a color: ")

for color_index in range(0, 5):
    if user_bet == colors[color_index]:
        is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win!, the turtle winner is {winning_turtle}")
            else:
                print(f"You lose, the turtle winner was {winning_turtle}")
        rand_move = random.randint(0, 10)
        turtle.forward(rand_move)
    

screen.exitonclick()


# turtles-race
