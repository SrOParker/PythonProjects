import cmp.components as Components
import man.manEntity as ManEntity
import random
class CollisionSystem:
    def __init__(self) -> None:
        self.cmps_to_update = [Components.CPosition(), Components.CCollision()]
        self.tags_to_update = [Components.Tags().collider]
        self.actualCollider = ManEntity.Entity()

    def update(self, EM:ManEntity.ManEntity, wn):
        EM.forallMatching(self.update_one_entity, self.cmps_to_update, self.tags_to_update, wn)

    def update_one_entity(self, EM:ManEntity.ManEntity, e:ManEntity.Entity, wn):
        self.actualCollider = e
        EM.forallMatching(self.checkCollision, self.cmps_to_update, [Components.Tags().collisionable], wn)

    def checkCollision(self, EM:ManEntity.ManEntity, e:ManEntity.Entity, wn):
        collider = EM.getEntityCMP(self.actualCollider , Components.CCollision())
        collisionable = EM.getEntityCMP(e , Components.CCollision())
        if self.collisionAABB(collider.bbox, collisionable.bbox) == 1:
            #Hay colision
            if(e.hasTag(Components.Tags().apple)):
                self.collisionWithApple(EM, self.actualCollider, e)
            if(e.hasTag(Components.Tags().tail)):
                self.collisionWithTail(EM, self.actualCollider, e)
            

    def collisionAABB(self, collider:Components.CCollision.BoundingBox, collisionable:Components.CCollision.BoundingBox):
        if collider.x2 < collisionable.x or collider.x > collisionable.x2:
            return 0
        if collider.y2 < collisionable.y or collider.y > collisionable.y2:
            return 0
        
        return 1
    def collisionWithApple(self, EM:ManEntity.ManEntity, e1, e2):
        #rend = EM.getEntityCMP(e2 , Components.CRender())
        pos1 = EM.getEntityCMP(e1 , Components.CPosition())
        pos2 = EM.getEntityCMP(e2 , Components.CPosition())
        if pos1.x == pos2.x and pos1.y == pos2.y:
            #New square to snake
            snake = EM.getEntityCMP(e1, Components.CSnake())
            snake.tail.append(EM.createEntity([Components.CRender(1), Components.CPosition(-10000, -10000), Components.CCollision()],[Components.Tags().collisionable, Components.Tags().tail]))
            #Move apple
            n  = random.randint(-24, 24)
            nn = random.randint(-24, 24)
            n  = random.randint(-24, 24)
            nn = random.randint(-24, 24)
            pos2.x = 20 * n
            pos2.y = 20 * nn
        
    def collisionWithTail(self, EM:ManEntity.ManEntity, e:ManEntity.Entity, e2:ManEntity.Entity):
        pos1 = EM.getEntityCMP(e , Components.CPosition())
        pos2 = EM.getEntityCMP(e2 , Components.CPosition())
        if pos1.x == pos2.x and pos1.y == pos2.y:
            print("cola")
            
