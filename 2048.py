#!/usr/bin/python
import string
import random 


word = "new"
i = 0
j = 0
status = "new"
direction = "hello"
hasMoved = False
numberOfInts = 0

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
	if ((direction == "a") or (direction == "A")):
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

def rand(numberOfInts):
	rand = 0
	randomRow = 0
	randomCol = 0
	counter = numberOfInts
	
	while counter:
		randomRow = int(random.random() * 4)
		randomCol = int(random.random() * 4)
		rand = int(random.random() * 2) *2 + 2
		if(value[randomRow][randomCol] == 0):
			value[randomRow][randomCol] = rand
			counter = counter - 1
		#else if (gridFull())
		#	counter = counter - 1
		print randomRow, randomCol, rand, "hello"
		counter = counter - 1
	return

while True:
		init_grid(status)
		findDirection()
		print "entering random"
		rand(2)
		while i <= 3:
			while j <= 3:
				print value[i][j], " ",
				j = j + 1
			print "\n"
			j = 0
			i = i + 1
			
			
		break
	
	
#end while 1 loop
