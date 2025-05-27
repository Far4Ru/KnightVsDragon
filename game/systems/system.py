class MovementSystem:
    def update(self, entities):
        for entity in entities:
            if Position in entity.components and Velocity in entity.components:
                pos = entity.components[Position]
                vel = entity.components[Velocity]
                pos.x += vel.dx
                pos.y += vel.dy

class InputSystem:
    def __init__(self, window):
        self.window = window
        self.events = []

    def on_key_press(self, key, modifiers):
        self.events.append(KeyPressEvent(key))

    def process_events(self, entities):
        for event in self.events:
            if isinstance(event, KeyPressEvent):
                for entity in entities:
                    if Controllable in entity.components:
                        self.handle_controllable(entity, event)
        self.events.clear()

    def handle_controllable(self, entity, event):
        vel = entity.components.get(Velocity)
        if not vel:
            return

        speed = entity.components[Controllable].speed
        if event.key == arcade.key.UP:
            vel.dy = speed
        elif event.key == arcade.key.DOWN:
            vel.dy = -speed
        elif event.key == arcade.key.LEFT:
            vel.dx = -speed
        elif event.key == arcade.key.RIGHT:
            vel.dx = speed



class PhysicsSystem:
    def update(self, entities):
        for i, entity_a in enumerate(entities):
            for entity_b in entities[i+1:]:
                if self.check_collision(entity_a, entity_b):
                    event = CollisionEvent(entity_a, entity_b)
                    # Можно отправлять в систему обработки столкновений
class PlayerControlSystem:
    def update(self, entities):
        for entity in entities:
            if Player in entity.components:  # Работает только с игроком
                pos = entity.components[Position]
                vel = entity.components[Velocity]
                player_data = entity.components[Player]
                
                if keyboard.is_pressed("UP"):
                    vel.dy = player_data.move_speed


class EnemyAISystem:
    def update(self, entities):
        for entity in entities:
            if Enemy in entity.components:  # Только враги
                enemy_data = entity.components[Enemy]
                pos = entity.components[Position]
                
                if enemy_data.enemy_type == "melee":
                    self._chase_player(entity)
                elif enemy_data.enemy_type == "range":
                    self._shoot_projectiles(entity)