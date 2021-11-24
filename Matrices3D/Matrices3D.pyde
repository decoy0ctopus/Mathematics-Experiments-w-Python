
#set the range of x-values
xmin = -10
xmax = 10

#range of y-values 
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin



def setup():
    global xscl, yscl 
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey 

def draw():
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    stroke(0)
    strokeWeight(2)
    noFill()
    fmatrix = [[0,0,0],[1,0,0],[1,2,0],[2,2,0],[2,3,0],[1,3,0],[1,4,0],
          [3,4,0],[3,5,0],[0,5,0],
          [0,0,1],[1,0,1],[1,2,1],[2,2,1],[2,3,1],[1,3,1],[1,4,1],
          [3,4,1],[3,5,1],[0,5,1]]
    edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],
        [7,8],[8,9],[9,0],
        [10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
        [17,18],[18,19],[19,10],
        [0,10],[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],
        [8,18],[9,19]]
    rot = map(mouseX,0,width,0,TWO_PI)
    tilt = map(mouseY,0,height,0,TWO_PI)
    newmatrix = transpose_matrix(multmatrix(rottilt(rot,tilt),transpose_matrix(fmatrix)))
    strokeWeight(2) #thicker line
    stroke(255,0,0) #red resultant matrix
    graphPoints(newmatrix,edges)
    
def grid(xscl, yscl):
    #Draw a grid for graphing
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax + 1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    for i in range(ymin, ymax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)

def graphMatrix(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl, pt[1]*yscl)
    endShape(CLOSE)
    
def graphPoints(pointList,edges):
    '''Graphs the points in a list using segments'''
    for e in edges:
        line(pointList[e[0]][0]*xscl,pointList[e[0]][1]*yscl,
            pointList[e[1]][0]*xscl,pointList[e[1]][1]*yscl)
    
def multmatrix(a,b):
    #Returns the product of matrix a and matrix b
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def transpose_matrix(X):
    Y = []
    for i in range(len(X[0])):
        Y.append([])
        for j in range(len(X)):
            Y[i].append(X[j][i])
    return Y

def rottilt(rot,tilt):
    #returns the matrix for rotating a number of degrees
    rotmatrix_Y = [[cos(rot),0.0,sin(rot)],
                   [0.0,1.0,0.0],
                   [-sin(rot),0.0,cos(rot)]]
    rotmatrix_X = [[1.0,0.0,0.0],
                   [0.0,cos(tilt),sin(tilt)],
                   [0.0,-sin(tilt),cos(tilt)]]
    return multmatrix(rotmatrix_Y,rotmatrix_X)
            
