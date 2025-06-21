# Framework Comparison: Flet vs Kivy

## Overview

This document compares the original Flet implementation (now removed) with the current Kivy implementation (`src/`) of the mentorIA application.

## Side-by-Side Comparison

### Application Entry Point

#### Flet Version
```python
# src/core/app.py
from flet import app
from core.containers import Container

def main(page):
    container = Container()
    container.wire(modules=[__name__])
    main_page = container.main_page()
    main_page.build(page)
    return None

def run():
    app(target=main)
```

#### Kivy Version
```python
# src/core/app.py
from core.containers import Container

def run():
    try:
        container = Container()
        container.wire(modules=[__name__])
        app = container.main_app()
        app.run()
    except Exception as ex:
        print(f"ERROR in app.run(): {ex}")
        import traceback
        traceback.print_exc()
```

### Main Application Class

#### Flet Version
```python
# src/presentation/win/main.py
class MainPage:
    def build(self, page: ft.Page):
        self.page = page
        self.page.window_frameless = True
        self.page.bgcolor = ft.Colors.WHITE
        # ... setup methods
```

#### Kivy Version
```python
# src/presentation/main_app.py
class MentorIAApp(App):
    def build(self):
        Window.size = (1000, 700)
        Window.minimum_width = 800
        Window.minimum_height = 600
        
        main_layout = BoxLayout(orientation='vertical')
        # ... build UI
        return main_layout
```

### Button Creation

#### Flet Version
```python
ft.ElevatedButton(
    "Create New Path",
    icon=ft.Icons.ADD,
    on_click=self._on_create_path_click
)
```

#### Kivy Version
```python
create_button = Button(
    text='Create New Path',
    size_hint=(None, None),
    size=('200dp', '50dp'),
    pos_hint={'center_x': 0.5}
)
create_button.bind(on_press=self.on_create_path_click)
```

### Dialog Creation

#### Flet Version
```python
# src/presentation/screens/about_dialog.py
ft.AlertDialog(
    modal=True,
    title=ft.Text("About mentorIA"),
    content=ft.Container(...),
    actions=[
        ft.TextButton("OK", on_click=self._close_dialog)
    ]
)
```

#### Kivy Version
```python
# src/presentation/screens/about_dialog.py
Popup(
    title='About mentorIA',
    content=content,
    size_hint=(None, None),
    size=('500dp', '350dp'),
    auto_dismiss=True
)
```

### Layout Systems

#### Flet Version
```python
ft.Column([
    ft.Text("Welcome"),
    ft.ElevatedButton("Click me")
], alignment=ft.MainAxisAlignment.CENTER)
```

#### Kivy Version
```python
BoxLayout(orientation='vertical', padding=50, spacing=30)
layout.add_widget(Label(text='Welcome'))
layout.add_widget(Button(text='Click me'))
```

## Key Differences

### 1. Architecture Pattern

| Aspect | Flet | Kivy |
|--------|------|------|
| **App Model** | Function-based with page parameter | Class-based inheritance from App |
| **UI Building** | Declarative with nested widgets | Imperative with add_widget() |
| **Event Handling** | Direct callback assignment | bind() method for events |

### 2. Widget System

| Feature | Flet | Kivy |
|---------|------|------|
| **Widget Creation** | `ft.Widget(properties)` | `Widget(properties)` then `add_widget()` |
| **Styling** | Built-in Material Design | Custom styling with properties |
| **Layout** | Automatic with containers | Manual with layout widgets |

### 3. Dialog Handling

| Aspect | Flet | Kivy |
|--------|------|------|
| **Dialog Type** | AlertDialog | Popup |
| **Modal Behavior** | Built-in modal support | auto_dismiss property |
| **Actions** | actions list | Custom button layout |

### 4. Error Handling

| Framework | Error Handling |
|-----------|----------------|
| **Flet** | Limited built-in error handling, prone to crashes |
| **Kivy** | Robust error handling, graceful degradation |

### 5. Performance

| Metric | Flet | Kivy |
|--------|------|------|
| **Startup Time** | Fast | Moderate (OpenGL initialization) |
| **Memory Usage** | Lower | Higher (graphics acceleration) |
| **Rendering** | Web-based | OpenGL hardware acceleration |
| **Responsiveness** | Good | Excellent |

### 6. Platform Support

| Platform | Flet | Kivy |
|----------|------|------|
| **Windows** | ✅ Good | ✅ Excellent |
| **macOS** | ✅ Good | ✅ Excellent |
| **Linux** | ⚠️ Issues with some DEs | ✅ Excellent |
| **Mobile** | ❌ No | ✅ Android/iOS |

## Migration Benefits

### ✅ Advantages of Kivy

1. **Stability**: No more crashes on menu clicks
2. **Performance**: Hardware-accelerated graphics
3. **Maturity**: Well-tested, stable framework
4. **Flexibility**: Extensive customization options
5. **Mobile Support**: Can target mobile platforms
6. **Community**: Large, active community

### ⚠️ Trade-offs

1. **Learning Curve**: More complex than Flet
2. **Setup**: Requires OpenGL and system dependencies
3. **Code Volume**: More verbose than Flet
4. **Styling**: Requires more manual styling work

## Conclusion

The migration from Flet to Kivy addresses the critical stability issues while providing a more robust foundation for future development. While Kivy requires more code and setup, it offers superior stability, performance, and extensibility.

### Recommendation

**Use Kivy (`src/`)** for:
- Production applications
- Cross-platform deployment
- Applications requiring stability
- Projects with complex UI requirements

**Consider Flet (`src/`)** for:
- Rapid prototyping
- Simple applications
- Web-based deployment
- Quick demos and MVPs

The Kivy implementation is recommended for the mentorIA project due to its stability and professional-grade capabilities.