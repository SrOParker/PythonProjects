import turtle

import cmp.components as Components
import man.manEntity as GameEngine
import syst.renderSys as RenderSystem
import syst.physicSys as PhysicSystem
import syst.inputSys as InputSystem
wn = turtle.Screen()
# Customize Screen window
def createWindow():
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    
# Game function / game loop
def game ():
    rendSys = RenderSystem.RenderSystem()
    phySys  = PhysicSystem.PhysicSystem()
    inpSys  = InputSystem.InputSystem()
    
    while True:
        inpSys.update(ge, wn)
        phySys.update(ge, wn)
        rendSys.update(ge, wn)
        wn.update()





#############################################
###############MAIN GAME#####################
#############################################

createWindow()

ge = GameEngine.ManEntity()
ge.createEntity([Components.CRender(1), Components.CPosition(0,0)],[Components.Tags().snake])
ball = ge.createEntity([Components.CRender(1), Components.CPosition(20,20)],[])
ge.getEntityCMP(ball, Components.CRender()).sprite.shape("circle")
game()