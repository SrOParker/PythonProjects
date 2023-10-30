import cmp.components as Components
import man.manEntity as ManEntity
class RenderSystem:
    def __init__(self) -> None:
        self.cmps_to_update = [Components.CRender()]
        self.tags_to_update = []

    def update(self, EM:ManEntity.ManEntity, wn):
        EM.forallMatching(self.update_one_entity, self.cmps_to_update, self.tags_to_update, wn)

    def update_one_entity(self, EM:ManEntity.ManEntity, e:ManEntity.Entity, wn):
        render = EM.getEntityCMP(e , Components.CRender())
        if render.renderizable == 1:
            render.sprite.showturtle()
        else:
            render.sprite.hideturtle()

