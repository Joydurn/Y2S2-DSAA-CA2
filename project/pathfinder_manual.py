#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
# Manual Algorithm class
from path_finder import pathFinder #parent
'''
The main purpose of the Manual Input Mode is to allow users to freely explore the whole map.
With the Algorithms, they start from the start and goes towards the destination, but what
'''
class manualPathfinder(pathFinder):
    def __init__(self,steps,start,screen,turtle,turtle2,turtle3,map):
        pathFinder.__init__(self,steps,start,screen,turtle,turtle2,turtle3,map)
        self.name = 'Manual Input'
        self.needPause = False
        self.screen.onkey(None,'space') #override pause, can't pause in manual mode (no need)


    def __move(self, direction, gridScale):
        x, y = self.current
        
        if direction == "up":
            if self.isInBounds([x, y-1]):
                if self.grid[y-1][x] != 'X':
                    self.t.setheading(90)
                    self.current = (x, y-1)
                    self.t.forward(gridScale)
                    self.steps += 1
                    self.updateTitle()
                    self.path.append(self.current)
        elif direction == "down":
            if self.isInBounds([x, y+1]):
                if self.grid[y+1][x] != 'X':
                    self.t.setheading(270)
                    self.current = (x, y+1)
                    self.t.forward(gridScale)
                    self.steps += 1
                    self.updateTitle()
                    self.path.append(self.current)
        elif direction == "left":
            if self.isInBounds([x-1, y]):
                if self.grid[y][x-1] != 'X':
                    self.t.setheading(180)
                    self.current = (x-1, y)
                    self.t.forward(gridScale)
                    self.steps += 1
                    self.updateTitle()
                    self.path.append(self.current)
        elif direction == "right":
            if self.isInBounds([x+1, y]):
                if self.grid[y][x+1] != 'X':
                    self.t.setheading(0)
                    self.current = (x+1, y)
                    self.t.forward(gridScale)
                    self.steps += 1
                    self.updateTitle()
                    self.path.append(self.current)

        new_x, new_y = self.current
        if (new_x, new_y) in self.destinations:          
            self.destinations.remove((new_x,new_y)) #reached destination, remove from list
            
        return



    def findPath(self):
        self.updateTitle()
        self.t.penup()
        self.t.pendown()
        self.t.shape('classic')
        self.t.color('blue')
        self.t.showturtle()
            
        # Moving turtle 


        self.screen.onkey(lambda: self.__move('up',self.map.gridScale), 'Up')
        self.screen.onkey(lambda: self.__move('down',self.map.gridScale), 'Down')
        self.screen.onkey(lambda: self.__move('left',self.map.gridScale), 'Left')
        self.screen.onkey(lambda: self.__move('right',self.map.gridScale), 'Right')
        

            
            
