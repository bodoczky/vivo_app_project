from kivy.core.window import Window
from app import FencingPointsApp
import config

if __name__ == '__main__':
    Window.size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    FencingPointsApp().run()

