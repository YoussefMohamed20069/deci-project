# Import the important packages
import time
import random


def play_again():
	"""
	This function will start when the game end and it will ask the player if he want to play again or not
	"""
	print_pause("GAME OVER")

	want = input("Would you like to play again? (y/n)")


	while want.upper() != "Y" and want.upper() != "N":
		want = input("Would you like to play again? (y/n)")

	if want.upper() == "Y":
		return True
	else:
		return False

def print_score(score):
	print_pause(f"Your Score is {score}")

def print_pause(msg):
	"""
		This function will take the text we will output and print it then wait 2 seconds before print anything else
	"""
	print(msg)
	#time.sleep(2)

def int_input():
	"""
		This function will take the input from the user and check if it valid and then wait for 2 seconds
	"""
	# Define the variable that will store the input
	choice = int(input("(Please enter 1 or 2)"))

	# Check if the input is valid
	while (choice != 1 and choice != 2):
		choice = int(input("(Please enter 1 or 2)"))

	# Return the input to use it in other functions
	return choice



def choose(choice1, choice2):
	"""
		This function will take the two possible choices that the player could choose from and output it to the user
		and then check if the choice is right and then return his choice to the main function to use it.
	"""
	# Output the choices for the user
	print_pause("Enter 1 to " + choice1)
	print_pause("Enter 2 to " + choice2)

	# Ask the user to give you his choice
	print_pause("What would you like to do?")

	# Define the variable that you will store the user choice in
	choice = int_input()

	# Return the choice variable to use in other functions
	return choice


def win_condition(score):
	if score >= 5:
		winning()
	else:
		losing()


def winning():
	"""
	This function will work to check if the user won or no
	"""

	print_pause("Congratualtions. You find your way finally.")
	print_pause("You Won!")

def losing():
	"""
	This function will work if the player lost
	"""

	print_pause("You Lost!")

def go_help(score):
	"""
		This function will work if the player chooses to go help the man
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	# A list of animals and weapons
	animals = ["brown bear", "lion", "wolf", "tiger"]
	weapons = ["gun", "knife", "sword"]

	# Choose an animal randomly
	animal = random.choice(animals)

	# Choose an weapon randomly
	weapon = random.choice(weapons)

	print_pause(f"There is a {animal} attacking the man and will kill him.")
	print_pause(f"you have a {weapon} with you and some meat.")

	# Identify the choices
	choice1 = f"Fight the {animal} with your {weapon}."
	choice2 = "Give him the meet."

	# make the user choose
	choice = choose(choice1, choice2)

	# Use the choice to continue the story
	if choice == 1:
		fight(score, animal)
	else:
		give_meat(animal)

def go_away():
	"""
		This function will work if the player chooses to run away
	"""

	# List of animals
	animals = ["brown bear", "lion", "wolf", "tiger"]

	# Choose the animal randomly
	animal = random.choice(animals)

	print_pause(f"When you were running away from the voice a {animal} sees you.")
	print_pause("It killed you.")

	losing()


def fight(score, animal):
	"""
		This function will work if the user chooses to fight the bear
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause(f"Good Job fighting the {animal}.")
	print_pause(f"now the {animal} died.")
	print_pause("You can use its meat for food for a long period of time.")


	#Identify the two choics for the user
	choice1 = "Give up about getting out of the forest and live with the man."
	choice2 = "Continue your Journey to get out of the forest."

	# Make the player choose
	choice = choose(choice1, choice2)

	# Use the choice to continue the story
	if choice == 1:
		give_up(score, animal)
	else:
		continue_journey(score)

def continue_journey(score):
	"""
		This function will work if the user continued his journey to get out of the forest.
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause("Good Job not giving up.")
	print_pause("now after a long time you have a crossroads.")

	# Get the choice from the user
	choice = choose("Go Left.", "Go Right.")


	# Use the choice to continue the story
	if choice == 1:
		go_left(score)
	else:
		go_right()

def give_up(score, animal):
	"""
	This function will work when the user decides that he wants to stay in the forest
	"""

	print_pause(f"When the {animal} attacked the man the crops.")
	print_pause("we haven't enough water to plant.")


	# Identify the choices that the user has
	choice1 = "Use the water you have for the process."
	choice2 = "Go in an adventure to get a resource of water."

	# Make the user choose what to do
	choice = choose(choice1, choice2)

	# Use the choice to continue the story
	if choice == 1:
		use_water()
	else:
		find_water(score)

def give_meat(animal):
	"""
		This function will work if the user chooses to give the animal the meat
	"""
	print_pause(f"The {animal} ate the meat and then go away.")
	print_pause("You don't have food so you die starving.")

def go_left(score):
	"""
		This function will work if the player chooses to go left
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause("Congratulations you did it out of the forest.")
	print_pause("you find a rescue team that get you in town.")
	print_pause("you get back to your home.")
	
	# Identify the choices of the player
	choice1 = "Tell them about the man."
	choice2 = "Don't tell them."

	# Make the player choose
	choice = choose(choice1, choice2)

	if choice == 1:
		tell(score)
	else:
		not_tell(score)

	return score


def tell(score):
	"""
	This function will work if the user wanted to tell the rescue team about the man.
	"""
	score += 1

	print_pause("You Told them.")
	print_pause("They gone and rescue the man.")

	# Check if the player won
	win_condition(score)

def not_tell(score):
	print_pause("You didn't tell them.")
	print_pause("You continued your life normally.")

	# Check if the player won
	win_condition(score)

def go_right():
	"""
		This function will work if the player chooses to go right
	"""

	print_pause("There is a lot of snakes that bite you with there venom.")
	print_pause("You died.")

	losing()


def use_water():
	"""
		This function will work if the user decided to use the water he has to plant the crops
	"""

	print_pause("You used all of your water for the plants")
	print_pause("now you has no water and you died.")

	losing()


def find_water(score):
	"""
		 This function will work if the user decided to go find a water resource.
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause("You Find a river far from the house.")

	# Identify the user 2 choices
	choice1 = "make a canal between your field and the river."
	choice2 = "Memorize the place of the river to get for water."

	# Make the user choose what to do
	choice = choose(choice1, choice2)


	# Use the choice to continue the story
	if choice == 1:
		make_canal(score)
	else:
		memorize_place(score)


def make_canal(score):
	"""
		This function will work if the player chooses to make a canal from the river to the house
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause("The Man Suggests to make an animal farm to secure the food.")

	# Make the user choose what to do
	choice = choose("Agree with him.", "Don't Agree with him.")


	# Use the user choice to continue the story
	if choice == 1:
		agree(score)
	else:
		disagree()


def memorize_place(score):
	"""
		This function will work if the player chooses to just memorize the place of the river to back from time to time.
	"""
	print_pause("The Man Suggests to make an animal farm to secure the food.")


	# Make the user choose what to do
	choice = choose("Agree with him.", "Don't Agree with him.")

	# Use the user choice to continue the story
	if choice == 1:
		agree(score)
	else:
		disagree()


def agree(score):
	"""
		This function will work if the player agreed with the man suggestion
	"""

	# Give the player information about his score
	print_score(score)

	# This array contain some colors
	colors = ['red', 'yellow', 'green', 'purple']

	# choose the color of the herbs randomly
	color = random.choice(colors)

	print_pause("You made the farm with the man.")
	print_pause("You secured your food for a long time.")
	print_pause("You Lived in the forest and the man helped you a lot.")
	print_pause("but now the man is getting sick.")
	print_pause(f"he need some {color} herbs as a cure for his sickness.")


	# Identify the two choices that the user has
	choice1 = f"Find the {color} Herbs."
	choice2 = "Just continue your work and leave him die."

	# Make the user choose what to do
	choice = choose(choice1, choice2)

	# Use the user choice to continue the story
	if choice == 1:
		find_herbs(score)
	else:
		just_work()

def disagree():
	"""
		This function will work if the player disagreed with the man suggestion
	"""
	print_pause("The man kicked you out of his house.")
	print_pause("You get to the forest without food or water.")
	print_pause("You died starving afterward.")
	
	losing()

def find_herbs(score):
	"""
	This function will work if the player wants to help the man.
	"""

	# Add the new score and print it
	score += 1

	print_score(score)

	print_pause("Good Job. The man is now fine.")
	print_pause("You continued working until you secured your food.")
	print_pause("Now you can live in the forest for a long time.")
	print_pause("The man became your best friend and you lived together.")

	# Check if the player won
	win_condition(score)

	# Check if the player won
	return score


def just_work():
	"""
		This function will work if the player wants to leave the man die
	"""

	print_pause("The Man died.")
	print_pause("you continued your work.")
	print_pause("but you won't be able to do the work alone in the right time")
	print_pause("you died starving before you continue your work.")

	losing()

# Define the main function that will contain the game main loop
def main():

	run = True
	

	while run:
		# The variable that stores the score of the player
		total_score = 0

		# Describe to the player what happens
		print_pause("You're lost in a forest.")
		print_pause("You want to find your way out.")
		print_pause("You heard a sound of a man that wants anyone to help him")

		# Give the user the first two choices and get his choice
		choice = choose("Go help him.", "Run away from the voice.")

		# Check the choice of the player
		if choice == 1:
			go_help(total_score)
		else:
			go_away()

		# After the game ended see if the player wants to play again or no
		run = play_again()



# Start the game
if __name__ == "__main__":
	main()
