#Laura Davis 27 June 2017

#Lesson and source code from YouTube user Trevor Payne
#This program demonstrates the A* (A-star) algorithm
#implemented with Python script.
#This algorithm is used specifically for AI and is used
#to find the shortest possible path from start to end states.
#The algorithm executes in three main stages:
#1.Setting start and goal (end) states 2.How progress is measured 
#3.How paths are generated in order to come to a logical solution.
#The logic of the algorithm: 1.Generate list of possible next steps from
#current position 2.Store "children" in queue based on distance to goal
#No potential paths o children are discarded.
#3.Select closest child and repeat until either the goal is reached
#or no more children exist.
#For more on states and related info, see finite-state machines. 

#!usr/bin/env python

from Queue import PriorityQueue

#creates preliminary values for variables and start state
class State(object):
	def __init__(self, value, parent, start = 0, goal = 0):
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0
		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal

#calls GetDist and CreateChildren		
	def GetDist(self):
		pass
	def CreateChildren(self):
		pass

#initializes State_String and GetDist 
class State_String(State):
	def __init__(self, value, parent, start = 0, goal = 0):
		super(State_String, self).__init__(value, 
			parent, start, goal)
		self.dist = self.GetDist()

#checks distance			
	def GetDist(self):
		if self.value == self.goal:
			return 0
		dist = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i - self.value.index(letter))
		return dist

#creates the children and reduces risk of accidental double-creation			
	def CreateChildren(self):
		if not self.children:
			for i in xrange(len(self.goal) - 1):
				val = self.value
				val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
				child = State_String(val, self)
				self.children.append(child)
				
#stores possible solutions to the problem
class AStar_Solver:
	def __init__(self, start, goal):
		self.path = []
		self.visitedQueue = []
		self.priorityQueue = PriorityQueue()
		self.start = start
		self.goal = goal

#calculates solutions, increments, checks distance, and comes to a solution			
	def Solve(self):
		startState = State_String(self.start, 0, self.start, self.goal)
		count = 0
		self.priorityQueue.put((0, count, startState))
		while(not self.path and self.priorityQueue.qsize()):
			closestChild = self.priorityQueue.get()[2]
			closestChild.CreateChildren()
			self.visitedQueue.append(closestChild.value)
			for child in closestChild.children:
				if child.value not in self.visitedQueue:
					count += 1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist, count, child))
		if not self.path:
			print "Goal of " + self.goal + " is not possible!"
		return self.path
	
##=====================================================================================
##MAIN
#initializes solver and calls main and sets start state and goal state

if __name__ =="__main__":
	start1 = "ruaLa viDas"
	goal1 = "Laura Davis"
	print 'starting...'
	a = AStar_Solver(start1, goal1)
	a.Solve()
	for i in xrange(len(a.path)):
		print "%d) " %i + a.path[i]


