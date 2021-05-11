def twoChoices():
    print('yes')
	print('no')

def main():

	twoChoices=input("Hello, welcome to the chess club. Are you interesting in joining?")

	if(twoChoices == 'yes'):
		print("Ok, please stay tuned for the three requirements.")
	elif(twoChoices == 'no'):
		print("Ok have a nice day.")
	else:
		print("invalid entry")
	
	age=int("How old are you?")
	if(age >= 15):
		print("You are eligibile to join if you meet two more requirements.")
	elif(age < 15):
		print("Sorry, but you are not old enough to join this club yet.")
		
	gpa = float("What is your gpa?")
	if(gpa >= 3.75):
		print("You are eligible to join if you meet one more requirement.")
	elif(gpa < 3.75):
		print("Sorry but you are ineligible to join.")
		
	yearsExperience = int("How many years of experience do you have in chess?")
	if(yearsExperience >= 2):
		print("You are now officially a member of this club! Welcome aboard!")
	elif(yearsExperience < 2):
		print("Sorry you are ineligible to join the club.")

main()
