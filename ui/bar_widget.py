from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout

class BarWidget(BoxLayout):
    def __init__(self, height, width, color, **kwargs):
        super(BarWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.width = width
        self.height = height
        self.bind(pos=self.update_rect, size=self.update_rect)

        with self.canvas:
            self.color = Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

