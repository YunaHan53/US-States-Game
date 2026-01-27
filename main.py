import turtle
import pandas as pd

is_playing = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Create a new turtle to write text for name of state
write_text = turtle.Turtle()
write_text.penup()
write_text.color("black")
write_text.hideturtle()

#Read the 50_states.csv file and extract the coordinates
us_data = pd.read_csv("50_states.csv")
states = us_data["state"]

guessed_state_coord = {}
correct_guesses = 0

while correct_guesses <= len(states):
    #Prompt user to input any U.S. states name:
    guess_state = screen.textinput(f"{correct_guesses}/{len(states)} States Correct","Please enter a state name:").title()

    #Compare the input to the U.S. state data list for a match.
    for state in states:
        if state == guess_state:
            # When a match is found, get the coordinates from the 50_states.csv file and place the state name at that location
            state_coordinates = us_data.loc[us_data["state"] == state]
            guessed_state_coord[state] = (state_coordinates["x"].values[0], state_coordinates["y"].values[0])
            # print(guessed_state_coord[state])
            write_text.goto(guessed_state_coord[state])
            write_text.write(f"{state}", align="center", font=("Arial", 8, "normal"))
            correct_guesses += 1

    #Terminate the game once all the states are filled in.
    if correct_guesses == len(states):
        write_text.goto(0,0)
        write_text.write(f"Congratulations! You named all the 50 U.S. States!", align="center", font=("Arial", 24, "normal"))
        is_playing = False
        break


screen.exitonclick()