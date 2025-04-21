class BatchRenderer:
    def __init__(self):
        self._batches = defaultdict(arcade.SpriteList)
        
    def add(self, texture_key, sprite):
        self._batches[texture_key].append(sprite)
        
    def draw(self):
        for batch in self._batches.values():
            batch.draw()