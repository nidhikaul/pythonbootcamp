import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

#Check user answer 

count = 0
correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States", prompt="Name a state").title()
    print(answer_state)

    if answer_state =="Exit":
        missed_list = [state for state in all_states if state not in correct_guess]
        # missed_list = []
        # for state in all_states:
        #     if state not in correct_guess:
        #         missed_list.append(state)
        new_data = pandas.DataFrame(missed_list)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guess.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # correct_guess.append()





# missed_list.append(set(all_states).difference(set(correct_guess)))




#Populate the location of the state on the map
#Correct answer count out of 50







# screen.exitonclick()