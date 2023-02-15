#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04

'''
Map class, 
reads a .txt file to initialise the grid which is a 3D list, representing the city  map
Calculates the size and approriate scale of the grid based on the number of columns and rows (dynamic scaling)
It draws out the map using the turtle pen passed by main program. 
'''
from sorted_linked_list import Sorted_Linked_List

class Map:
    def __init__(self,pen,windowSize):
        self.grid = []
        self.start = ()
        self.destinations = []
        self.pen=pen
        # Set the size of the window and the scale of the grid (square sizes)
        self.windowSize = windowSize
        #default values for grid sizes
        self.gridScale = self.windowSize // 27
        self.shapeScale=self.gridScale//21
        self.squareOffset=self.gridScale//2
        

        
    
    def readFile(self, filename):
        values = []
        with open(f'{filename}', 'r') as f:
            for line in f:
                print(line)
                line=line.strip() #remove whitespace
                array = list(line)
                if array: #if not empty
                    values.append(array)
        self.grid = values

        sortedList=Sorted_Linked_List()
        # Looping to find the location of "s" and "e" in the map
        for row in range(len(values)): 
            for col in range(len(values[0])): 
                if values[row][col] == "s":
                    if self.start:
                        print('WARNING: Multiple stores detected: Lowest one to the right will be used as the start')
                    self.start = (col,row)
                elif values[row][col] == "e":
                    self.destinations.append((col,row))
                #SORTED LINKED LIST FOR PRIORITY DESTINATIONS FOR DESTINATIONS LABELLED AS DIGITS (1-9)
                elif values[row][col].isdigit():
                    sortedList.insert_element([values[row][col],(col,row)])
        
        #PRIORITY DESTINATIONS
        if sortedList.size>0:
            print(sortedList.return_list())
            finalSortedList=sortedList.return_list()
            if sortedList.size>1:
                finalSortedList.reverse()

                

            print(finalSortedList)
            for x in finalSortedList:
                print('yes1')
                print(x)
                self.destinations.insert(0,x[1]) #insert into 1st index

            
        #error checks
        if not self.grid:
            raise Exception('Error no map data found')
        if not self.destinations:
            raise Exception('Error no destination location found')
        if not self.start:
            raise Exception('Error no start location found')
        print(self.destinations)
        self.OGdestinations=list(self.destinations) #store as a seperate variable
        self.__updateSize()



    def __updateSize(self):
        rowCount= len(self.grid)
        colCount =len(self.grid[0])
        #minimum and maximum square sizes
        maxScale=26
        minScale=8
        #loop to find ideal size of square that fits both vertical and horizontal space
        scale=maxScale #try max first then work our way down
        offset=0
        horPixels=1200
        verPixels=600
        while True:
            #set size based on vertical space
            self.gridScale=scale-offset
            #check if vertical and horizontal space allows
            if (self.gridScale*rowCount)<verPixels and (self.gridScale*colCount)<horPixels:
                break 
            elif self.gridScale==minScale: #already minimum and cant fit more
                raise Exception("Sorry but your map is too large.")
            else:
                offset+=1 #inrease offset to decrease square size

        self.shapeScale=self.gridScale/21
        self.squareOffset=self.gridScale//2

    
    #Function for drawing the map, squares are drawn using turtle stamps, then pen is used to draw out the borders of the squares
    def drawMap(self):
        
        def __drawSquare(row, col, color):
            self.pen.goto(self.squareOffset+col * self.gridScale, -self.squareOffset -abs(row * self.gridScale))
            self.pen.color(color)
            self.pen.stamp()
      

            
        def __drawBorders(rowCount,colCount):
            for row in range(rowCount+1):
                self.pen.penup()
                self.pen.color('black')
                self.pen.goto(0, -abs(row * self.gridScale))
                self.pen.pendown()
                self.pen.goto(colCount*self.gridScale,-abs(row * self.gridScale))
           
            for col in range(colCount+1):
                self.pen.penup()
                self.pen.color('black')
                self.pen.goto(abs(col * self.gridScale),0)
                self.pen.pendown()
                self.pen.goto(abs(col * self.gridScale),-abs(rowCount*self.gridScale))

   
                
        def __drawTitle():
            self.pen.penup()
            self.pen.goto(0,10)
            self.pen.write('PIZZA RUNNERS: DONE BY NATHAN (2123082) AND JAYDEN (2112790) DAAA/2B/04')
            self.pen.goto(0,45)
            self.pen.color('red')
            self.pen.write('CONTROLS: \nSpacebar -> Pause/Unpause      Tab -> Change Pathfinding Algorithm   R -> Reset Drone    Arrow Keys: Move drone up/down/left/right in manual mode')

        
        __drawTitle()
        self.grid
        rowCount=len(self.grid)
        colCount=len(self.grid[0])
        self.pen.color("black")
        self.pen.speed(1000000)
        #squares
        self.pen.shape("square")
        self.pen.shapesize(self.shapeScale,self.shapeScale)
        self.pen.penup()
        for row in range(0,rowCount):
            for col in range(colCount):
                val=self.grid[row][col]
                if val=='.':
                    continue 
                elif val=='X':
                    __drawSquare(row, col, "grey")
                elif val=='s':
                    __drawSquare(row, col, "lime")
                elif (col,row) in self.destinations:
                    __drawSquare(row,col,"cyan")
        __drawBorders(rowCount,colCount)
    


