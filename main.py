import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states.txt")
# print(data)
data_lst = data.state.to_list()
guess_lst = []
missing_states = []
score = 0
# print(state_row, state,x_value,y_value)
while score <= 50:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="What's the state name?").title()
    if guess == "Exit":
        for states in data_lst:
            if states not in guess_lst:
                missing_states.append(states)
        # print(missing_states)
        # with open("missing_states.txt", "w") as missing_file:
        #     missing_file.write(str(missing_states))
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("States_to_learn.csv")
        break
    if guess in data_lst:
        guess_lst.append(guess)
        state_row = data[data.state == guess]
        x_value = int(state_row.x)
        y_value = int(state_row.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_value, y_value)
        t.write(guess)
        score += 1

