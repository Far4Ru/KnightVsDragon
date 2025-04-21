from dependency_injector import containers, providers

class EngineContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    resource = providers.Singleton(ResourceManager)
    scene = providers.Singleton(SceneManager)
    entity = providers.Singleton(EntityManager)