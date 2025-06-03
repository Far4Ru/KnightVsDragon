class AnimationManager:
    def __init__(self):
        self.animations = {}

    def add(self, texture_name, texture):
        frame_index = texture_name.rindex('_')
        if frame_index == -1:
            return
        frame = texture_name[frame_index + 1:]
        animation_name_index = texture_name.rindex('_', 0, frame_index)
        if animation_name_index == -1:
            return
        animation_name = texture_name[animation_name_index + 1:frame_index]
        if self.animations[animation_name] is None:
            self.animations[animation_name] = {}
        self.animations[animation_name][frame] = texture

    def get(self, texture_name: str, animation_name: str, frame: int, looped=True):
        animation = self.animations[texture_name][animation_name]
        if looped:
            return animation[frame % len(animation)]
        if frame < len(animation):
            return animation[frame]
        return None
