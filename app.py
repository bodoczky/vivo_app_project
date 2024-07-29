from data.data_manager import DataManager
from ui.ui import FencingPointsTracker
from kivy.core.window import Window
from kivy.app import App

class FencingPointsApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        data_manager = DataManager('fencing_data.json')
        return FencingPointsTracker(
            data_manager=data_manager
        )