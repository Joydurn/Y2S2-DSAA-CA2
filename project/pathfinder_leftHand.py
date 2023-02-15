#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
# Left hand Rule Algorithm
from path_finder import pathFinder #parent
'''
The left-hand rule algorithm is a simple method for finding an exit from a maze. It involves holding
one's left hand on the wall and always turning left at intersections until the exit is found. In case
the algorithm realises its stuck in a loop, it will automatically switch to a random algorithm to get
itself unstuck. This ensures that if there is a valid path, the left hand algorithm will always find it
eventually. Other methods of improving the algorithm might not follow the idea of the left
hand rule being used by blind people to find their way out of a maze. The use case for this
in our case of the pizza delivery drone is that this algorithm could be used as a backup
in case the drone's sensors fail. For example, its visions sensors might fail so in that case,
it can revert to using the left hand algorithm to always get it to where it needs to go eventually.

Algorithm:
1. Check the square to the left, if available, go there and append to path list, if not continue
2. Check the square in front, if available, go there and append to path list, if not, then turn to the right
3. Repeat. If at a square that has been in the path list more than twice, change the algorithm to random
 algorithm for a random number of steps (between 8 and 20) to get itself unstuck. After switching back to left
 hand algorithm, refresh the path list again.
'''
class leftHandPathfinder(pathFinder):
    def __init__(self,steps,start,screen,turtle,turtle2,turtle3,map,shouldBePausedFirst=True):
        pathFinder.__init__(self,steps,start,screen,turtle,turtle2,turtle3,map)
        self.needRandom=False
        if not shouldBePausedFirst:
            self.needPause=False
        self.name = 'Left Hand Algorithm'
        

    def __facingDown(self,gridScale):
        if (self.t.heading() == 270):                   # check to see if the sprite is pointing down
            x,y = self.current     
            if (x, y) in self.destinations:          
                self.destinations.remove((x,y)) #reached destination, remove from list
                return
            if self.isInBounds([x+1,y]):
                if self.grid[y][x+1]!='X':          # check to see if they are walls on the left
                    ##self.turnAntiClockwise(90) #turn left
                    self.t.left(90)
                    self.current=(x+1,y) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle
                    self.path.append(self.current)
                    return
            if self.isInBounds([x,y+1]):
                if self.grid[y+1][x] !='X':   # check to see if path ahead is clear
                    self.current=(x,y+1) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            ##self.turnAntiClockwise(-90) #turn right
            self.t.right(90)
            return
        


    def __facingLeft(self,gridScale):
        if (self.t.heading() == 180):                   # check to see if the sprite is pointing left
            x,y = self.current     
            if (x, y) in self.destinations:          
                self.destinations.remove((x,y)) #reached destination, remove from list
                return
            if self.isInBounds([x,y+1]):
                if self.grid[y+1][x]!='X':          # check to see if they are walls on the left
                    #self.turnAntiClockwise(90) #turn left
                    self.t.left(90)
                    self.current=(x,y+1) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            if self.isInBounds([x-1,y]):
                if self.grid[y][x-1] !='X':   # check to see if path ahead is clear
                    self.current=(x-1,y) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            #self.turnAntiClockwise(-90) #turn right
            self.t.right(90)
            return
    
    def __facingUp(self,gridScale):
        if (self.t.heading() == 90):                   # check to see if the sprite is pointing up
            
            x,y = self.current     
            if (x, y) in self.destinations:         
                self.destinations.remove((x,y)) #reached destination, remove from list
                return
            if self.isInBounds([x-1,y]):
                if self.grid[y][x-1]!='X':          # check to see if they are walls on the left
                    #self.turnAntiClockwise(90) #turn left
                    self.t.left(90)
                    self.current=(x-1,y) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            if self.isInBounds([x,y-1]):
                if self.grid[y-1][x] !='X':   # check to see if path ahead is clear
                    self.current=(x,y-1) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            #self.turnAntiClockwise(-90) #turn right
            self.t.right(90)
            return
    
    def __facingRight(self,gridScale):
        if (self.t.heading() == 0):                   # check to see if the sprite is pointing right
            
            x,y = self.current     
            if (x, y) in self.destinations:         
                self.destinations.remove((x,y)) #reached destination, remove from list
                return

            if self.isInBounds([x,y-1]):
                if self.grid[y-1][x]!='X':          # check to see if they are walls on the left
                    #self.turnAntiClockwise(90) #turn left
                    self.t.left(90)
                    self.current=(x,y-1) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return

            if self.isInBounds([x+1,y]):
                if self.grid[y][x+1] !='X':   # check to see if path ahead is clear
                    self.current=(x+1,y) #move forward
                    self.t.forward(gridScale)
                    self.steps+=1
                    self.updateTitle()
                    self.path.append(self.current)
                    return
            #self.turnAntiClockwise(-90) #turn right
            self.t.right(90)
            return



    def findPath(self):
        self.t.penup()
        self.t.goto(self.current[0] * self.map.gridScale + self.map.squareOffset, -abs(self.current[1] * self.map.gridScale + self.map.squareOffset)) #
        self.t.pendown()
        self.t.shape('classic')
        self.t.color('blue')
        self.t.showturtle()
        

        
        while self.destinations and not self.needPause and not self.needSwitch and not self.needReset: #while there are still destinations to be reached
            self.updateTitle()
            # Moving turtle
            if self.t.heading() == 270:
                self.__facingDown(self.map.gridScale)

            elif self.t.heading() == 180:
                self.__facingLeft(self.map.gridScale)
                
            elif self.t.heading() == 90:
                self.__facingUp(self.map.gridScale)
                
            elif self.t.heading() == 0:
                self.__facingRight(self.map.gridScale)
            
            #Check if algorithm is stuck (passed a point more than twice)
            if self.path.count(self.current) > 2: 
                #switch pathfinder to random
                self.needRandom=True
                self.needSwitch=True
                break

            print("Current:",self.current) 
            self.updateTitle()
            
        return self.path
