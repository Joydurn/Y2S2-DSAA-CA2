#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
# Random Algorithm class, inherit from pathFinder parent class
'''
The main purpose of this pathfinder is to improve the left hand algorithm.
When the left hand algorithm is stuck in a loop, it will automatically switch
to this random algorithm in the hopes of getting itself unstuck/finding the destination.
More details/justification in the pathfinder_leftHand.py
Algorithm:
1. Calculates which of the 4 possible directions are valid (in bounds and not a building)
2. Appends the direction to a list twice, if the last direction moved by the algorithm was the opposite, append once
    a. This makes the algorithm disfavour going backwards compared to the other directions, hence higher chance of making progress
3. Randomly sample a direction from the list
4. Move in that sampled direction
5. Repeat
'''
import random
from path_finder import pathFinder #parent

class randomPathfinder(pathFinder):
    def __init__(self,steps,start,screen,turtle,turtle2,turtle3,map,maxSteps):
        pathFinder.__init__(self,steps,start,screen,turtle,turtle2,turtle3,map)
        self.maxSteps=maxSteps
        
        if self.maxSteps != 0:
            self.name = 'Random Algorithm (unstuck)'
            self.needPause = False
        else:
            self.name = 'Random Algorithm'
    def findPath(self):
        x,y = self.current 
        colCount=len(self.grid[0])
        rowCount=len(self.grid)
        self.t.showturtle()
        self.t.penup()
        #if paused
        if self.needPause or self.needSwitch or self.needReset or not self.destinations:
            return
        self.updateTitle()
        self.t.goto(self.current[0] * self.map.gridScale + self.map.gridScale // 2, -abs(self.current[1] * self.map.gridScale + self.map.gridScale // 2))
        
        self.t.pendown()
        lastDirection=None
        repeat = False
        if self.maxSteps == 0:
            repeat = True
        # for i in range(self.maxSteps):
        i= 0 
        while i < self.maxSteps or repeat:
            #if no more destinations / Paused / Switching Algorithms
            if not self.destinations or self.needPause or self.needSwitch or self.needReset:
                return
            if (x,y) in self.destinations:
                self.destinations.remove((x,y)) #reached destination, remove from list
                continue
            valid_directions = []
            if x+1 < colCount and self.grid[y][x+1] != "X":
                if lastDirection=='left':
                    valid_directions.append("right")
                elif lastDirection=='right':
                    valid_directions.append("right")
                    valid_directions.append("right") #prioritise straight line
                else: 
                    valid_directions.append("right")
                    valid_directions.append("right")
                    #append twice so less probable to backtrack
            if x-1 >= 0 and self.grid[y][x-1] != "X":
                if lastDirection=='right':
                    valid_directions.append("left")
                elif lastDirection=='left':
                    valid_directions.append("left")
                    valid_directions.append("left") #prioritise straight line
                else: 
                    valid_directions.append("left")
                    valid_directions.append("left")
                    #append twice so less probable to backtrack
            if y+1 < rowCount and self.grid[y+1][x] != "X":
                if lastDirection=='up':
                    valid_directions.append("down")
                elif lastDirection=='down':
                    valid_directions.append("down")
                    valid_directions.append("down") #prioritise straight line
                else: 
                    valid_directions.append("down")
                    valid_directions.append("down")
                    #append twice so less probable to backtrack
            if y-1 >= 0 and self.grid[y-1][x] != "X":
                if lastDirection=='down':
                    valid_directions.append("up")
                elif lastDirection=='up':
                    valid_directions.append("up")
                    valid_directions.append("up") #prioritise straight line
                else: 
                    valid_directions.append("up")
                    valid_directions.append("up")
                    #append twice so less probable to backtrack


            if not valid_directions:
                print('Error: No path')
                break
            direction = random.choice(valid_directions)
            lastDirection=direction
            if direction == "right":
                x += 1
                xcoord=x * self.map.gridScale + self.map.gridScale // 2
                ycoord=-abs(y * self.map.gridScale + self.map.gridScale // 2)
                self.t.setheading(self.t.towards(xcoord,ycoord))
                self.t.goto(xcoord,ycoord)
            elif direction == "left":
                x -= 1
                xcoord=x * self.map.gridScale + self.map.gridScale // 2
                ycoord=-abs(y * self.map.gridScale + self.map.gridScale // 2)
                self.t.setheading(self.t.towards(xcoord,ycoord))
                self.t.goto(xcoord,ycoord)
            elif direction == "up":
                y -= 1
                xcoord=x * self.map.gridScale + self.map.gridScale // 2
                ycoord=-abs(y * self.map.gridScale + self.map.gridScale // 2)
                self.t.setheading(self.t.towards(xcoord,ycoord))
                self.t.goto(xcoord,ycoord)
            elif direction == "down":
                y += 1
                xcoord=x * self.map.gridScale + self.map.gridScale // 2
                ycoord=-abs(y * self.map.gridScale + self.map.gridScale // 2)
                self.t.setheading(self.t.towards(xcoord,ycoord))
                self.t.goto(xcoord,ycoord)
            
            self.current=(x,y)
            self.steps+=1
            self.updateTitle()
            i+= 1
            
        self.needSwitch=True #switch back to left hand algorithm
        



