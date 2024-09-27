import pgzrun
import random
HEIGHT=600
WIDTH=700
TITLE="Shootaalien"
moonman=Actor("moonman")
counter=0
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.text("Aliens hit:"+str(counter),(300,250))
    moonman.draw()
def on_mouse_down(pos):
    global counter
    if moonman.collidepoint(pos):
        x=random.randint(0,700)
        y=random.randint(0,600)
        moonman.pos=(x,y)
        counter=counter+1
        



    



    
    
        









def update():
    pass
pgzrun.go()