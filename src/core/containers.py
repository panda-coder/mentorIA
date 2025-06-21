"""Dependency injection containers for the Kivy application"""

from dependency_injector import containers, providers
from presentation.main_app import MentorIAApp


class Container(containers.DeclarativeContainer):
    """Main dependency injection container"""
    
    # Configuration
    config = providers.Configuration()
    
    # Main application
    main_app = providers.Factory(MentorIAApp)