import turtle
class ComponentUtils:
    def __init__(self, mask, slot):
        self.mask = mask
        self.slot = slot
        
class CRender:
    def __init__(self, renderizable:int = 1):
        self.sprite = turtle.Turtle()
        self.sprite.color("white")
        self.sprite.penup()      
        self.sprite.shape("square")
        self.renderizable = renderizable
        self.utils = ComponentUtils(0b1, 0)
        if renderizable == 1:
            self.sprite.showturtle()
        else:
            self.sprite.hideturtle()

class CPosition:
    def __init__(self, x:float = 0, y:float = 0, vx:float = 0, vy:float = 0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.utils = ComponentUtils(0b10, 1)
        
class CSnake:
    def __init__(self):
        self.tail = list()
        self.utils = ComponentUtils(0b100, 2)

class CCollision:
    class BoundingBox:
        def __init__(self, x=0, y=0, x2=20, y2=20):
            self.x=x
            self.y=y
            self.x2 = x2
            self.y2= y2
    def __init__(self, x=0, y=0, x2=20, y2=20):
        self.bbox = self.BoundingBox(x,y,x2,y2)
        self.utils = ComponentUtils(0b1000, 3)


numberOfComponents = 4


class Tags:
    def __init__(self):
        self.snake          = 0b00001 
        self.collider       = 0b00010 
        self.collisionable  = 0b00100 
        self.apple          = 0b01000 
        self.tail           = 0b10000
