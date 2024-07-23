import turtle
import pandas

# setting up the screen
screen = turtle.Screen()
# screen.setup(width = 725, height = 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  # creating the turtle screen to be the map

# Extracting information
us_states = pandas.read_csv("50_states.csv")

# necessary variables for the game
all_states = us_states.state.to_list()
guessed_states = []
try:
	while len(guessed_states) <= 50:
		# asking the user to make guess by entering US State name
		answer = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
								  prompt = "What is another state's name").title()

		# allowing the user to exit by typing the 'Exit' in the input box and ending the game
		if answer == "Exit":
			missing_states = [state for state in all_states if state not in guessed_states]
			missing_data = pandas.DataFrame(missing_states)
			missing_data.to_csv("States_to_study.csv")
			print(f"{len(missing_data)} more states you can study")
			break

		# checking if the user guess is correct or not
		# if its correct drawing it to map at its coordinates
		# adding the answer to guessed_states
		if answer in all_states:
			guessed_states.append(answer)
			state = us_states[us_states.state == answer]
			t = turtle.Turtle()
			t.penup()
			t.hideturtle()
			t.goto(x = int(state.x.iloc[0]), y = int(state.y.iloc[0]))
			t.write(answer)  # , align = "center", font = ('Arial', 10, 'normal')
# closing the screen when needed
# print(guessed_states)
# turtle.mainloop()
except Exception as e:
	pass
