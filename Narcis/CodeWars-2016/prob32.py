import sys

lines = [x for x in sys.stdin.read().split('\n') if x != '0' and x != '']




# Take vars ###################################
fEff = float(lines[0])
fCost = float(lines[1])



# ROAD CLASS #################

class road():
	def __init__(this, origin, destination, name, milles, toll):	
		this.origin = origin
		this.destination = destination
		this.name = name
		this.milles = float(milles)
		this.toll = float(toll)
		this.cost = this.milles*fCost/fEff+this.toll

# Take roads 
cNum = int(lines[2])
rNum = int(lines[3+cNum])


roads = []

for i in range(4+cNum, 4+cNum+rNum):
	li = lines[i].split(' ')
	r = road(li[0], li[1], li[2], li[3], li[4])
	roads.append(r)



# Take cities #################################

class city:
	visited = False
	def __init__(this, name):
		this.name = name
	def getCities(this):
		nearCit = []
		for i in roads:
			if i.origin == this.name:
				nearCit.append([i.destination, i])
			elif i.destination == this.name:
				nearCit.append([i.origin, i])
		return nearCit




cities = []
for i in range(3, 3+cNum):
	c = city(lines[i])
	exec(lines[i]+' = c')
	cities.append(c)


# Get destinations

dNum = int(lines[4+cNum+rNum])

travels = []

for i in range(5+cNum+rNum, 5+cNum+rNum+dNum):
	start = lines[i].split(' ')[0]
	end = lines[i].split(' ')[1]
	temp = []
	exec('temp.append('+start+')')
	exec('temp.append('+end+')')
	travels.append(temp)




# FUNCIO FIND-PATH ####################################################
path = []
bestPath = None



def calculateCost(path):
	if not path: return None
	total = 0.0
	for i in path:
		if type(i) == list:
			total += i[1].cost
	return total

def calculateMilles(path):
	if not path: return None
	total = 0.0
	for i in path:
		if type(i) == list:
			total += i[1].milles
	return total

def calculateCities(path):
	if not path: return None
	total = 0
	for i in path:
		if type(i) == instance:
			total += 1
	return total

def calculateToll(path):
	if not path: return None
	total = 0.0
	for i in path:
		if type(i) == list:
			total += i.toll
	return total

def findPath(current, destination):
	global bestPath
	global path
	if current.name == destination.name:
		if not bestPath or calculateCost(path) < calculateCost(bestPath):
			bestPath = list(path)
		elif calculateCost(path) == calculateCost(bestPath):
			if calculateMilles(path) < calculateMilles(bestPath):
				bestPath = list(path)
			elif calculateMilles(path) == calculateMilles(bestPath):
				if calculateCities(path) < calculateCities(bestPath):
					bestPath = list(path)
				elif calculateCities(path) == calculateCities(bestPath):
					if calculateToll(path) < calculateToll(bestPath):
						bestPath = list(path)

		return
	current.visited = True
	dest = current.getCities()
	path.append(current)
	for i in dest:
		path.append(i)
		exec( 'ii = '+i[0])
		if not ii.visited:
			findPath(ii,destination)
		del path[path.index(i)]
	current.visited = False
	del path[path.index(current)]


# OUTPUT FUNCTION ############################################

def output(path):
	print '%.2f'%(calculateCost(path)), '%.2f'%(calculateMilles(path))
	for i in [x*2 for x in range(len(path)/2)]:			
			print path[i+1][1].name, '%.2f'%(path[i+1][1].milles) , '%.2f'%(path[i+1][1].cost), path[i].name, path[i+1][0]

for i in travels:
	bestPath = []
	path = []
	findPath(i[0],i[1])
	output(bestPath)