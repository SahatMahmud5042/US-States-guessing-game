import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")

states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Your guess?").title()

    if ans_state == "Exit":
        break

    if ans_state in states:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)
        states.remove(ans_state)


missed_states = pd.DataFrame(states)

missed_states.to_csv("missed_states.csv")



