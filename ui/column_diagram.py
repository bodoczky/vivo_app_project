
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from calendar import day_abbr
from datetime import datetime
from ui.bar_widget import BarWidget
from ui.color_label import ColorLabel



class ColumnDiagram(BoxLayout):
    color1 = (0.31, 0.67, 0.91, 1)
    color2 = (0.18, 0.19, 0.55, 1)
    color3 = (0.89, 0.43, 0.22, 1)
    color4 = (0.85, 0.22, 0.19, 1)

    def __init__(self, **kwargs):
        super(ColumnDiagram, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.chart_layout = BoxLayout(orientation='horizontal', size_hint_y=1)
        self.day_labels_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.legend_layout = GridLayout(cols=2, size_hint_y=0.1, )
        self.add_widget(self.chart_layout)
        #self.add_widget(self.day_labels_layout) #removed
        #self.add_widget(self.legend_layout) #removed 

    def update_diagram(self, month_data):
        self.chart_layout.clear_widgets()
        self.day_labels_layout.clear_widgets()
        self.legend_layout.clear_widgets()
        
        categories = ["Victory", "Defeat", "Touches Scored", "Touches Received"]
        colors = [self.color1, self.color2, self.color3, self.color4]
        # Victory: #4EABE9
        # Defeat: #2E318D
        # Touches scored: #E16E38
        # Touches received: #DA3831
        for day, data in sorted(month_data.items(), key=lambda x: int(x[0])):
            day_layout = BoxLayout(orientation='horizontal', size_hint_x=None, width=23.7) 
            
            for category, color in zip(categories, colors):
                value = data[category]
                height = self.calculate_height(value)
                bar = BarWidget(height=height, width=4.2, color=color)
                day_layout.add_widget(bar)
            
            self.chart_layout.add_widget(day_layout)
            
            # Add space between days
            space = BoxLayout(size_hint_x=None, width=1)
            self.chart_layout.add_widget(space)
            
            # Add day label - unused
            day_num = int(day)
            day_name = day_abbr[datetime(2024, 1, day_num).weekday()][:1]  # First letter of day name
            label = Label(text=day_name, size_hint_x=None, width=24) 
            self.day_labels_layout.add_widget(label)
            
            # Add space between labels
            label_space = BoxLayout(size_hint_x=None, width=50)
            self.day_labels_layout.add_widget(label_space)
        
        # Add legend - unused
        for category, color in zip(categories, colors):
            legend_item = ColorLabel(text=category, color=color)
            self.legend_layout.add_widget(legend_item)


    def calculate_height(self, value,max_height=227, max_value=50, min_value=0):
        #TODO: This functionality needs to be reworked completely
        if value <= 50:
            if value < 1 or value > 50:
                raise ValueError("Input value must be between 1 and 50")
            
            output_value = ((value - 1) / 50) * 227
            return output_value
        else:
            return value 