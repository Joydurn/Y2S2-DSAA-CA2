#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
#parent class for other pathfinder algorithms
class pathFinder: 
    def __init__(self,steps,start,screen,turtle1,turtle2,turtle3,map,verifier=False):
        self.name='Pathfinder'
        self.map=map
        self.steps=steps
        self.grid=map.grid
        self.current=start
        self.destinations=map.destinations
        self.path=[start]

        if not verifier:
            self.screen=screen
            self.t=turtle1
            #change pen size depending on gridscale
            if map.gridScale<11:
                self.t.pensize(0.1)
                self.t.turtlesize(0.3)
            elif map.gridScale<17:
                self.t.pensize(0.3)
                self.t.turtlesize(0.5)
            else:
                self.t.pensize(1)
                self.t.turtlesize(1)
            #for STEP COUNT
            self.t2=turtle2
            self.t2.speed(10)
            
            #for PAUSED state
            self.t3=turtle3
            self.t3.speed(10)

            self.needPause=True 
            self.needSwitch=False
            self.needReset=False
            self.screen.onkey(lambda:setattr(self,'needPause', not self.needPause),'space')
            self.screen.onkey(lambda:setattr(self,'needSwitch', True),'Tab')
            self.screen.onkey(lambda:setattr(self,'needReset', True),'r')
            self.screen.listen()

    def isInBounds(self,coordinates):
        x,y=coordinates
        if x < 0 or x >=len(self.grid[0]) or y < 0 or y >= len(self.grid):
            return False 
        else: 
            return True

    def updateTitle(self):
        #display number of steps
        self.t2.color("black")
        self.t2.penup()
        self.t2.clear()
        self.t2.write(f'{self.steps}',font=("Arial",13,"normal"))
        #display paused state
        paused='PAUSED: ' if self.needPause else ''
        self.t3.color("red")
        self.t3.penup()
        self.t3.clear()
        self.t3.write(f'{paused}',font=("Arial",11,"normal"))
        self.t3.write(f'{paused}',font=("Arial",11,"normal"))
        #write number of steps and whether paused
        
        self.screen.title(f"{paused}{self.name}: {self.steps} steps")
    
    def drawPath(self): #overwritten by children
        pass