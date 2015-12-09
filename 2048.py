#!/usr/bin/python
import string
import sys
import random
import os

word = "new"
i = 0
j = 0
inp = 2048
numberOfInts = 0
status = "new"
direction = "hello"
hasMoved = False
global score

value = [[0 for x in range(4)] for x in range(4)]
hasMerged = [[False for x in range(4)] for x in range(4)]

def init_grid(word):
	i = 0
	j = 0
	if word == "new":
		while i <= 3:
			while j <= 3:
				value[i][j] = 0
				hasMerged[i][j] = False
				j = j + 1
			j = 0
			i = i + 1	
	elif word == "clear":
		while i <= 3:
			while j <= 3:
				hasMerged[i][j] = False
				j = j + 1
			j = 0
			i = i + 1
	return

def highestTile(inp):
	i = 0
	j = 0
	while i <= 3:
		while j <= 3:
			if value[i][j] == inp:
				return True
			j = j + 1
		j = 0
		i = i + 1
			
def gridFull():
	i = 0;
	j = 0;
	while i <= 3:
		while j <= 3:
			if value[i][j] == 0:
				return False
			j = j + 1
		j = 0
		i = i + 1
		return True

def rand(numberOfInts):
	rand = 0
	randomRow = 0
	randomCol = 0
	counter = numberOfInts
	
	while counter != 0:
		randomRow = int(random.random() * 4)
		randomCol = int(random.random() * 4)
		rand = int(random.random() * 2) *2 + 2
		if(value[randomRow][randomCol] == 0):
			value[randomRow][randomCol] = rand
			counter = counter - 1
		elif (gridFull()):
			counter = counter - 1
		#print randomRow, randomCol, rand, "hello"
	return

def findDirection():
	direction = (raw_input("Enter direction: a,s,d or w then press enter: "))
	os.system('clear')
	shift(direction)
	return

def gameOver():
	i = 0
	j = 0
	while i <= 3:
		while j <= 3:
			if canMove2("a", i, j) or canMove2("s", i, j) or canMove2("d", i, j) or canMove2("w", i, j):
				return False
			j += 1	
		j = 0
		i += 1
	return True


def canMove(direction, i, j):
	###### LEFT ######
	if direction == "a":
		if (j - 1) < 0:
			return False
		else:
			if (value[i][j-1] == value[i][j]) and (hasMerged[i][j-1] == False):
				value[i][j-1] *= 2
				value[i][j] = 0
				hasMerged[i][j-1] = True
				return False
			elif (value[i][j-1] != 0):
				return False
		return True
	######## RIGHT #######
	elif direction == "d":
		if (j + 1) > 3:
			return False
		else:
			if (value[i][j+1] == value[i][j]) and (hasMerged[i][j+1] == False):
				value[i][j+1] *= 2
				value[i][j] = 0
				hasMerged[i][j+1] = True
				return False
			elif (value[i][j+1] != 0):
				return False
		return True
	######## down #######
	elif direction == "s":
		if (i + 1) > 3:
			return False
		else:
			if (value[i+1][j] == value[i][j]) and (hasMerged[i+1][j] == False):
				value[i+1][j] *= 2
				value[i][j] = 0
				hasMerged[i+1][j] = True
				return False
			elif (value[i+1][j] != 0):
				return False
		return True
	######## down #######
	elif direction == "w":
		if (i - 1) < 0:
			return False
		else:
			if (value[i-1][j] == value[i][j]) and (hasMerged[i-1][j] == False):
				value[i-1][j] *= 2
				value[i][j] = 0
				hasMerged[i-1][j] = True
				return False
			elif (value[i-1][j] != 0):
				return False
		return True

def canMove2(direction, i, j):
	###### LEFT ######
	if direction == "a":
		if (j - 1) < 0:
			return False
		else:
			if (value[i][j-1] == value[i][j]) and (hasMerged[i][j-1] == False):
				value[i][j-1] *= 2
				value[i][j] = 0
				hasMerged[i][j-1] = True
				return True
			elif (value[i][j-1] != 0):
				return False
		return True
	######## RIGHT #######
	elif direction == "d":
		if (j + 1) > 3:
			return False
		else:
			if (value[i][j+1] == value[i][j]) and (hasMerged[i][j+1] == False):
				value[i][j+1] *= 2
				value[i][j] = 0
				hasMerged[i][j+1] = True
				return True
			elif (value[i][j+1] != 0):
				return False
		return True
	######## down #######
	elif direction == "s":
		if (i + 1) > 3:
			return False
		else:
			if (value[i+1][j] == value[i][j]) and (hasMerged[i+1][j] == False):
				value[i+1][j] *= 2
				value[i][j] = 0
				hasMerged[i+1][j] = True
				return True
			elif (value[i+1][j] != 0):
				return False
		return True
	######## down #######
	elif direction == "w":
		if (i - 1) < 0:
			return False
		else:
			if (value[i-1][j] == value[i][j]) and (hasMerged[i-1][j] == False):
				value[i-1][j] *= 2
				value[i][j] = 0
				hasMerged[i-1][j] = True
				return True
			elif (value[i-1][j] != 0):
				return False
		return True
		


def shift(direction):
	hasMoved = False 
	#left
	if direction == "a":
		i = 0
		j = 1
		while i <= 3:
			while j <= 3:
				if value[i][j] != 0:
					if canMove(direction, i, j):
						hasMoved = True
						
					while canMove(direction, i, j):
						value[i][j-1] = value[i][j]
						hasMerged[i][j-1] = hasMerged[i][j]
						value[i][j] = 0
						j -= 1
				j = j + 1
			j = 0
			i = i + 1
			init_grid("clear")
	#right
	elif direction == "d":
		i = 3
		j = 2
		while i >= 0:
			while j >= 0:
				if value[i][j] != 0:
					if canMove(direction, i, j):
						hasMoved = True
						
					while canMove(direction, i, j):
						value[i][j+1] = value[i][j]
						hasMerged[i][j+1] = hasMerged[i][j]
						value[i][j] = 0
						j += 1
				j -= 1
			j = 2
			i -= 1
			init_grid("clear")
	#down
	elif direction == "s":
		i = 2
		j = 3
		while i >= 0:
			while j >= 0:
				if value[i][j] != 0:
					if canMove(direction, i, j):
						hasMoved = True
						
					while canMove(direction, i, j):
						value[i+1][j] = value[i][j]
						hasMerged[i+1][j] = hasMerged[i][j]
						value[i][j] = 0
						i += 1
				j = j - 1
			j = 3
			i = i - 1
			init_grid("clear")
		#up
	elif direction == "w":
		i = 1
		j = 0
		while i <= 3:
			while j <= 3:
				if value[i][j] != 0:
					if canMove(direction, i, j):
						hasMoved = True
						
					while canMove(direction, i, j):
						value[i-1][j] = value[i][j]
						hasMerged[i-1][j] = hasMerged[i][j]
						value[i][j] = 0
						i -= 1
				j = j + 1
			j = 0
			i = i + 1
			init_grid("clear")
	return

#def output(stage):
#	if(stage == "initialize")




#	return
	
init_grid(status)
rand(2)
os.system('clear')
while True:
	while i <= 3:
		while j <= 3:
			if value[i][j] == 0:
				print '%4s' % " ",
			else:
				
				print '%4s' %  value[i][j],
			j = j + 1
		print "\n"
		j = 0
		i = i + 1
	i = 0
	j = 0
	findDirection()	
	rand(1)
	if gameOver() == True:
		print "YOU LOSE, Please Exit out of the Program"
#end while 1 loop

