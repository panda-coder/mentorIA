"""Initial screen for the mentorIA application"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class InitialScreen(Screen):
    """Initial screen that shows when the app starts with no paths created"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_path_callback = None
        self.build_ui()
    
    def build_ui(self):
        """Build the initial screen UI"""
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        # Add some spacing at the top
        main_layout.add_widget(Widget(size_hint_y=0.3))
        
        # Welcome message
        welcome_label = Label(
            text='Start by creating a new path...',
            font_size='24sp',
            color=(0.5, 0.5, 0.5, 1),
            size_hint_y=None,
            height='50dp',
            halign='center'
        )
        welcome_label.bind(size=welcome_label.setter('text_size'))
        main_layout.add_widget(welcome_label)
        
        # Create path button
        create_button = Button(
            text='Create New Path',
            size_hint=(None, None),
            size=('200dp', '50dp'),
            pos_hint={'center_x': 0.5}
        )
        create_button.bind(on_press=self.on_create_path_click)
        main_layout.add_widget(create_button)
        
        # Add spacing at the bottom
        main_layout.add_widget(Widget(size_hint_y=0.3))
        
        self.add_widget(main_layout)
    
    def bind_create_path_callback(self, callback):
        """Bind the create path callback"""
        self.create_path_callback = callback
    
    def on_create_path_click(self, button):
        """Handle create path button click"""
        if self.create_path_callback:
            self.create_path_callback()