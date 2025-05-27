def load_entity_from_json(entity_type, x, y) -> Entity:
    with open("entities.json") as f:
        templates = json.load(f)
    
    entity = Entity()
    for comp_name, comp_data in templates[entity_type]["components"].items():
        component_class = globals()[comp_name]  # Получаем класс по имени
        entity.add_component(component_class(**comp_data))
    return entity

# Использование:
player = load_entity_from_json("player", 100, 200)
enemy = load_entity_from_json("enemy", 400, 200)

class GameECS(arcade.Window):
    def __init__(self):
        self.entities = []  # Все сущности
        self.systems = [
            PlayerControlSystem(),
            EnemyAISystem(),
            MovementSystem(),
            RenderingSystem()
        ]

    def on_update(self, delta_time):
        for system in self.systems:
            system.update(self.entities)

class MenuView(Scene):
    def __init(self):
        self.entities = []
        self.systems = [
            MovementSystem(),
            InputSystem(self)
        ]
        self.setup()
        self.ecs_world = ECSWorld()  # Ваш менеджер ECS (сущности + системы)

    def on_show(self):
        self.ecs_world.setup_level_1()

    def on_update(self, delta_time):
        self.ecs_world.update(delta_time)

    def setup(self):
        player = Entity()
        player.add_component(Position(400, 300))
        player.add_component(Velocity(0, 0))
        player.add_component(Controllable())
        self.entities.append(player)# Игрок
        player = Entity()
        player.add_component(Position(100, 200))
        player.add_component(Velocity(0, 0))
        player.add_component(Sprite("player.png"))
        player.add_component(Player())

        # Враг
        enemy = Entity()
        enemy.add_component(Position(400, 200))
        enemy.add_component(Velocity(-1, 0))
        enemy.add_component(Sprite("enemy.png"))
        enemy.add_component(Enemy(enemy_type="range"))

    def on_key_press(self, key, modifiers):
        for system in self.systems:
            if isinstance(system, InputSystem):
                system.on_key_press(key, modifiers)

    def on_update(self, delta_time):
        for system in self.systems:
            if isinstance(system, InputSystem):
                system.process_events(self.entities)
            system.update(self.entities)

    def on_draw(self):
        arcade.start_render()
        for entity in self.entities:
            if Position in entity.components:
                pos = entity.components[Position]
                arcade.draw_circle_filled(pos.x, pos.y, 20, arcade.color.BLUE)