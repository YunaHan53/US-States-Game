import turtle
import pandas as pd

is_playing = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a new turtle to write text for name of state
text = turtle.Turtle()
text.penup()
text.hideturtle()

#Read the 50_states.csv file and extract the state names
us_data = pd.read_csv("50_states.csv")
states = us_data["state"].to_list()
correct_guess = 0

while correct_guess <= len(states):
    #Prompt user to input any U.S. states name:
    guess_state = screen.textinput(title=f"{correct_guess}/{len(states)} States Correct",
                                   prompt="Please enter a state name:").title()

    #Compare the input to the U.S. states data list for a match.
    for state in states:
        if guess_state == state:
            # When a match is found, get the coordinates from the file and place the state name at that location
            state_data = us_data[us_data["state"] == guess_state]
            state_coord = (state_data["x"].item(), state_data["y"].item())
            text.goto(state_coord)
            text.write(f"{state}", align="center", font=("Arial", 7, "normal"))
            correct_guess += 1

    #Terminate the game once all the states are filled in.
    if correct_guess == len(states):
        text.goto(0,0)
        text.write(f"Congratulations! You named all the 50 U.S. States!", align="center", font=("Arial", 24, "normal"))
        is_playing = False
        break


screen.exitonclick()