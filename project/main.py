#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
#main.py 
'''
For details of the main program see logic.py
1.	Maps files: Please place any map files in the maps folder. The map can have multiple destinations with multiple usage scenarios.
	General requirements:
	Max supported size: 140 columns x 70 rows
	X indicates a building/unavailable square
	. indicates a available square
	s indicates the starting square for the drone 
	If more than 1 s is detected, the most bottom-right square will be used
	e indicates a destination
	A number from 1-9 will indicate a destination using priority
	Multiple e letters: Shortest-path finder will go through in order of top to bottom , then left to right. 
	Priority destinations: Use numbers from (1-9) instead of e to designate the order of destinations for the shortest-path finder to follow. 
	If there are multiple destinations under one number it will follow the rules stated in a. but for those specific destinations only.


2.	Loading the Program: You can Load the program by opening anaconda prompt and going to the project folder, from there just type “python main.py (and a map of your choice e.g. map1.txt)”. This will bring a pop-up window where it will be ready to use. (Note: maps have to be in maps folder to be used)
3.	When loading the program, the default Algorithm is the Left-Hand Algorithm as denoted by the title of the pop-up window at the top left. For other algorithms, you can use the “Tab” key to change algorithms to others such as Dijkstra Algorithm (which is the fastest algorithm). We have a total of 4 modes for you to choose from and it goes in this order: Left-Hand, Dijkstra, Manual Input, Random Movement. (Note: Left-Hand algorithm will switch to Random Movement automatically to unstuck itself)
4.	When you have selected the mode which you want, you can press “Space” key to start running the algorithm. For Manual mode, you can just press the arrow keys to move the turtle.
5.	Pressing “Space” at any time during the running of the algorithms will Pause or Un pause if it is already paused. Note: The title shows whether the algorithm is paused and there is a display when paused too
6.	Pressing “Tab” at any time will change the modes as earlier mentioned. After changing the modes, the program will automatically pause so do press “Space” to un pause or press “Tab” to continue switching/cycling between modes.
7.	If you wish to reset the pathfinder at any time, press “R” to reset the drone to its start position
'''
import sys

#Check filename argument
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument. Eg. 'python main.py filename.txt'")
    sys.exit()

filename = sys.argv[1]
try:
    with open(f'maps/{filename}', 'r') as file:
        #open just to check if file is there
        pass
except FileNotFoundError:
    print("The file could not be found. Please use 'python main.py filename.txt'")
    sys.exit()

from logic import MainProgram 
main=MainProgram(filename)
if __name__=='__main__':
    main.main()
else:
    print('Not Authorised')