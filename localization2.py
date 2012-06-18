#colors = [['red', 'green', 'green', 'red' , 'red'],
#          ['red', 'red', 'green', 'red', 'red'],
#          ['red', 'red', 'green', 'green', 'red'],
#          ['red', 'red', 'red', 'red', 'red']]
colors = [['green', 'green'],
          ['red', 'green']]
			
measurements = ['red', 'red']#, 'green', 'green', 'green']
motions =   [[0,0],   [-1,0]]#,   [1,0],   [1,0],   [0,1]]
#colors = [['green', 'green', 'green'],
#		  ['green', 'red', 'red'],
#		  ['green', 'green', 'green']]
#measurements = ['green', 'green', 'green' ,'green', 'green']
#measurements = ['red','red']

#motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
#motions = [[0,0],[0,1]]
sensor_right = 0.8#1#0.2
p_move = 1#

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
# build p with probability distribution
def build():
	q =[]
	rows = len(colors)
	cols = len(colors[0])
	q = [[0 for i in range(cols)] for j in range(rows)]
	nbProbability = 1./(rows*cols)
	for i in range(rows):
		for j in range(cols):
			q[i][j]=nbProbability
	return q
def sense(p,Z):
	q = []
	q = [[0 for i in range(len(p[0]))] for j in range(len(p))]
	for i in range(len(p)):
		for j in range(len(p[0])):
			hit = (Z ==colors[i][j])
			q[i][j]= (p[i][j]*(hit* sensor_right + (1-hit)*(1-sensor_right)))
	s = 0.
	for i in range(len(q)):
		s = s + sum(q[i])
	for i in range(len(q)):
		for j in range(len(q[0])):
			q[i][j] =q[i][j] /(s*1.) 
	return q
def move(p,U):
	q = []
	q = [[0 for i in range(len(p[0]))] for j in range(len(p))]
	print "P: "+str(p)
	print "U: "+str(U)
	for i in range(len(p)):
		for j in range(len(p[0])):
			print 'i-U: '+str(i)+' - '+str(U[0])+'='+ str(i-U[0])
			print 'j - U: '+str(j)+' - '+str(U[1])+'='+str(j - U[1])
			index1 = 0
			hitworld = False
			if(i-U[0]) >= len(p) or (i-U[0])<0:
				index1 = i
				print "index1: "+str(index1)
				hitworld = True
			index2 = 0
			if(j-U[1]) >= len(p[0]) or (j-U[1])<0:
				index2 = j
				print "index2: "+str(index2)
				hitworld = True
			first = (i-U[0]) % len(p)
			second = (j - U[1]) % len(p[0])
			if hitworld:
				first = i
				second = j
				s = 0
				q[i][j] = s 
			else:
				s = p[first][second] * p_move
				q[i][j] = s + p[i][j]
			#s = p[(i-U[0]) % len(p)][(j - U[1]) % len(p[0])] * p_move
			s = s + p[i][j]*(1-p_move)
			print "update q [i][i] = q["+str(i)+"]["+str(j)+"]= "+str(s) 
			#q[i][j] = s + p[i][j]
	s = 0.
	for i in range(len(q)):
		s = s + sum(q[i])
	print 'sum:'+str(s)
	for i in range(len(q)):
		for j in range(len(q[0])):
			q[i][j] =q[i][j] /(s*1.)
	return q
def main():
	p = build()
	for k in range(len(measurements)):
		show(p)
		p = move(p,motions[k])
		show(p)
		p = sense(p,measurements[k])
	show(p)
#Your probability array must be printed 
#with the following code.
#show(p)
main()



