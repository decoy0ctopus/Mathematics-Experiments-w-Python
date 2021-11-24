xmin = -2
xmax = 2
ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
def draw():
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl) , (ymin + y * yscl) ]
            #put it into the mandelbrot function
            col=Mandelbrot(z,100)
            #if mandelbrot returns 0
            if col == 100:
                fill(0) #make the rectangle black
            else:
                fill(255) #make the rectangle white
            #draw a tiny rectangle
            rect(x,y,1,1)

def cAdd(x, y): # Add two complex numbers
    return [x[0]+y[0], x[1]+y[1]]

def cMult(x, y):  # Multiply two complex numbers
    return [x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]]

def Magnitude(x): # Find the magnitude of two complex numbers
    return sqrt(x[0]**2+x[1]**2)

def Mandelbrot(z, num):
    # runs the process num times and returns the diverge count
    count = 0
    z1 = z
    while count <= num:
        #Check for divergence
        if Magnitude(z1) > 2.0:
            return count
        #Iterate process for new z1
        z1 = cAdd(cMult(z1, z1), z)
        count += 1
    #If z hasnt diverged by the end
    return num
        
