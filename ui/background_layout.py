from kivy.graphics import Rectangle
from kivy.uix.relativelayout import RelativeLayout

import config



class BackgroundLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super(BackgroundLayout, self).__init__(**kwargs)
        self.bind(size=self._update_background, pos=self._update_background)
        
        with self.canvas.before:
            self.background = Rectangle(source='assets/background.png', pos=self.pos, size=self.size)

    def _update_background(self, instance, value):
        # Calculate the scaling factor to fit the image while maintaining aspect ratio
        image_ratio = config.WINDOW_WIDTH / config.WINDOW_HEIGHT  # width / height of your background image
        if self.width / self.height > image_ratio:
            # Window is wider than the image
            new_height = self.height
            new_width = new_height * image_ratio
        else:
            # Window is taller than the image
            new_width = self.width
            new_height = new_width / image_ratio

        # Calculate position to center the image
        x = (self.width - new_width) / 2
        y = (self.height - new_height) / 2

        # Update the background rectangle
        self.background.pos = (x, y)
        self.background.size = (new_width, new_height)

