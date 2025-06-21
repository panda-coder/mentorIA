"""About dialog for the mentorIA application"""

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class AboutDialog:
    """About dialog showing application information"""
    
    def __init__(self):
        self.popup = None
    
    def show(self):
        """Show the about dialog"""
        if self.popup is None:
            self.popup = self._build_popup()
        
        self.popup.open()
    
    def _build_popup(self):
        """Build the about dialog popup"""
        # Content layout
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title_label = Label(
            text='mentorIA',
            font_size='28sp',
            size_hint_y=None,
            height='40dp',
            bold=True
        )
        content.add_widget(title_label)
        
        # Version
        version_label = Label(
            text='Version: 0.1.0',
            font_size='18sp',
            size_hint_y=None,
            height='30dp'
        )
        content.add_widget(version_label)
        
        # Description
        description_label = Label(
            text='A self-study studio designed to leverage Large Language Models (LLMs) to build customized study sessions.',
            font_size='14sp',
            text_size=(None, None),
            halign='center',
            valign='middle',
            size_hint_y=None,
            height='60dp'
        )
        content.add_widget(description_label)
        
        # GitHub link
        github_label = Label(
            text='https://github.com/panda-coder/mentorIA',
            font_size='14sp',
            color=(0.2, 0.6, 1, 1),
            size_hint_y=None,
            height='30dp'
        )
        content.add_widget(github_label)
        
        # OK button
        ok_button = Button(
            text='OK',
            size_hint=(None, None),
            size=('100dp', '40dp'),
            pos_hint={'center_x': 0.5}
        )
        ok_button.bind(on_press=self._close_dialog)
        content.add_widget(ok_button)
        
        # Create popup
        popup = Popup(
            title='About mentorIA',
            content=content,
            size_hint=(None, None),
            size=('500dp', '350dp'),
            auto_dismiss=True
        )
        
        return popup
    
    def _close_dialog(self, button):
        """Close the about dialog"""
        if self.popup:
            self.popup.dismiss()