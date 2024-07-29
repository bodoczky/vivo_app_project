from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ColorLabel(Label):
    def __init__(self, color, **kwargs):
        super(ColorLabel, self).__init__(**kwargs)
        self.color = (0, 0, 0, 1)  # Black text
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size