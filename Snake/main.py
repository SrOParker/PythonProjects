import turtle

import cmp.components as Components
import man.manEntity as GameEngine
import syst.renderSys as RenderSystem
import syst.physicSys as PhysicSystem
import syst.inputSys as InputSystem
import syst.collSys as CollisionSystem
wn = turtle.Screen()
# Customize Screen window
def createWindow():
    wn.bgcolor("black")
    wn.setup(width=1000, height=1000)
    
    
# Game function / game loop
def game ():
    rendSys = RenderSystem.RenderSystem()
    phySys  = PhysicSystem.PhysicSystem()
    inpSys  = InputSystem.InputSystem()
    colSys = CollisionSystem.CollisionSystem()
    while True:
        
        inpSys.update(ge, wn)
        phySys.update(ge, wn)
        colSys.update(ge, wn)
        rendSys.update(ge, wn)
        wn.update()





#############################################
###############MAIN GAME#####################
#############################################

createWindow()

ge = GameEngine.ManEntity()
player = ge.createEntity([Components.CRender(1), Components.CPosition(0,0), Components.CCollision(), Components.CSnake()],[Components.Tags().snake, Components.Tags().collider])
ball = ge.createEntity([Components.CRender(1), Components.CPosition(20,20), Components.CCollision()],[Components.Tags().collisionable, Components.Tags().apple])
ge.getEntityCMP(ball, Components.CRender()).sprite.shape("circle")
game()