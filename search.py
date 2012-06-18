# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
	
	# init vars
	to_open = [] 	#next coords check
	visited = [] 	#coords already checked
	look = []		#coords to add to to_open array
	current_cost = 0#incremental cost
	toExpand = True
	
	#first case
	to_open.append([0,init[0],init[1]])
	current = [current_cost,init]
	to_open.pop()
	
	# loop until goal is found or their is nothing to expand
	while current[1] != goal and toExpand:
		
		if current[1] not in visited:
			visited.append(current[1])
			
		look = look_allcases(current[1],visited)
		#increment current cost to be the cost of current case plus the cost
		current_cost= current[0] + cost
		
		#add posible cases to array
		for elem in look:
			to_open.append([current_cost,elem[0],elem[1]])
		# check if nothing else to expand hence, goal not found 
		if to_open == []:
			toExpand = False
		# if their are still coords to expand
		if toExpand:
			# get index to min gval
			min_index = index_mingval(to_open)
			#expand elem with min gval
			temp =  to_open.pop(min_index)
			current = [ temp[0] , [ temp[1],temp[2] ] ]
	
	if current[1] == goal:
		return [current[0],current[1][0],current[1][1]]
	else:
		return "fail"
	
# for a current coordinates returns a list of all posible coordinates
# invalid cases are removed: fontier values
# allready visited values
def look_allcases(current,visited):
	
	look = []
	to_remove = []
	look_up = [current[0] + delta[0][0],current[1] + delta[0][1]]
	look_left = [current[0] + delta[1][0],current[1] + delta[1][1]]
	look_down = [current[0] + delta[2][0],current[1] + delta[2][1]]
	look_right = [current[0] + delta[3][0],current[1] + delta[3][1]]
	look.append(look_up)
	look.append(look_left)
	look.append(look_down)
	look.append(look_right)
	
	#remove invalid cases eg: fontier values or already visited values
	for i in range(len(look)):
		#check up and left fontiers
		if -1 in look[i]:
			to_remove.append(i)
		#check down fontiers
		elif len(grid) == look[i][0]:
			to_remove.append(i)
		#check right frontiers
		elif len(grid[0]) ==look[i][1]:
			to_remove.append(i)
		#check visited
		elif look[i] in visited:
			to_remove.append(i)
		#check if element is in a block eg: '1'
		elif grid[look[i][0]][look[i][1]] == 1:
			to_remove.append(i)
	#create new look with valid cases
	new_look = []
	for i in range(len(look)):
		if i not in to_remove:
			new_look.append(look[i])
	return new_look
	
# get index of the element with the lowest gval
def index_mingval(to_open):
	#look for smallest gval
	min_gval = to_open[0][0]
	curr_index = 0
	min_index = 0
	for elem in to_open:
		if min_gval > elem[0]:
			min_gval = elem[0]
			min_index = curr_index
		curr_index = curr_index + 1
	return min_index	
print search()
