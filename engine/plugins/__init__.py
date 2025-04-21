class Plugin:
    def initialize(self, container):
        pass

class AnalyticsPlugin(Plugin):
    def initialize(self, container):
        container.resource.add_provider(
            providers.Singleton(AnalyticsService)
        )

# main.py
# container = EngineContainer()
# container.wire(modules=[__name__])
# container.plugin_manager.install(AnalyticsPlugin())