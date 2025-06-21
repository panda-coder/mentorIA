"""Create path dialog for the mentorIA application"""

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from core.config import AppConfig


class CreatePathDialog:
    """Dialog for creating a new learning path"""
    
    def __init__(self):
        self.popup = None
        self.subject_input = None
        self.create_callback = None
    
    def show(self):
        """Show the create path dialog"""
        if self.popup is None:
            self.popup = self._build_popup()
        
        # Reset the input field
        if self.subject_input:
            self.subject_input.text = AppConfig.DEFAULT_SUBJECT
        
        self.popup.open()
    
    def bind_create_callback(self, callback):
        """Bind the create callback"""
        self.create_callback = callback
    
    def _build_popup(self):
        """Build the create path dialog popup"""
        # Content layout
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Instructions
        instructions_label = Label(
            text='Define the subject or topic you want to study:',
            font_size='16sp',
            size_hint_y=None,
            height='30dp',
            halign='left'
        )
        instructions_label.bind(size=instructions_label.setter('text_size'))
        content.add_widget(instructions_label)
        
        # Subject input
        self.subject_input = TextInput(
            text=AppConfig.DEFAULT_SUBJECT,
            multiline=True,
            size_hint_y=None,
            height='120dp',
            hint_text=f'Enter the subject you want to study (e.g., {AppConfig.DEFAULT_SUBJECT})'
        )
        content.add_widget(self.subject_input)
        
        # Button layout
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height='50dp')
        
        # Cancel button
        cancel_button = Button(
            text='Cancel',
            size_hint_x=0.5
        )
        cancel_button.bind(on_press=self._close_dialog)
        button_layout.add_widget(cancel_button)
        
        # Create button
        create_button = Button(
            text='Create',
            size_hint_x=0.5
        )
        create_button.bind(on_press=self._create_path)
        button_layout.add_widget(create_button)
        
        content.add_widget(button_layout)
        
        # Create popup
        popup = Popup(
            title='Create New Learning Path',
            content=content,
            size_hint=(None, None),
            size=('600dp', '300dp'),
            auto_dismiss=False
        )
        
        return popup
    
    def _create_path(self, button):
        """Handle create path action"""
        subject = self.subject_input.text.strip()
        
        if not subject:
            # TODO: Show error message
            print("Please enter a subject")
            return
        
        # Call the create callback
        if self.create_callback:
            self.create_callback(subject)
        
        self._close_dialog(button)
    
    def _close_dialog(self, button):
        """Close the create path dialog"""
        if self.popup:
            self.popup.dismiss()