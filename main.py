import turtle
import pandas as pd

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
states_list = us_data["state"].to_list()
correct_guesses = 0
guessed_states = []

while correct_guesses <= len(states_list):
    #Prompt user to input any U.S. states name:
    guess_state = screen.textinput(title=f"{correct_guesses}/{len(states_list)} States Correct",
                                   prompt="Please enter a state name:").title()

    #Gives user an Exit prompt to exit the game and generate a csv file with all the missing states.
    if guess_state == "Exit":
        text.goto(0, 0)
        text.write(f"Thank you for playing!", align="center", font=("Arial", 24, "normal"))
        # Extract missing states into a csv file
        missing_states = [state for state in states_list if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv(f"list_of_{len(missing_states)}_missed_states.csv")
        break

    #Compare the input to the U.S. states data list for a match.
    for state in states_list:
        if guess_state == state:
            # When a match is found, get the coordinates from the file and place the state name at that location
            state_data = us_data[us_data["state"] == guess_state]
            state_coord = (state_data["x"].item(), state_data["y"].item())
            text.goto(state_coord)
            text.write(f"{state}", align="center", font=("Arial", 7, "normal"))
            guessed_states.append(state)
            correct_guesses += 1

    #Terminate the game once all the states are filled in.
    if correct_guesses == len(states_list):
        text.goto(0,0)
        text.write(f"Congratulations! You named all the 50 U.S. States!", align="center", font=("Arial", 24, "normal"))
        break