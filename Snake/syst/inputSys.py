import cmp.components as Components
import man.manEntity as ManEntity
class InputSystem:
    def __init__(self) -> None:
        self.cmps_to_update = [Components.CPosition(), Components.CRender()]
        self.tags_to_update = [Components.Tags().snake]

    def update(self, EM:ManEntity.ManEntity, wn):
        EM.forallMatching(self.update_one_entity, self.cmps_to_update, self.tags_to_update, wn)
        
    def update_one_entity(self, EM:ManEntity.ManEntity, e:ManEntity.Entity, wn):
        render = EM.getEntityCMP(e , Components.CRender())
        position = EM.getEntityCMP(e , Components.CPosition())
        wn.listen()
        wn.onkeypress(lambda: self.moveUp(position), "Up")
        wn.onkeypress(lambda: self.moveDown(position), "Down")
        wn.onkeypress(lambda: self.moveLeft(position), "Left")
        wn.onkeypress(lambda: self.moveRight(position), "Right")
        
    def moveUp(self, pos):
        pos.vy = 20
        pos.vx = 0
    def moveDown(self, pos):
        pos.vy = -20
        pos.vx = 0
    def moveLeft(self, pos):
        pos.vx = -20
        pos.vy = 0
    def moveRight(self, pos):
        pos.vx = 20
        pos.vy = 0

