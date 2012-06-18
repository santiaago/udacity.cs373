# ----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    gval = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    count = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            gval[x][y] = g
            expand[x][y] = count
            count = count + 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    #print "expand: "
    #for i in range(len(expand)):
    #    print expand[i]
    #print "gval: "
    #for i in range(len(gval)):
    #        print gval[i]
    if found:
        path = [[',' for row in range(len(grid[0]))] for col in range(len(grid))]
        finish = False
        place = []
        place = [goal[0],goal[1]]
        last = '*'
        x = place[0]
        y = place[1]
        delta_name1 = ['v', '>', '^', '<']
        while not finish:
            if place == init:
                finish = True
                path[place[0]][place[1]] = last
            x = place[0]
            y = place[1]
            for i in range(len(delta)):
                x2 = x +delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if  grid[x2][y2] == 0:
                        if gval[x2][y2] < gval[x][y] and gval[x2][y2]>-1:
                            place[0] = x2
                            place[1] = y2
                            path[x][y] = last
                            last = delta_name1[i]

        #path[goal[0]][goal[1]] = '*'
        for i in range(len(path)):
            print path[i]
    return 1#path# make sure you return the shortest path.
search()


