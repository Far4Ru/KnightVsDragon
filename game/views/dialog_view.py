class DialogView(Scene):
    def show_dialog(self, dialog_id):
        engine = GameEngine()
        dialog_data = engine.resource_manager.get_dialog(dialog_id)
        
        # Создание компонентов диалога
        speaker_comp = SpeakerComponent(dialog_data['speaker'])
        text_comp = TextComponent(dialog_data['text'])
        
        self.dialog_entity = engine.entity_manager.create_entity([
            speaker_comp,
            text_comp,
            DialogControlsComponent()
        ])
