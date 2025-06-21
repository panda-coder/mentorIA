"""Custom widgets for the mentorIA application"""

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class IconButton(Button):
    """Button with icon support"""
    
    def __init__(self, icon_text="", **kwargs):
        super().__init__(**kwargs)
        self.icon_text = icon_text
        if icon_text:
            self.text = f"{icon_text} {self.text}"


class TitleLabel(Label):
    """Styled title label"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '24sp'
        self.bold = True
        self.size_hint_y = None
        self.height = '40dp'


class SectionLayout(BoxLayout):
    """Layout for sections with consistent styling"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10