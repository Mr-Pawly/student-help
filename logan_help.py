# Logan Welch
# 6.03 Project: Hangman Game
# 5/4/21 
 
import turtle
import random
 
def drawGallows(t):
 
	t.color = ("black")
	t.setpos(100, 0)
	t.left(180)
	t.forward(100)
	t.backward(50)
	t.right(90)
	t.forward(150)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(35)
	t.hideturtle()
		
def drawHead(t):
 
	t.color = ("black")
	t.penup()
	t.setpos(-10, 105)
	t.pendown()
	t.circle(10)
	t.hideturtle()
 
def drawBody(t):
 
	t.color = ("black")
	t.penup()
	t.setpos(0, 95)
	t.pendown()
	t.forward(45)
	t.hideturtle()
	
def drawArms(t):
 
	t.color = ("black")
	t.penup()
	t.setpos(0, 90)
	t.pendown()
	t.right(45)
	t.forward(20)
	t.penup()
	t.setpos(0, 90)
	t.pendown()
	t.left(90)
	t.forward(20)
	t.hideturtle()
	
def drawLegs(t):
 
	t.color = ("black")
	t.penup()
	t.setpos(0, 50)
	t.pendown()
	t.right(90)
	t.forward(25)
	t.penup()
	t.setpos(0, 50)
	t.pendown()
	t.left(90)
	t.forward(25)
	t.hideturtle()
 
def main():
 
    gex = turtle.Turtle()
	gex.speed(50)
	
    games = ["MINECRAFT", "SKYRIM", "HALO", "TETRIS", "HOLLOW KNIGHT", "OCARINA OF TIME", "SUPER MARIO ODYSSEY"]
	
	games[0] = "Burger Racing"
	print(games)
	hiddenWord = random.choice(games)
	input(hiddenWord)
	
	guess = input("pick a letter")
	if guess in hiddenWord:
	    print("wow")
	
	
	#hidden word is chosen
	#find length of hidden word
	#generate underscore version of the word
	#Display underscore version of the word
	#user guesses letter
	#if 
	drawGallows(gex)
	
	
	
	drawHead(gex)
	drawBody(gex)
	drawArms(gex)
	drawLegs(gex)
	
	
	
main()
