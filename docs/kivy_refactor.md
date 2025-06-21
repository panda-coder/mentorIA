# Kivy Refactor Documentation

## Overview

The mentorIA application has been successfully refactored from Flet to Kivy. The new implementation is located in the `src/` directory and provides the same functionality with improved stability and cross-platform compatibility.

## Directory Structure

```
src/
├── core/
│   ├── __init__.py
│   ├── app.py              # Main application entry point
│   └── containers.py       # Dependency injection container
├── presentation/
│   ├── __init__.py
│   ├── main_app.py         # Main Kivy application class
│   ├── screens/
│   │   ├── __init__.py
│   │   ├── initial_screen.py      # Welcome screen
│   │   ├── about_dialog.py        # About dialog
│   │   └── create_path_dialog.py  # Create path dialog
│   └── widgets/
│       ├── __init__.py
│       └── custom_widgets.py      # Custom UI components
└── main.py                 # Application entry point
```

## Key Components

### 1. MentorIAApp (main_app.py)
The main Kivy application class that:
- Sets up the window properties (1000x700, minimum 800x600)
- Creates the action bar menu system
- Manages screen navigation
- Handles dialog interactions

### 2. InitialScreen (initial_screen.py)
The welcome screen that displays:
- Welcome message: "Start by creating a new path..."
- "Create New Path" button
- Clean, centered layout

### 3. AboutDialog (about_dialog.py)
Modal popup showing:
- Application name and version
- Description
- GitHub link
- OK button to close

### 4. CreatePathDialog (create_path_dialog.py)
Modal popup for creating learning paths:
- Instructions text
- Multi-line text input (pre-filled with "Japanese JLPT1")
- Cancel and Create buttons
- Input validation

## Menu Structure

The application features an action bar with three main menu groups:

### Paths Menu
- **Create**: Opens the create path dialog
- **Load**: Placeholder for loading existing paths

### Configuration Menu
- **LLM Providers**: Placeholder for LLM configuration

### Help Menu
- **About**: Opens the about dialog

## Key Features

### 1. Responsive Design
- Minimum window size constraints
- Flexible layouts that adapt to window resizing
- Proper spacing and padding throughout

### 2. Event Handling
- Menu item clicks
- Button interactions
- Dialog management
- Callback system for inter-component communication

### 3. Error Handling
- Try-catch blocks in critical methods
- Graceful error reporting
- Fallback UI elements

### 4. Dependency Injection
- Uses the same dependency-injector pattern as the Flet version
- Clean separation of concerns
- Easy testing and maintenance

## Advantages of Kivy Over Flet

### 1. Stability
- More mature framework with extensive testing
- Better error handling and recovery
- Fewer crashes and unexpected behaviors

### 2. Cross-Platform Compatibility
- Native support for Windows, macOS, Linux
- Mobile platform support (Android, iOS)
- Consistent behavior across platforms

### 3. Performance
- Hardware-accelerated graphics with OpenGL
- Efficient rendering pipeline
- Better memory management

### 4. Customization
- Extensive theming and styling options
- Custom widget creation
- Fine-grained control over UI elements

### 5. Community and Documentation
- Large, active community
- Comprehensive documentation
- Extensive examples and tutorials

## Running the Application

### Prerequisites
```bash
# Install dependencies
uv pip install kivy kivymd dependency-injector
```

### Launch
```bash
# Run the Kivy version
uv run python src/main.py
```

## Migration Notes

### What Was Preserved
- ✅ Same application architecture
- ✅ Dependency injection pattern
- ✅ Screen management concept
- ✅ Dialog-based interactions
- ✅ Menu structure and functionality
- ✅ Initial screen layout and behavior

### What Changed
- 🔄 UI framework: Flet → Kivy
- 🔄 Widget types: Flet widgets → Kivy widgets
- 🔄 Event handling: Flet events → Kivy events
- 🔄 Layout system: Flet containers → Kivy layouts
- 🔄 Dialog system: Flet AlertDialog → Kivy Popup

### Code Comparison

#### Flet Version (Button)
```python
ft.ElevatedButton(
    "Create New Path",
    icon=ft.Icons.ADD,
    on_click=self._on_create_path_click
)
```

#### Kivy Version (Button)
```python
Button(
    text='Create New Path',
    size_hint=(None, None),
    size=('200dp', '50dp'),
    pos_hint={'center_x': 0.5}
)
button.bind(on_press=self.on_create_path_click)
```

## Testing Results

### ✅ Successful Tests
- Application startup and initialization
- Window creation and sizing
- Menu system functionality
- Screen navigation
- Dialog creation and display
- Button interactions
- Text input handling

### 🔧 System Requirements
- Python 3.12+
- OpenGL support
- SDL2 (automatically installed with Kivy)
- X11/Wayland on Linux (standard desktop environments)

## Future Enhancements

### Planned Features
1. **Material Design**: Integrate KivyMD for modern UI components
2. **Themes**: Dark/light mode support
3. **Animations**: Smooth transitions between screens
4. **Icons**: Add proper icons to menu items and buttons
5. **Responsive Layout**: Better mobile/tablet support
6. **Settings Screen**: User preferences and configuration
7. **Path Management**: Full CRUD operations for learning paths

### Technical Improvements
1. **Configuration System**: External config files
2. **Logging**: Structured logging system
3. **Testing**: Unit tests for all components
4. **Packaging**: Standalone executables for distribution
5. **Internationalization**: Multi-language support

## Conclusion

The Kivy refactor successfully addresses the stability issues encountered with Flet while maintaining all the original functionality. The new implementation provides:

- **Better stability** and error handling
- **Cross-platform compatibility**
- **Performance improvements**
- **Extensibility** for future features
- **Professional UI** with customization options

The application is now ready for further development and can serve as a solid foundation for implementing the full mentorIA feature set.