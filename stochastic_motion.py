# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

#grid = [[0, 0, 0],
#        [0, 0, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    def calcminval(x,y,value,policy):
        minval = 1000
        val = 0.
        dire = 0
        for i in range(len(delta)):
            val = 0.0
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if grid[x2][y2]==0:
                    val = val + success_prob * value[x2][y2]*1.
                else:
                    val = val + success_prob * collision_cost*1.
            else:
                val = val + success_prob * collision_cost*1.
            if i == 0 or i == 2: #up or down
                xleft = x + delta[1][0]
                yleft = y + delta[1][1]

                xright = x + delta[3][0]
                yright = y + delta[3][1]
                #left
                if xleft >= 0 and xleft < len(grid) and yleft >=0 and yleft < len(grid[0]):
                    if grid[xleft][yleft]==0:
                        val = val + failure_prob * value[xleft][yleft]
                    else:
                        val = val + failure_prob * collision_cost*1.
                else:#off the grid then collision_cost
                    val = val + failure_prob * collision_cost*1.
                #right	
                if xright >= 0 and xright < len(grid) and yright >=0 and yright < len(grid[0]):
                    if grid[xright][yright] == 0:
                        val = val + failure_prob * value[xright][yright]*1.
                    else:
                        val = val + failure_prob * collision_cost*1.
                else:#off the grid then collision_cost
                    val = val + failure_prob * collision_cost*1.
            else:# left or right
                xup = x + delta[0][0]
                yup = y + delta[0][1]

                xdown = x + delta[2][0]
                ydown = y + delta[2][1]
                #left
                if xup >= 0 and xup < len(grid) and yup >=0 and yup < len(grid[0]):
                    if grid[xup][yup]==0:
                        val = val + failure_prob * value[xup][yup]*1.
                    else:
                        val = val + failure_prob * collision_cost*1.
                else:#off the grid then val collision_cost
                    val = val + failure_prob * collision_cost*1.
                #right	
                if xdown >= 0 and xdown < len(grid) and ydown >=0 and ydown < len(grid[0]):
                    if grid[xdown][ydown]==0:
                        val = val + failure_prob * value[xdown][ydown]*1.
                    else:
                        val = val + failure_prob * collision_cost*1.
                else:#off the grid then val collision_cost
                    val = val + failure_prob * collision_cost*1.
            #add the cost step
            val = val +cost_step
            if val < minval and abs(val-minval)>0.00001:
                minval = val
                dire = i
        policy[x][y] = delta_name[dire]
        return minval
    
    
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    #init goal value/cost
    value[goal[0]][goal[1]] = 0.0
    policy[goal[0]][goal[1]] ='*'
    x = goal[0]
    y = goal[1]
    converge = False
    #visited = []
    #visited.append(goal)
    open = [[0,x,y]]
    while not converge:
        open.sort()
        open.reverse()
        next = open.pop()
        x = next[1]
        y = next[2]
        c = next[0]
        # look for each neighbor and calculate its minval
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            #check frontiers
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                #only if not a block
                if grid[x2][y2] == 0 and [x2,y2]!=[goal[0],goal[1]]:
                    #calculate new value then append
                    val = calcminval(x2,y2,value,policy)
                    if abs(val-value[x2][y2])>0.00001:
                        if val < value[x2][y2]:
                            value[x2][y2] = val
                            found = False
                            for elem in open:
                                if elem[1]==x2 and elem[2]==y2:
                                    elem[0]=val
                                    found = True
                            if not found:
                                open.append([val,x2,y2])
        if len(open) == 0:
            converge = True	
    return value, policy
v,p= stochastic_value()
for i in v:
    print i
for j in p:
    print j