#!/usr/bin/python
import string
import sys
import random
from Tkinter import *


root = Tk()
word = "new"
i = 0
j = 0
count1 = 0
count2 = 1
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
		print randomRow, randomCol, rand, "hello"
	return

# def findDirection():
# 	direction = (raw_input("Enter direction: "))
# 	shift(direction)
# 	return

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


def initGui():

	root.configure(background = "bisque4")
	root.wm_title("2048 - UNIX")
	mainFrame = Frame(root)
	titleLabel = Label(root, text = "2048: By Sushant, Tom, and Karthik", font = "Helvetica 14 bold", bg = "PeachPuff4", fg = "white" )
	titleLabel.place(x = 100, y = 0)


	root.maxsize(500, 620)
	root.minsize(500, 620)


	button1 = Button(root, text="Up", fg = "white", bg = "firebrick3", width = 3, height = 2, relief = RAISED, command = shift("w"))
	button2 = Button(root, text="Left", fg = "white", bg = "firebrick3", width = 3, height = 2, relief = RAISED, command = shift("a") )
	button3 = Button(root, text="Down", fg = "white", bg = "firebrick3", width = 3, height = 2, relief = RAISED, command = shift("s"))
	button4 = Button(root, text="Right", fg = "white", bg = "firebrick3", width = 3, height = 2, relief = RAISED, command = shift("d"))


	button1.place(x = 370, y = 515)
	button2.place(x = 310, y = 565)
	button3.place(x = 370, y = 565)
	button4.place(x = 430, y = 565)

	canvas1 = Canvas(root, width = 460, height = 460, bg = "bisque2")
	canvas1.place(x = 20, y = 40)


	rect  = canvas1.create_rectangle(20, 20 , 110, 110, fill = "NavajoWhite2" )
	rect2 = canvas1.create_rectangle(130, 20, 220, 110, fill = "NavajoWhite2" )
	rect3 = canvas1.create_rectangle(240, 20, 330, 110, fill = "NavajoWhite2" )
	rect4 = canvas1.create_rectangle(350, 20, 440, 110, fill = "NavajoWhite2" )

	rect5 = canvas1.create_rectangle(20, 130 , 110, 220, fill = "NavajoWhite2" )
	rect6 = canvas1.create_rectangle(130, 130, 220, 220, fill = "NavajoWhite2" )
	rect7 = canvas1.create_rectangle(240, 130, 330, 220, fill = "NavajoWhite2" )
	rect8 = canvas1.create_rectangle(350, 130, 440, 220, fill = "NavajoWhite2" )

	rect9  = canvas1.create_rectangle(20, 240 , 110, 330, fill = "NavajoWhite2" )
	rect10 = canvas1.create_rectangle(130, 240, 220, 330, fill = "NavajoWhite2" )
	rect11 = canvas1.create_rectangle(240, 240, 330, 330, fill = "NavajoWhite2" )
	rect12 = canvas1.create_rectangle(350, 240, 440, 330, fill = "NavajoWhite2" )

	rect13 = canvas1.create_rectangle(20, 350 , 110, 440, fill = "NavajoWhite2" )
	rect14 = canvas1.create_rectangle(130, 350, 220, 440, fill = "NavajoWhite2" )
	rect15 = canvas1.create_rectangle(240, 350, 330, 440, fill = "NavajoWhite2" )
	rect16 = canvas1.create_rectangle(350, 350, 440, 440, fill = "NavajoWhite2" )

	rand(2)

	box00 = Label(root, text = value[0][0], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box00.place(x = 50, y= 85)
	box01 = Label(root, text = value[0][1], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box01.place(x = 165, y= 85)
	box02 = Label(root, text = value[0][2], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box02.place(x = 275, y= 85)
	box03 = Label(root, text = value[0][3], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box03.place(x = 385, y= 85)

	box10 = Label(root, text = value[1][0], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box10.place(x = 50, y= 195)
	box11 = Label(root, text = value[1][1], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box11.place(x = 165, y= 195)
	box12 = Label(root, text = value[1][2], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box12.place(x = 275, y= 195)
	box13 = Label(root, text = value[1][3], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box13.place(x = 385, y= 195)

	box20 = Label(root, text = value[2][0], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box20.place(x = 50, y= 305)
	box21 = Label(root, text = value[2][1], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box21.place(x = 165, y= 305)
	box22 = Label(root, text = value[2][2], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box22.place(x = 275, y= 305)
	box23 = Label(root, text = value[2][3], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box23.place(x = 385, y= 305)

	box30 = Label(root, text = value[3][0], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box30.place(x = 50, y= 415)
	box31 = Label(root, text = value[3][1], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box31.place(x = 165, y= 415)
	box32 = Label(root, text = value[3][2], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box32.place(x = 275, y= 415)
	box33 = Label(root, text = value[3][3], width = 4, font = "Helvetica 20 bold", bg = "NavajoWhite2", fg = "white" )
	box33.place(x = 385, y= 415)

	
#end of initGui


# while 1:
# print "ANYTHINGG"
init_grid(status)
initGui()
print "hello world"

#while True:
#	while i <= 3:
#		while j <= 3:
#			if value[i][j] == 0:
#				print "    ",
#			else:
#				
#				print '%4s' % "||", value[i][j], "||",
#			j = j + 1
#		print "\n"
#		j = 0
#		i = i + 1
#	i = 0
#	j = 0
#	
#	findDirection()
#S	rand(1)
#end while 1 loop





root.mainloop()