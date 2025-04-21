import watchdog.events

class AssetReloadHandler(watchdog.events.FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".png"):
            key = extract_key_from_path(event.src_path)
            GameEngine().resource_manager.reload_texture(key)