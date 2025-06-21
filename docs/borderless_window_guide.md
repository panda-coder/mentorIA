# Borderless Window Implementation Guide

## Overview

The Kivy version of mentorIA supports multiple window modes, including a borderless window mode that removes the system title bar and provides a custom title bar with window controls. This guide explains how to use and customize the borderless window functionality.

## Window Modes

### 1. Normal Mode (Default System Window)
- Uses the standard system title bar
- Standard window controls (minimize, maximize, close)
- Can be moved and resized using system controls

### 2. Borderless Mode (Custom Title Bar)
- Removes the system title bar (`Window.borderless = True`)
- Provides a custom title bar with drag functionality
- Custom minimize and close buttons
- Modern, clean appearance

### 3. Fullscreen Mode
- Occupies the entire screen
- No title bar or window controls
- Suitable for presentation or immersive modes

## Configuration

### Setting Window Mode

Edit `src/core/config.py` to change the window mode:

```python
class WindowConfig:
    # Window modes
    NORMAL = "normal"           # Standard window with system title bar
    BORDERLESS = "borderless"   # No border, custom title bar
    FULLSCREEN = "fullscreen"   # Fullscreen mode
    
    # Set the desired mode here
    WINDOW_MODE = BORDERLESS    # Change this to NORMAL or FULLSCREEN
```

### Customizing Window Properties

```python
class WindowConfig:
    # Window size settings
    DEFAULT_WIDTH = 1000
    DEFAULT_HEIGHT = 700
    MIN_WIDTH = 800
    MIN_HEIGHT = 600
    
    # Title bar appearance
    TITLE_BAR_HEIGHT = 30
    TITLE_BAR_COLOR = (0.2, 0.2, 0.2, 1)  # Dark gray
    TITLE_TEXT_COLOR = (1, 1, 1, 1)       # White
    
    # Button colors
    MINIMIZE_BUTTON_COLOR = (0.3, 0.3, 0.3, 1)  # Gray
    CLOSE_BUTTON_COLOR = (0.8, 0.2, 0.2, 1)     # Red
```

## Features

### Borderless Window Features

#### ✅ **Custom Title Bar**
- Dark gray background with white text
- Shows application name ("mentorIA")
- 30dp height (configurable)

#### ✅ **Window Dragging**
- Click and drag the title bar to move the window
- Smooth dragging experience
- Proper coordinate handling

#### ✅ **Window Controls**
- **Minimize Button** (−): Currently shows a message (Kivy limitation)
- **Close Button** (×): Properly closes the application

#### ✅ **Responsive Design**
- Title bar adapts to window width
- Proper background rendering
- Maintains aspect ratio

## Implementation Details

### Key Components

#### 1. Window Mode Detection
```python
# In main_app.py build() method
if WindowConfig.WINDOW_MODE == WindowConfig.BORDERLESS:
    Window.borderless = True
    title_bar = self.create_title_bar()
    main_layout.add_widget(title_bar)
```

#### 2. Custom Title Bar Creation
```python
def create_title_bar(self):
    title_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height='30dp')
    
    # Background color
    with title_bar.canvas.before:
        Color(*WindowConfig.TITLE_BAR_COLOR)
        title_bar.bg_rect = Rectangle(size=title_bar.size, pos=title_bar.pos)
    
    # App title (draggable)
    title_label = Label(text=AppConfig.APP_NAME, color=WindowConfig.TITLE_TEXT_COLOR)
    title_label.bind(on_touch_down=self._on_title_bar_touch_down)
    title_label.bind(on_touch_move=self._on_title_bar_touch_move)
    
    # Window control buttons
    # ... minimize and close buttons
```

#### 3. Drag Functionality
```python
def _on_title_bar_touch_down(self, instance, touch):
    if instance.collide_point(*touch.pos):
        self._drag_start_pos = touch.pos
        self._window_start_pos = (Window.left, Window.top)
        return True
    return False

def _on_title_bar_touch_move(self, instance, touch):
    if hasattr(self, '_drag_start_pos') and self._drag_start_pos:
        dx = touch.pos[0] - self._drag_start_pos[0]
        dy = touch.pos[1] - self._drag_start_pos[1]
        
        Window.left = self._window_start_pos[0] + dx
        Window.top = self._window_start_pos[1] - dy
```

## Usage Examples

### Running Different Window Modes

#### Borderless Mode (Default)
```bash
uv run python src/main.py
```

#### Normal Mode
1. Edit `src/core/config.py`:
   ```python
   WINDOW_MODE = NORMAL
   ```
2. Run the application:
   ```bash
   uv run python src/main.py
   ```

#### Fullscreen Mode
1. Edit `src/core/config.py`:
   ```python
   WINDOW_MODE = FULLSCREEN
   ```
2. Run the application:
   ```bash
   uv run python src/main.py
   ```

## Customization Options

### 1. Title Bar Styling

#### Change Colors
```python
# Dark theme
TITLE_BAR_COLOR = (0.1, 0.1, 0.1, 1)      # Very dark gray
TITLE_TEXT_COLOR = (0.9, 0.9, 0.9, 1)     # Light gray

# Light theme
TITLE_BAR_COLOR = (0.9, 0.9, 0.9, 1)      # Light gray
TITLE_TEXT_COLOR = (0.1, 0.1, 0.1, 1)     # Dark gray

# Accent color theme
TITLE_BAR_COLOR = (0.2, 0.4, 0.8, 1)      # Blue
TITLE_TEXT_COLOR = (1, 1, 1, 1)           # White
```

#### Change Height
```python
TITLE_BAR_HEIGHT = 40  # Taller title bar
TITLE_BAR_HEIGHT = 25  # Shorter title bar
```

### 2. Button Customization

#### Different Button Styles
```python
# Flat buttons
MINIMIZE_BUTTON_COLOR = (0, 0, 0, 0)       # Transparent
CLOSE_BUTTON_COLOR = (0, 0, 0, 0)          # Transparent

# Colorful buttons
MINIMIZE_BUTTON_COLOR = (0.2, 0.6, 0.2, 1) # Green
CLOSE_BUTTON_COLOR = (0.8, 0.2, 0.2, 1)    # Red
```

### 3. Adding More Controls

You can extend the title bar with additional buttons:

```python
# In create_title_bar() method
# Add maximize button
maximize_btn = Button(
    text='□',
    size_hint=(None, None),
    size=(f'{WindowConfig.TITLE_BAR_HEIGHT}dp', f'{WindowConfig.TITLE_BAR_HEIGHT}dp'),
    background_color=(0.3, 0.3, 0.3, 1)
)
maximize_btn.bind(on_press=self._maximize_window)
controls_layout.add_widget(maximize_btn)
```

## Platform Considerations

### Windows
- ✅ Full support for borderless windows
- ✅ Proper window dragging
- ✅ Window controls work correctly

### macOS
- ✅ Borderless windows supported
- ⚠️ May need additional handling for macOS-specific behaviors
- ✅ Dragging functionality works

### Linux
- ✅ Works on most desktop environments
- ⚠️ Some window managers may have specific behaviors
- ✅ Tested on Ubuntu with GNOME/Wayland

## Limitations

### Current Limitations

1. **Minimize Functionality**: Kivy doesn't provide built-in window minimize functionality
2. **Maximize/Restore**: Not implemented (can be added with platform-specific code)
3. **Window Snapping**: System window snapping may not work in borderless mode
4. **Taskbar Integration**: May have different behavior compared to normal windows

### Workarounds

#### 1. Minimize Button
```python
def _minimize_window(self, button):
    # Platform-specific minimize code could be added here
    # For now, we hide the window
    Window.minimize()  # This may not work on all platforms
```

#### 2. Double-click to Maximize
```python
def _on_title_bar_double_click(self, instance, touch):
    # Toggle between normal and maximized
    if Window.size == (Window.system_size):
        Window.size = (WindowConfig.DEFAULT_WIDTH, WindowConfig.DEFAULT_HEIGHT)
    else:
        Window.maximize()  # Platform-specific implementation needed
```

## Best Practices

### 1. User Experience
- Always provide a way to close the application
- Make the draggable area clearly visible
- Ensure the title bar is easily distinguishable

### 2. Visual Design
- Use consistent colors with your application theme
- Maintain adequate contrast for text readability
- Keep button sizes touch-friendly (minimum 30dp)

### 3. Performance
- Update background rectangles only when necessary
- Use efficient event handling for dragging
- Avoid complex graphics in the title bar

## Troubleshooting

### Common Issues

#### 1. Window Not Draggable
**Problem**: Title bar doesn't respond to drag gestures
**Solution**: Check that touch events are properly bound and collision detection works

#### 2. Background Not Updating
**Problem**: Title bar background doesn't resize with window
**Solution**: Ensure the `_update_title_bar_bg` method is properly bound

#### 3. Buttons Not Working
**Problem**: Window control buttons don't respond
**Solution**: Verify button event bindings and callback methods

### Debug Tips

#### Enable Debug Logging
```python
# Add to main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Test Touch Events
```python
def _on_title_bar_touch_down(self, instance, touch):
    print(f"Touch down at: {touch.pos}")
    print(f"Widget bounds: {instance.pos}, {instance.size}")
    # ... rest of method
```

## Conclusion

The borderless window implementation provides a modern, customizable alternative to standard system windows. While there are some platform-specific limitations, the implementation offers a solid foundation for creating professional-looking applications with custom window controls.

The configuration-based approach makes it easy to switch between window modes and customize the appearance to match your application's design requirements.