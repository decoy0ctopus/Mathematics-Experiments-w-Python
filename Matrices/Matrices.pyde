
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
    fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]
    ang = map(mouseX+mouseY, 0, width, -TWO_PI, TWO_PI)
    rot_matrix = [[cos(ang),-sin(ang)], [sin(ang),cos(ang)]]
    fmatrix = transpose_matrix(multmatrix(rot_matrix, transpose_matrix(fmatrix)))
    graphMatrix(fmatrix)
    
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
            
