#Group 9: Jayden p2112790 Nathan 2123082 DAAA2B04
# Shortest Pathfinder class, inherit from parent Pathfinder class
# Uses networkx's shortest path algorith which is Dijkstra algorithm.
''' 
Dijkstra's algorithm is a graph search algorithm that finds the shortest path
from a source node to all other nodes in a weighted graph by successively selecting
the node with the lowest distance and updating distances of its neighbors. 
The algorithm terminates when the destination node is reached or all nodes have been processed.

Steps:
1.Initialize the distance of the source node to zero and set the distance of all other nodes to infinity.
2.Create a priority queue to store nodes to be processed, with the source node added initially.
3.While the priority queue is not empty:
   a. Remove the node with the smallest distance from the priority queue.
   b. For each of the node's neighbors:
   i. Calculate the tentative distance to the neighbor.
   ii. If the tentative distance is less than the current distance of the neighbor, 
   update the neighbor's distance and add it to the priority queue.
4.The final distance values represent the shortest distances from the source node to all other nodes.

Big O Notation: 
O(E + V log V) where E is the number of edges in the graph and V is the number of vertices, it is linear but with a logarithmic factor
Compared to an algorithm like Breadth-first search with a Big O of O(V + E) which is also linear but with no logarithmic factor, it is better.
'''
from path_finder import pathFinder #parent
import networkx as nx

class shortestPathfinder(pathFinder):
   def __init__(self,steps,start,screen,turtle,turtle2,turtle3,map,verifier=False):
      #if used for verification, dont need to init parent
      pathFinder.__init__(self,steps,start,screen,turtle,turtle2,turtle3,map,verifier)
      self.name = 'Dijkstra (shortest path)'
      

   #first add nodes to the networkX graph, then add every edge, then calculate the shortest path using Dijkstra algorithm
   def __A_to_B_path(self, start, dest):
      G = nx.Graph()
      rowCount=len(self.grid)
      colCount=len(self.grid[0])
      # Add nodes to the graph
      for row in range(rowCount):
         for col in range(colCount):
               if self.grid[row][col] !='X':
                  G.add_node((col, row))
      
      # Add edges to the graph
      for node in G.nodes:
         col, row = node
         if col > 0 and self.grid[row][col-1] !='X':
               G.add_edge(node, (col-1, row))
         if col < colCount - 1 and self.grid[row][col+1] !='X':
               G.add_edge(node, (col+1, row))
         if row > 0 and self.grid[row-1][col] !='X':
               G.add_edge(node, (col, row-1))
         if row < rowCount - 1 and self.grid[row+1][col] !='X':
               G.add_edge(node, (col, row+1))
      return nx.shortest_path(G, start,dest)
   
   #for every destination, find a path and append the path together for the final path
   def getPath(self): 
      finalPath=[]
      lastFound=None #storing last found destination
      start=self.current
      for destination in self.destinations:
         newPath=self.__A_to_B_path(start,destination)
         if len(newPath)>1: #if a path was found
            for point in newPath:
               finalPath.append(point)
            start=destination #change new start for next iteration
            finalPath.pop() #remove last point because next path will include it at start
            lastFound=destination
         else:
            raise Exception('Error: No path found')
      finalPath.append(lastFound)
      return finalPath


   def findPath(self):
      '''
      Goes in sequence of destinations to find shortest path
      i.e shortest path to go from Point A to Point B to Point C in that same order
      Most approriate for pizza delivery because deliveries are usually made in order of their customer's order time'''
      try:
         finalPath=self.getPath()
         #draw path
         self.t.showturtle()
         self.t.penup()
         
         if self.needPause or self.needSwitch or self.needReset or not self.destinations:
            return
         self.updateTitle()
         self.t.goto(self.current[0] * self.map.gridScale + self.map.gridScale // 2, -abs(self.current[1] * self.map.gridScale + self.map.gridScale // 2)) #
         self.t.showturtle()
         self.t.shape('classic')
         self.t.pendown()
         
         for square in finalPath[1:]:
            if self.needPause or self.needSwitch or self.needReset:
               break
            x,y=square
            xcoord=x * self.map.gridScale + self.map.gridScale // 2
            ycoord=-abs(y * self.map.gridScale + self.map.gridScale // 2)
            self.t.setheading(self.t.towards(xcoord, ycoord))
            self.t.goto(xcoord,ycoord) 
            self.steps+=1
            self.updateTitle()
            if (x,y) in self.destinations:
               self.destinations.remove((x,y))
            self.current=(x,y)
         print(finalPath)
         return finalPath
      except:
         #switch because no path
         self.needSwitch=True