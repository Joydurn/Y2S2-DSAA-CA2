#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
'''
Main Program class sets up the turtle graphics window and handles all the individual turtle pens.
It also handles the switching of pathfinding algorithms, pausing, resetting the program, as well as the
Tkinter pathfinding speed widget. 
More details of the main() function below
'''

import turtle 
import time
from map import Map 
from pathfinder_shortest import shortestPathfinder
from pathfinder_leftHand import leftHandPathfinder
from pathfinder_random import randomPathfinder
from pathfinder_manual import manualPathfinder
import random
import tkinter as tk

class MainProgram:
    def __init__(self,filename):
        global paused
        self.filename=filename


        # Initialize the turtle graphics window
        __windowSize=720

        self.screen=turtle.Screen()
        self.screen.setup(1280,720)
        self.screen.title("Drawing Map")
        self.screen.bgcolor("white")
        
        self.pen1=turtle.Turtle(visible=False)
        self.screen.setworldcoordinates(-80,-600,1200,120)
        # self.screen.setworldcoordinates(-144,-1296,1296,144)
        self.pen1=turtle.Turtle(visible=False) #pen for drawing grid/map
        self.pen2=turtle.Turtle(visible=False) #pen for drawing path
        self.pen2.shape('classic')
        self.pen2.color('blue')
        self.pen2.speed(1)
        self.pen2.pensize(3) #default pensize
        #pen for updating step count
        self.pen3=turtle.Turtle(visible=False) 
        self.pen3.penup()
        self.pen3.goto(-70,-50)
        
        #pen for updating algorithm
        self.__pen4=turtle.Turtle(visible=False) 
        self.__pen4.penup()
        self.__pen4.goto(-70,-150)

        #pen for paused state
        self.pen5=turtle.Turtle(visible=False) 
        self.pen5.penup()
        self.pen5.goto(-70,-200)

        #pen for solved state
        self.__pen6=turtle.Turtle(visible=False) 
        self.__pen6.penup()
        self.__pen6.goto(700,20)
        #init map object
        self.map=Map(self.pen1,__windowSize)
        self.map.readFile(f'maps/{self.filename}')
        #set default pathfinder
        self.pathfinder=leftHandPathfinder(0,self.map.start,self.screen,self.pen2,self.pen3,self.pen5,self.map)

    def __drawLabels(self): 
        self.pen1.penup()
        self.pen1.goto(-70, -25)
        self.pen1.write('STEPS:')
        self.pen1.goto(-70, -95)
        self.pen1.write('ALGORITHM:')

    def __updateAlgorithm(self):
        #write number of steps
        name=self.pathfinder.name 
        if name=='Left Hand Algorithm':
            self.__pen4.color("orange")
        elif name=='Dijkstra (shortest path)':
            self.__pen4.color("green")
        elif name=='Manual Input':
            self.__pen4.color("blue")
        elif name=='Random Algorithm':
            self.__pen4.color("red")
        self.__pen4.penup()
        self.__pen4.clear()
        #add spacing to string
        string=''
        for word in self.pathfinder.name.split():
            string+=f'{word}\n' 
        self.__pen4.write(f'{string}',font=("Arial",8,"normal"))

    def __switchPathfinder(self,desiredPF,randomSteps=0):
        
        print('Switching to: ', desiredPF)
        current=self.pathfinder.current
        steps=self.pathfinder.steps
        self.__resetManualInput()

        if desiredPF=='left':
            self.pathfinder=leftHandPathfinder(steps,current,self.screen,self.pen2,self.pen3,self.pen5,self.map)
        elif desiredPF=='leftUnpaused':
            self.pathfinder=leftHandPathfinder(steps,current,self.screen,self.pen2,self.pen3,self.pen5,self.map,shouldBePausedFirst=False)
        elif desiredPF=='shortest':
            self.pathfinder=shortestPathfinder(steps,current,self.screen,self.pen2,self.pen3,self.pen5,self.map)
        
        elif desiredPF=='random':
            self.pathfinder=randomPathfinder(steps,current,self.screen,self.pen2,self.pen3,self.pen5,self.map,randomSteps) #steps,start,screen,turtle,turtle2,map,maxSteps
        elif desiredPF=='manual':
            self.pathfinder=manualPathfinder(steps,current,self.screen,self.pen2,self.pen3,self.pen5,self.map)

        # Updating name of pathfinder
        self.pathfinder.updateTitle()
        self.__updateAlgorithm()
    
    def __handleKeypress(self):
        #cycling pathfinders: left hand -> shortest -> manual path -> random -> left hand -> repeat (left hand will auto switch to random if needed to unstuck itself)
        if self.pathfinder.needReset:
            self.__reset()
        if self.pathfinder.needSwitch:
            if self.pathfinder.name =='Left Hand Algorithm':
                #switch to random for unstuck purpose
                if self.pathfinder.needRandom:
                    print('Changing to Random Algo')
                    self.__switchPathfinder('random',
                    randomSteps=random.randint(8,20)
                    )
                else: #manual user switch
                    print('Changing to shortest algo')
                    self.__switchPathfinder('shortest')
            elif self.pathfinder.name =='Dijkstra (shortest path)':
                print('Changing to manual')
                self.__switchPathfinder("manual")
            elif self.pathfinder.name =='Manual Input':
                print('Changing to Random Algo')
                self.__switchPathfinder('random')
            elif self.pathfinder.name =='Random Algorithm (unstuck)': 
                print('Changing to left algo without pausing')
                self.__switchPathfinder("leftUnpaused")
            elif self.pathfinder.name =='Random Algorithm': 
                print('Changing to left algo')
                self.__switchPathfinder("left")
            
    def __change_speed(self,val):
        speed = int(val)
        self.pen2.speed(speed)

    def __reset(self):
        print('reset')
        
        #reset variables and pathfinder back to start
        self.pathfinder.needPause=True
        self.pen2.penup()
        self.pen2.setheading(0)
        self.pen2.clear()
        #reset destinations
        self.map.destinations=list(self.map.OGdestinations)
        #move drone back
        self.pen2.goto(self.map.start[0] * self.map.gridScale + self.map.gridScale // 2, -abs(self.map.start[1] * self.map.gridScale + self.map.gridScale // 2)) 
        self.pathfinder=leftHandPathfinder(0,self.map.start,self.screen,self.pen2,self.pen3,self.pen5,self.map)
        self.pathfinder.updateTitle()
        self.__updateAlgorithm()
        self.__pen6.clear()
        self.solveFlag=False
        self.__resetManualInput()
        
        
    def __resetManualInput(self):
        self.screen.onkey(None, 'Up')
        self.screen.onkey(None, 'Down')
        self.screen.onkey(None, 'Left')
        self.screen.onkey(None, 'Right')

        
    '''
    First, an instance of our Dijkstra algorithm is used to verify that there is a valid path. If there is no valid path, a warning is shown.
    Then, it calls upon a single instance of the Map class which reads the file given by user, then draws out the map
    using the pens passed in by the Main Program.
    Then, Main Program draws miscellaneous details like the Step Counter and Algorithm Label
    Then we set up the Tkinter slider widget used for the dyanmic pen speed.
    Next we use a single instance of a pathfinder which is switched between the different Pathfinder classes.
    In a loop:
        We use the findPath() function of the Pathfinder classes which will run until either
            a. the user pauses
            b. user wants to switch algorithm 
            c. user wants to reset program
            d. all destinations were reached
        Then we call the handleKeypress function which checks for a,b,c and does actions accordingly
            a. Continue and let the while loop run until the user unpauses
            b. Switch the self.pathfinder to next pathfinder in the cycle
            c. Reset pathfinder to original position
        Then check if d. was reached (i.e all destinations reached), if so, flash a message, this will only flash once
        Repeat
    '''
    def main(self):

        #verify that there is a path, throw warning if not
        
        try: 
            verifier=shortestPathfinder(0,self.map.start,self.screen,self.pen2,self.pen3,self.pen5,self.map,verifier=True)
            verifier.getPath() #if no path, exception thrown
        except:
            print('WARNING: No valid path to reach all destinations found')
            self.pen1.penup()
            self.pen1.goto(500,25)
            self.pen1.write('WARNING: No valid path, shortest pathfinder unavailable')
      

        
        self.map.drawMap()
        self.__drawLabels()
        self.__updateAlgorithm()
        self.pathfinder.updateTitle()

        canvas=self.screen.getcanvas()
        root=canvas.winfo_toplevel()
        
        speed_scale = tk.Scale(root, from_=1, to=10, orient="horizontal",
                       label="Drone Speed", command=self.__change_speed)
        speed_scale.set(1)
        speed_scale.pack()

        self.screen.listen()
        self.solveFlag=False
        while True:
            path=self.pathfinder.findPath()
            self.__handleKeypress()
            if len(self.pathfinder.destinations) == 0 and not self.solveFlag:
                self.__pen6.write(f'SOLVED!',font=("Arial",18,"normal"))
                print('SOLVED')
                time.sleep(2)
                self.__pen6.clear()
                self.solveFlag=True
        self.screen.mainloop()

    
    




