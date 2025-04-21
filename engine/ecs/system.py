class RenderingSystem(System):
    def update(self, entities):
        for entity in entities.with_components(Transform, Sprite):
            position = entity.get(Transform)
            sprite = entity.get(Sprite)
            sprite.draw(position.x, position.y)