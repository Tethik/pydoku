from array import array
import sys

puzzle = list()
solution = list()

def getPossible(x,y):
	possiblevalues = set(range(1,10))
	boxy = int(y / 3)
	boxx = int(x / 3)
	#print(x,y,boxx,boxy)
	for i in range(9):
		#print(i)
		# Kolla kolumn		
		possiblevalues.discard(puzzle[y][i])
		possiblevalues.discard(solution[y][i])
		# Kolla rad		
		possiblevalues.discard(puzzle[i][x])		
		possiblevalues.discard(solution[i][x])		
		# Kolla box		
		possiblevalues.discard(puzzle[boxy*3 + i % 3][boxx*3 + int(i / 3)])
		possiblevalues.discard(solution[boxy*3 + i % 3][boxx*3 + int(i / 3)])		
		if len(possiblevalues) == 0:
			break
			
	return possiblevalues
	

def solve(i,dir):	
	while i > -1 and i < 81:		
		x = i % 9
		y = int(i / 9)		
		if puzzle[y][x] > 0:
			solution[y][x] = puzzle[y][x]
			i += dir
			continue
		possible = getPossible(x,y)				
		found = False
		#print(i,solution[y][x],possible)
		for p in range(1,10):
			if p in possible and p > solution[y][x]:
				solution[y][x] = p
				i += 1
				dir = 1
				found = True		
				break
				
		if found:
			continue
			
		solution[y][x] = 0
		dir = -1
		i -= 1
		
def stepback():
	solution[8][8] = 0
	i = 79	
	while i > -1:				
		x = i % 9
		y = int(i / 9)
		if puzzle[y][x] > 0:
			i -= 1
			continue
		else:
			return i		
	
def hassolution():
	for r in solution:
		for c in r:
			if c == 0:
				return False
				
	return True
		
for x in range(9):
	puzzle.append(list())
	solution.append(list())
	for y in range(9):
		puzzle[x].append(0)
		solution[x].append(0)
		

if len(sys.argv) == 1:
	print ("Usage: pydoku <puzzle in comma delimited form>")
	input()
else:
	args = sys.argv[1].split(",")
	for i in range(81):
		x = i % 9
		y = int(i / 9)	
		try:
			puzzle[y][x] = int(args[i])
		except ValueError:
			puzzle[y][x] = 0
		
	
solve(0,1)

while hassolution():
	ans = ""
	for i in range(81):
		x = i % 9
		y = int(i / 9)
		if i > 0:
			ans += ","
		ans += str(solution[y][x])
		
	print (ans)	
	index = stepback()
	if index < 0:
		break
	solve(index,-1)

