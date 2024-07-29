from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from utils import date_utils
from ui.background_layout import BackgroundLayout
from ui.arrow_button import ArrowButton
from ui.column_diagram import ColumnDiagram

class FencingPointsTracker(FloatLayout):
    def __init__(self, data_manager, **kwargs):
        super(FencingPointsTracker, self).__init__(**kwargs)
        self.data_manager = data_manager

        self.seasons = self.data_manager.get_seasons()
        self.current_season_index = 0
        self.current_date = date_utils.get_first_available_date(
            self.data_manager.get_available_months(self.seasons[0])
        )

        self._setup_ui()

    def _setup_ui(self):
        # Background setup
        self.background_layout = BackgroundLayout(size_hint=(None, None), size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(self.background_layout)

        # Month picker setup
        self._setup_month_picker()

        # Season picker setup
        self._setup_season_picker()

        # Statistics table and diagram setup
        self._setup_statistics()

    def _setup_month_picker(self):
        month_picker = BoxLayout(size_hint=(0.35, None), height=60)
        month_picker.pos_hint = {'center_x': 0.64, 'center_y': 0.885}   
        
        self.prev_month_btn = ArrowButton(on_press=self.prev_month)
        self.next_month_btn = ArrowButton(on_press=self.next_month)
        self.month_year_label = Label(
            text=date_utils.get_month_year_text_label(self.current_date),
            bold=True,
            color=(0.2, 0.2, 0.2, 1.0),
            font_size='11sp'
        )
        month_picker.add_widget(self.prev_month_btn)
        month_picker.add_widget(self.month_year_label)
        month_picker.add_widget(self.next_month_btn)
        self.background_layout.add_widget(month_picker)

    def _setup_season_picker(self):
        season_picker = BoxLayout(size_hint=(0.35, None), height=60)
        season_picker.pos_hint = {'center_x': 0.632, 'center_y': 0.834} 
        self.prev_season_btn = ArrowButton(on_press=self.prev_season)
        self.next_season_btn = ArrowButton(on_press=self.next_season)
        self.season_label = Label(
            text=self.seasons[self.current_season_index],
            bold=True,
            color=(0.2, 0.2, 0.2, 1.0),
            font_size='11sp'
        )
        season_picker.add_widget(self.prev_season_btn)
        season_picker.add_widget(self.season_label)
        season_picker.add_widget(self.next_season_btn)
        self.background_layout.add_widget(season_picker)

    def _setup_statistics(self):
        self.data_grid = GridLayout(cols=5, size_hint=(0.85, 0.16))
        self.data_grid.pos_hint = {'center_x': 0.51, 'center_y': 0.605} 
        self.background_layout.add_widget(self.data_grid)
        
        self.diagram = ColumnDiagram(size_hint=(1, 1))
        self.diagram.pos_hint = {'center_x': 0.624, 'center_y': 0.6765}   
        self.background_layout.add_widget(self.diagram)
        
        self.update_data_grid()

    def prev_month(self, instance):
        current_season = self.seasons[self.current_season_index]
        prev_date = date_utils.get_prev_month(self.current_date)
        prev_month_year = date_utils.get_month_year_text(prev_date)
        
        if prev_month_year in self.data_manager.get_available_months(current_season):
            self.current_date = prev_date
        elif self.current_season_index > 0:
            self.current_season_index -= 1
            available_months = self.data_manager.get_available_months(self.seasons[self.current_season_index])
            self.current_date = date_utils.get_last_available_date(available_months)
        
        self.update_labels()

    def next_month(self, instance):
        current_season = self.seasons[self.current_season_index]
        next_date = date_utils.get_next_month(self.current_date)
        next_month_year = date_utils.get_month_year_text(next_date)
        
        if next_month_year in self.data_manager.get_available_months(current_season):
            self.current_date = next_date
        elif self.current_season_index < len(self.seasons) - 1:
            self.current_season_index += 1
            available_months = self.data_manager.get_available_months(self.seasons[self.current_season_index])
            self.current_date = date_utils.get_first_available_date(available_months)
        
        self.update_labels()

    def prev_season(self, instance):
        if self.current_season_index > 0:
            self.current_season_index -= 1
            self.update_season()

    def next_season(self, instance):
        if self.current_season_index < len(self.seasons) - 1:
            self.current_season_index += 1
            self.update_season()

    def update_season(self):
        self.season_label.text = self.seasons[self.current_season_index]
        
        target_month_year = date_utils.get_month_year_text(self.current_date)
        available_months = self.data_manager.get_available_months(self.seasons[self.current_season_index])
        
        if target_month_year in available_months:
            self.current_date = date_utils.parse_month_year(target_month_year)
        else:
            available_dates = [date_utils.parse_month_year(date) for date in available_months]
            closest_date = min(available_dates, key=lambda d: abs(d - self.current_date))
            self.current_date = closest_date
        
        self.update_labels()

    def update_labels(self):
        self.month_year_label.text = date_utils.get_month_year_text_label(self.current_date)
        self.season_label.text = self.seasons[self.current_season_index]
        self.update_data_grid()

    def update_data_grid(self):
        self.data_grid.clear_widgets()
        self.data_grid.spacing = (0, 0)
        
        current_season = self.seasons[self.current_season_index]
        current_month_year = date_utils.get_month_year_text(self.current_date)
        weekly_totals = self.data_manager.calculate_weekly_totals(current_season, current_month_year)
        
        for week, totals in weekly_totals.items():
            self.data_grid.add_widget(Label(text=f"Week {week}", color=(0,0,0,0)))
            for category in ['Victory', 'Defeat', 'Touches Scored', 'Touches Received']:
                value = str(totals.get(category, "N/A"))
                self.data_grid.add_widget(Label(text=value, font_size='10sp', bold=True))
        
        # Update diagram with the month's data
        month_data = self.data_manager.get_month_data(current_season, current_month_year)
        self.diagram.update_diagram(month_data)