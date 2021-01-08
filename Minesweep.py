import random
import pyfiglet
from termcolor import colored
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
		"				           Code by shaan453\n",
		"                                          Version: 2021.3.2\n",
		"------------------------------------------------------------------------------")
def gameStart(playground, n):
	for i in range(n):
		for j in range(n):
			x = int(input("Enter the coordinate: x= "))
			y = int(input("Enter the coordinate: y= "))
			if playground[x][y] == 1:
				status = "Boom! Bomb have been blasts. You lose"
				print(colored(status,"red"))
				return False
			status = "No bomb, you are lucky this time"
			print(colored(status,"green"))
			if i == n-1 and j == n-1:
				status = "Congratulations! You won the game"
				print(colored(status,"green"))
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
