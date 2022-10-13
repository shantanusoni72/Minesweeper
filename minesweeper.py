import random
import pyfiglet
from termcolor import colored

class minesweeper:
    def Play(self):
        # Play
        n = int(input("[*] Enter the length of ground: "))
        m = minesweeper()
        playground = m.generatingGround(n)
        playground = m.readyGround(playground, n)
        result = m.gameStart(playground, n)
        
    def readyGround(self, playground, n):
        # readyGround
        i = 0
        if i < n + 1:
            playground[random.randint(0,n-1)][random.randint(0,n-1)] = 1
            i += 1
        print("[*] Ground is ready for dig")
        return playground
        
    def generatingGround(self, n):
        # generatingGround
        ground = [[0]*n]*n
        m = minesweeper()
        if ground == None:
            return m.generatingGround(n)
        else: 
            print("[*] Ground have been created")
            return ground
            
    def banner(self):
        # banner
        print(pyfiglet.figlet_format("Minesweeper"))
        print(
            '''
            -----------------------------------Code by ''',colored("@shantanusoni72","cyan"),'''
            -----------------------------------Version ''',colored("2022.1.0","white"),'''
            '''
            )
        
    def menu(self):
        # menu
        print(colored("-------------------------Main-Menu-------------------------","yellow"))
        print(colored("1.","yellow"), "Start the game")
        print(colored("2.","yellow"), "Exit the game")
        print("-----------------------------------")
        choice = int(input("[*] Enter your choice: "))
        return choice

    def gameStart(self, playground, n):
        # gameStart
        for i in range(n):
            for j in range(n):
                x = int(input("[*] Enter the coordinate: x = "))
                y = int(input("[*] Enter the coordinate: y = "))
                try:
                    if playground[x][y] == 1:
                        status = "[*] Boom! Bomb have been blasts. You lose"
                        print(colored(status,"red"))
                        return False
                    status = "[*] No bomb, you are lucky this time"
                    print(colored(status,"green"))
                    if i == n-1 and j == n-1:
                        status = "[*] Congratulations! You won the game"
                        print(colored(status,"green"))
                        return True
                except(Exception):
                    print("[*] Please enter the coordinates within the ground.")

