t=0
circleList = []
points=[]
prop = 0.8

def setup():
    size(600,600)

def draw():
    global t, points, prop
    background(255) #white
    translate(width/2,height/2)
    stroke(0)
    spirograph(300, 105, 5)
    t += 0.1
    

def draw_polygon(sz, points):
    beginShape()
    for i in range(points):
        vertex(sz*cos(radians(360/points*i)), sz*sin(radians(360/points*i)))
    endShape(CLOSE)
    
def orbit(r1, r2):
    global t, circleList
    
    #Orbital path
    noFill()
    stroke(0)
    ellipse(0, 0, r1*2, r1*2)
    
    #Orbiting object
    fill(255, 0, 0)
    y = r1*sin(t)
    x = r1*cos(t)
    ellipse(x, y, r2, r2)
    
    #Horizontal Line
    stroke(0, 255, 0)
    line(x, y, 200, y)
    
    circleList.insert(0,y)
    circleList = [y] + circleList[:249]
    
    for index, value in enumerate(circleList):
    #small circle for trail:
        ellipse(200+index, value, 5, 5)
        
def spirograph(r1, r2, r3):
    global t, points, prop
    #Big circle
    noFill()
    stroke(0)
    x0 = 0
    y0 = 0
    ellipse(x0, y0, r1*2, r1*2)
    
    #Little circle
    x1 = (r1 - r2)*cos(t)
    y1 = (r1 - r2)*sin(t)
    ellipse(x1, y1, r2*2, r2*2)
    
    #drawing dot
    x2 = x1+prop*(r2 - r3)*cos(-((r1-r2)/r2)*10*t)
    y2 = y1+prop*(r2 - r3)*sin(-((r1-r2)/r2)*10*t)
    fill(255,0,0)
    ellipse( x2, y2, 2*r3, 2*r3)
    
    points = [[x2, y2]] + points[:2000]
    for i,p in enumerate(points): #go through the points list
        if i < len(points)-1: #up to the next to last point
            stroke(255,0,0) #draw red lines between the points
            line(p[0],p[1],points[i+1][0],points[i+1][1])

    
    
    
