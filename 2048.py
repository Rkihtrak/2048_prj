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

def shift(direction):
	i = 0
	j = 1
	#left
	hasMoved = False 
	if (direction == "a") or (direction == "A"):
		while i <= 3:
			while j <= 3:
				if value[i][j] != 0:
					if canmove(direction, i, j):
						hasMoved = True
						
					while canmove(direction, i, j):
						value[i][j-1] = value[i][j]
						value[i][j] = 0
						j -= 1
				j = j + 1
			j = 0
			i = i + 1
			init_grid("clear")
	
	return

while True:
		init_grid(status)
		findDirection()
		while i <= 3:
			while j <= 3:
				print value[i][j], " ",
				j = j + 1
			print "\n"
			j = 0
			i = i + 1
			
		break
	
	
#end while 1 loop
