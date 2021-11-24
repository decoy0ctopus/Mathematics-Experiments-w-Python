def setup():
    global xscl, yscl 
    size(600, 600)

t = 0
def draw():
    global t
    #Moving the origin
    translate(width/2, height/2)
    # Rotating the plane
    # rotate(radians(20))
    # Draw an ellipse (x-coordinate, y-coordinate, width, height)
    # ellipse(0, 0, 100, 100)
    #Draw a rectangle ( x-coordinate, y-coordinate, width, height)
    # rect(0, 0, 40, 30)
    stroke(sin(t)*255, cos(t)*255, sin(t**2)*255)
    for i in range(255):
        rotate(radians(360/90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t+3*i*360/90))
        tri(50)
        popMatrix()
    t += 1
    
def tri(x):
    triangle(-x*sqrt(3)/2, x/2, x*sqrt(3)/2, x/2, 0, -x)
