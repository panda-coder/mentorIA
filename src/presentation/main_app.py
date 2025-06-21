"""Main Kivy application class"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionGroup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

from presentation.screens.initial_screen import InitialScreen
from presentation.screens.about_dialog import AboutDialog
from presentation.screens.create_path_dialog import CreatePathDialog
from core.config import WindowConfig, AppConfig


class MentorIAApp(App):
    """Main mentorIA Kivy application"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = AppConfig.APP_NAME
        self.screen_manager = None
        self.about_dialog = None
        self.create_path_dialog = None
        
        # Window dragging variables
        self._drag_start_pos = None
        self._window_start_pos = None
        
    def build(self):
        """Build the main application UI"""
        try:
            # Set window properties
            Window.size = (WindowConfig.DEFAULT_WIDTH, WindowConfig.DEFAULT_HEIGHT)
            Window.minimum_width = WindowConfig.MIN_WIDTH
            Window.minimum_height = WindowConfig.MIN_HEIGHT
            
            # Apply window mode
            if WindowConfig.WINDOW_MODE == WindowConfig.BORDERLESS:
                Window.borderless = True
            elif WindowConfig.WINDOW_MODE == WindowConfig.FULLSCREEN:
                Window.fullscreen = True
            # NORMAL mode doesn't need special settings
            
            # Create main layout
            main_layout = BoxLayout(orientation='vertical')
            
            # Create custom title bar only for borderless mode
            if WindowConfig.WINDOW_MODE == WindowConfig.BORDERLESS:
                title_bar = self.create_title_bar()
                main_layout.add_widget(title_bar)
            
            # Create action bar (menu)
            action_bar = self.create_action_bar()
            main_layout.add_widget(action_bar)
            
            # Create screen manager
            self.screen_manager = ScreenManager()
            
            # Add initial screen
            initial_screen = InitialScreen(name='initial')
            initial_screen.bind_create_path_callback(self.show_create_path_dialog)
            self.screen_manager.add_widget(initial_screen)
            
            main_layout.add_widget(self.screen_manager)
            
            # Initialize dialogs
            self.about_dialog = AboutDialog()
            self.create_path_dialog = CreatePathDialog()
            self.create_path_dialog.bind_create_callback(self.on_path_created)
            
            return main_layout
            
        except Exception as ex:
            print(f"ERROR in MentorIAApp.build(): {ex}")
            import traceback
            traceback.print_exc()
            return Label(text=f"Error building app: {ex}")
    
    def create_action_bar(self):
        """Create the application menu bar"""
        action_bar = ActionBar()
        
        action_view = ActionView()
        action_view.add_widget(ActionPrevious(title='mentorIA', with_previous=False))
        
        # Paths menu
        paths_group = ActionGroup(text='Paths', mode='spinner')
        paths_group.add_widget(ActionButton(text='Create', on_press=self.show_create_path_dialog))
        paths_group.add_widget(ActionButton(text='Load', on_press=self.on_load_path))
        action_view.add_widget(paths_group)
        
        # Configuration menu
        config_group = ActionGroup(text='Configuration', mode='spinner')
        config_group.add_widget(ActionButton(text='LLM Providers', on_press=self.on_llm_providers))
        action_view.add_widget(config_group)
        
        # Help menu
        help_group = ActionGroup(text='Help', mode='spinner')
        help_group.add_widget(ActionButton(text='About', on_press=self.show_about_dialog))
        action_view.add_widget(help_group)
        
        action_bar.add_widget(action_view)
        return action_bar
    
    def create_title_bar(self):
        """Create a custom title bar for borderless window"""
        title_bar = BoxLayout(
            orientation='horizontal', 
            size_hint_y=None, 
            height=f'{WindowConfig.TITLE_BAR_HEIGHT}dp'
        )
        
        # Add background color
        with title_bar.canvas.before:
            Color(*WindowConfig.TITLE_BAR_COLOR)
            title_bar.bg_rect = Rectangle(size=title_bar.size, pos=title_bar.pos)
        
        # Bind to update background when size/position changes
        title_bar.bind(size=self._update_title_bar_bg, pos=self._update_title_bar_bg)
        
        # App title (draggable area)
        title_label = Label(
            text=AppConfig.APP_NAME,
            color=WindowConfig.TITLE_TEXT_COLOR,
            size_hint_x=1,
            font_size='14sp'
        )
        
        # Make title bar draggable
        title_label.bind(on_touch_down=self._on_title_bar_touch_down)
        title_label.bind(on_touch_move=self._on_title_bar_touch_move)
        
        title_bar.add_widget(title_label)
        
        # Window control buttons
        controls_layout = BoxLayout(orientation='horizontal', size_hint_x=None, width='90dp')
        
        # Minimize button
        minimize_btn = Button(
            text='−',
            size_hint=(None, None),
            size=(f'{WindowConfig.TITLE_BAR_HEIGHT}dp', f'{WindowConfig.TITLE_BAR_HEIGHT}dp'),
            background_color=WindowConfig.MINIMIZE_BUTTON_COLOR
        )
        minimize_btn.bind(on_press=self._minimize_window)
        controls_layout.add_widget(minimize_btn)
        
        # Close button
        close_btn = Button(
            text='×',
            size_hint=(None, None),
            size=(f'{WindowConfig.TITLE_BAR_HEIGHT}dp', f'{WindowConfig.TITLE_BAR_HEIGHT}dp'),
            background_color=WindowConfig.CLOSE_BUTTON_COLOR
        )
        close_btn.bind(on_press=self._close_window)
        controls_layout.add_widget(close_btn)
        
        title_bar.add_widget(controls_layout)
        
        return title_bar
    
    def _update_title_bar_bg(self, instance, value):
        """Update title bar background rectangle"""
        instance.bg_rect.pos = instance.pos
        instance.bg_rect.size = instance.size
    
    def _on_title_bar_touch_down(self, instance, touch):
        """Handle title bar touch down for dragging"""
        if instance.collide_point(*touch.pos):
            self._drag_start_pos = touch.pos
            self._window_start_pos = (Window.left, Window.top)
            return True
        return False
    
    def _on_title_bar_touch_move(self, instance, touch):
        """Handle title bar dragging"""
        if hasattr(self, '_drag_start_pos') and self._drag_start_pos:
            dx = touch.pos[0] - self._drag_start_pos[0]
            dy = touch.pos[1] - self._drag_start_pos[1]
            
            Window.left = self._window_start_pos[0] + dx
            Window.top = self._window_start_pos[1] - dy  # Invert Y for screen coordinates
    
    def _minimize_window(self, button):
        """Minimize the window"""
        # Note: Kivy doesn't have built-in minimize, this is a placeholder
        print("Minimize functionality not available in Kivy")
    
    def _close_window(self, button):
        """Close the application"""
        self.stop()
    
    def show_about_dialog(self, *args):
        """Show the about dialog"""
        try:
            self.about_dialog.show()
        except Exception as ex:
            print(f"Error showing about dialog: {ex}")
    
    def show_create_path_dialog(self, *args):
        """Show the create path dialog"""
        try:
            self.create_path_dialog.show()
        except Exception as ex:
            print(f"Error showing create path dialog: {ex}")
    
    def on_load_path(self, *args):
        """Handle load path menu item"""
        print("Load path functionality not implemented yet")
    
    def on_llm_providers(self, *args):
        """Handle LLM providers menu item"""
        print("LLM Providers configuration not implemented yet")
    
    def on_path_created(self, subject):
        """Handle path creation"""
        print(f"Path created for subject: {subject}")
        # TODO: Implement actual path creation logic