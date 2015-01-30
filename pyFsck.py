from sys import argv, stdout
#~ import sys

script, filename = argv

txt = open(filename)
title = open("title.txt")

print title.read()

print "\n\tusage: python pyFsck.py [text file]\n\n"

lst = list(txt)
n = 0
m = len(lst)
a = 0
comma = ""

mem30k = [0] * 30000
pos = 0
loopCounter = 0

def runChar(self):
	global pos
	global n
	global m
	global a
	global b
	global loopCounter
	global comma
	
	if ch == '+':
		if mem30k[pos] < 255:
			mem30k[pos] = mem30k[pos] + 1
			#~ print "mem30k[pos]:", mem30k[pos]
		else:
			#memory cell wrapping enabled
			mem30k[pos] = 0
			#~ print "cannot increase cell above 255"
			
	elif ch == '-':
		if mem30k[pos] > 0:
			mem30k[pos] = mem30k[pos] - 1
			#~ print "mem30k[pos]:", mem30k[pos]
		else:
			#memory cell wrapping enabled
			mem30k[pos] = 255
			#~ print "cannot decrease cell below 0"
			
	elif ch == '<':
		if pos > 0:
			pos = pos - 1
			#~ print "pos:", pos
		else:
			#30k wrapping enabled
			pos = 30000-1
			#~ print "cannot decrement memory below 0"
		
	elif ch == '>':
		if pos < 30000-1:
			pos = pos + 1
			#~ print "pos:", pos
		else:
			#30k wrapping enabled
			pos = 0
			#~ print "cannot increment memory above 30000"
		
	elif ch == '[':
		if mem30k[pos] == 0:
			loopCounter += 1
			while loopCounter != 0:
				b = len(lst[n])
				
				while loopCounter != 0 and a < b-1:
					a += 1
					if lst[n][a] == '[':
						loopCounter += 1
						
					if loopCounter > 0 and lst[n][a] == ']':
						loopCounter -= 1
						
				if n < m and loopCounter > 0:
					a = 0
					n += 1
				
		elif mem30k[pos] != 0:
			if a >= b-1:
				a = 0
				n += 1
		
	elif ch == ']':
		if mem30k[pos] == 0:
			if a < b-1:
				pass
				
			else:
				a = 0
				if n < m-1:
					n += 1
					
				else:
					print "playtime is over"
		
		if mem30k[pos] != 0:
			loopCounter += 1
			while loopCounter != 0:
				b = len(lst[n])
				while loopCounter != 0 and a > 0:
					a -= 1
					if lst[n][a] == ']':
						loopCounter += 1
					
					if loopCounter > 0 and lst[n][a] == '[':
						loopCounter -= 1
					
				if n > 0 and loopCounter > 0:
					n -= 1
					a = len(lst[n])
			
		elif mem30k[pos] == 0:
			pass
					
	elif ch == '.':
		stdout.write(chr(mem30k[pos]))
		
	elif ch == ',':
		if comma == "":
			comma = raw_input("::")
		
		tempComma = list(comma)
		ordComma = ord(tempComma[0])
		mem30k[pos] = ordComma
		
		del(tempComma[0])
		comma = "".join(tempComma)
		
	else:
		pass


while n < m:
	b = len(lst[n])
	while a < b:
		ch = lst[n][a]
		runChar(ch)
		a = a + 1
	a = 0
	n = n + 1
