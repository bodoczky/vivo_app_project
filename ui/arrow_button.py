from kivy.uix.button import Button

class ArrowButton(Button):
    def __init__(self, **kwargs):
        super(ArrowButton, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0] 
        self.color = [0, 0, 0, 1]
        self.size_hint = (None, 1)
        self.width = 70