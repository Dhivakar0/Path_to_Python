import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_states = []
# states_to_learn = []

data = pd.read_csv("50_states.csv")
states = (data["state"]).to_list()

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="Name any state of U.S.A.").title()
    if answer_state == "Exit":
        # for state in states:
        #     if state not in correct_states:
        #         states_to_learn.append(state)
        # states_not_know = pd.DataFrame(states_to_learn, columns = ["state"])
        # states_not_know.to_csv("states_to_learn.csv",index=False)
        # break
        states_to_learn = [state for state in states if state not in correct_states]
        states_to_know = pd.DataFrame(states_to_learn, columns = ["state"])
        states_to_know.to_csv("states_to_learn_list_comp.csv",index=False)
        break
    if answer_state in states and answer_state not in correct_states:
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_data = data[data["state"] == answer_state]
        state_turtle.goto(state_data.x.item(),state_data.y.item())
        state_turtle.write(arg=answer_state)
        correct_states.append(answer_state)





























screen.exitonclick()
