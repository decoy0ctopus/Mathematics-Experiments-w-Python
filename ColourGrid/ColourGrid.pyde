def setup():
    global xscl, yscl 
    size(600, 600)
    
def draw():
    background(0)
    for x in range(20):
        for y in range(20):
            d = dist(30*x, 30*y, mouseX, mouseY)
            fill(1*d, 2*d, 0.5*d)
            rect(30*x, 30*y, 30, 30)
