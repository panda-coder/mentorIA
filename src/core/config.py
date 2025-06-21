"""Configuration settings for the mentorIA application"""

class WindowConfig:
    """Window configuration settings"""
    
    # Window modes
    NORMAL = "normal"           # Standard window with system title bar
    BORDERLESS = "borderless"   # No border, custom title bar
    FULLSCREEN = "fullscreen"   # Fullscreen mode
    
    # Default settings
    DEFAULT_WIDTH = 1000
    DEFAULT_HEIGHT = 700
    MIN_WIDTH = 800
    MIN_HEIGHT = 600
    
    # Current mode (can be changed at runtime)
    WINDOW_MODE = BORDERLESS  # Change this to NORMAL for standard window
    
    # Title bar settings
    TITLE_BAR_HEIGHT = 30
    TITLE_BAR_COLOR = (0.2, 0.2, 0.2, 1)  # Dark gray
    TITLE_TEXT_COLOR = (1, 1, 1, 1)       # White
    
    # Window control button colors
    MINIMIZE_BUTTON_COLOR = (0.3, 0.3, 0.3, 1)  # Gray
    CLOSE_BUTTON_COLOR = (0.8, 0.2, 0.2, 1)     # Red


class AppConfig:
    """General application configuration"""
    
    APP_NAME = "mentorIA"
    VERSION = "0.1.0"
    
    # Theme settings
    THEME_MODE = "light"  # "light" or "dark"
    
    # Default values
    DEFAULT_SUBJECT = "Japanese JLPT1"