import random
import pyfiglet
def Play():
	n = int(input("Enter the n: "))
	playground = generatingGround(n)
	playground = readyGround(playground, n)
	result = gameStart(playground, n)
def readyGround(playground, n):
	i = 0
	if i < n + 1:
		playground[random.randint(0,n-1)][random.randint(0,n-1)] = 1
		i += 1
	print("Ground is ready for dig")
	return playground

def generatingGround(n):
	ground = [[0]*n]*n
	if ground == None:
		return generatingGround(n)
	else: 
		print("Ground have been created")
		return ground
def banner():
	print("------------------------------------------------------------------------------",
		pyfiglet.figlet_format("Minesweeper"),
		"				Code by shaan453\n",
		"------------------------------------------------------------------------------")
def gameStart(playground, n):
	for i in range(n):
		for j in range(n):
			x = int(input("Enter the coordinate: x= "))
			y = int(input("Enter the coordinate: y= "))
			if playground[x][y] == 1:
				print("Boom! Bomb have been blasts. You lose")
				return False
			print("No bomb, you are lucky this time")
			if i == n-1 and j == n-1:
				print("Congratulations! You won the game")
				return True


def Menu():
	banner()
	print("1. Play\n2. Exit")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		Play()

	elif choice == 2:
		exit()
	else:
		exit()

Menu()
