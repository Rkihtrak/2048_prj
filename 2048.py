#!/usr/bin/python
import string

word = "new"
i = 0
j = 0
status = "new"
direction = "hello"
hasMoved = False

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

def findDirection():
	direction = (raw_input("Enter direction: "))
	shift(direction)
	return

def canMove(direction, i, j):
	if direction == "a":
		if (j - 1) < 0:
			return False
		else:
			if (value[i][j-1] == value[i][j]) and (hasMerged[i][j-1] == False):
				value[i][j-1] *= 2;
				score += value[i][j-1]
				value[i][j] = 0
				hasMerged[i][j-1] = True
				return False
			elif (value[i][j-1] != 0):
				return False
	return True

def shift(direction):
	i = 0
	j = 1
	#left
	hasMoved = False 
	if direction == "a":
		while i <= 3:
			while j <= 3:
				if value[i][j] != 0:
					if canMove(direction, i, j):
						hasMoved = True
						
					while canMove(direction, i, j):
						value[i][j-1] = value[i][j]
						value[i][j] = 0
						j -= 1
				j = j + 1
			j = 0
			i = i + 1
			init_grid("clear")
	
	return
init_grid(status)
value[0][3] = 1	

while True:
	while i <= 3:
		while j <= 3:
			print value[i][j], " ",
			j = j + 1
		print "\n"
		j = 0
		i = i + 1
	i = 0
	j = 0
	findDirection()
#end while 1 loop
