import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states_data = pandas.read_csv("50_states.csv")
all_us_states = us_states_data.state.to_list()
guessed_states = []
missing_states = []

guessed_states_count = 0
while guessed_states_count < len(all_us_states):
    answer_state = screen.textinput(title=f"{guessed_states_count}/50Guess the State", prompt="What's another stat's name?").title()
    if answer_state == "Exist":
        missing_states = [state for state in all_us_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_us_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_states_data[us_states_data["state"] == answer_state]
        t.goto(x=state_data.x.item(), y=state_data.y.item())
        t.write(answer_state)
        guessed_states_count += 1

for state in missing_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("red")
    state_data = us_states_data[us_states_data["state"] == state]
    t.goto(x=state_data.x.item(), y=state_data.y.item())
    t.write(state)

turtle.mainloop()
