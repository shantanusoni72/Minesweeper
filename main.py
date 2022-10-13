from minesweeper import *

if __name__ == '__main__':
	m = minesweeper()
	m.banner()
	choice = m.menu()
	if choice == 1:
		m.Play()
	elif choice == 2:
		exit()
	else:
		exit()
	