# mentorIA - Kivy Version

## 🎯 Overview

This is the Kivy-based version of mentorIA, a self-study studio designed to leverage Large Language Models (LLMs) to build customized study sessions. This version addresses stability issues found in the original Flet implementation.

## 🚀 Quick Start

### Using Taskfile (Recommended)

This project includes a `Taskfile.yml` for easy task management. Install [Task](https://taskfile.dev/) and use these commands:

```bash
# Show all available tasks
task --list

# Install dependencies and run the application
task setup

# Run the application (default: borderless mode)
task run

# Run in different window modes
task run-normal      # Standard window with title bar
task run-borderless  # Borderless window (default)
task run-fullscreen  # Fullscreen mode

# Development tasks
task dev            # Run in development mode
task clean          # Clean up cache files
task info           # Show project information

# Configuration management
task config-show    # Show current window configuration
task config-reset   # Reset to default configuration
```

### Manual Setup

### Prerequisites
- Python 3.12+
- OpenGL support (standard on most systems)

### Installation & Running
```bash
# Install dependencies
uv pip install kivy kivymd dependency-injector

# Run the application
uv run python src/main.py
```

## 📁 Project Structure

```
src/                           # Kivy implementation
├── core/
│   ├── app.py                 # Application entry point
│   └── containers.py          # Dependency injection
├── presentation/
│   ├── main_app.py           # Main Kivy app class
│   ├── screens/              # UI screens
│   │   ├── initial_screen.py
│   │   ├── about_dialog.py
│   │   └── create_path_dialog.py
│   └── widgets/              # Custom widgets
└── main.py                   # Entry point

docs/                          # Documentation
├── kivy_refactor.md          # Detailed refactor docs
└── framework_comparison.md   # Flet vs Kivy comparison
```

## ✨ Features

### Current Features
- ✅ **Stable UI**: No crashes on menu interactions
- ✅ **Cross-platform**: Windows, macOS, Linux support
- ✅ **Borderless Window**: Custom title bar with drag functionality
- ✅ **Multiple Window Modes**: Normal, Borderless, Fullscreen
- ✅ **Responsive Design**: Minimum 800x600, scales to 1000x700
- ✅ **Menu System**: Paths, Configuration, Help menus
- ✅ **Create Path Dialog**: Multi-line input with validation
- ✅ **About Dialog**: Application information
- ✅ **Error Handling**: Graceful error management
- ✅ **Configuration System**: Easy customization of window appearance

### Menu Structure
- **Paths**
  - Create: Opens path creation dialog
  - Load: (Placeholder for future implementation)
- **Configuration**
  - LLM Providers: (Placeholder for future implementation)
- **Help**
  - About: Shows application information

## 🎨 Window Modes

The application supports three window modes:

### 1. Borderless Mode (Default)
- Custom title bar with drag functionality
- Minimize and close buttons
- Modern, clean appearance
- No system window border

### 2. Normal Mode
- Standard system title bar
- All system window controls
- Traditional window appearance

### 3. Fullscreen Mode
- Occupies entire screen
- No title bar or controls
- Immersive experience

### Switching Window Modes

Edit `src/core/config.py`:

```python
# For borderless window (default)
WINDOW_MODE = WindowConfig.BORDERLESS

# For normal window with system title bar
WINDOW_MODE = WindowConfig.NORMAL

# For fullscreen mode
WINDOW_MODE = WindowConfig.FULLSCREEN
```

See [Borderless Window Guide](docs/borderless_window_guide.md) for detailed customization options.

## 🔧 Technical Details
- **Framework**: Kivy 2.3.0+ with KivyMD
- **Pattern**: Dependency Injection with dependency-injector
- **UI**: Hardware-accelerated OpenGL rendering
- **Layout**: Responsive BoxLayout system

### Key Components
1. **MentorIAApp**: Main application class
2. **InitialScreen**: Welcome screen with path creation
3. **AboutDialog**: Modal popup with app info
4. **CreatePathDialog**: Path creation form

## 🆚 Why Kivy Over Flet?

| Aspect | Flet | Kivy |
|--------|------|------|
| **Stability** | ❌ Crashes on menu clicks | ✅ Rock solid |
| **Performance** | ⚠️ Web-based rendering | ✅ Hardware accelerated |
| **Mobile Support** | ❌ None | ✅ Android/iOS |
| **Customization** | ⚠️ Limited | ✅ Extensive |
| **Community** | 🆕 New | 👥 Large & mature |

## 🐛 Known Issues

### System Warnings (Non-critical)
- Clipboard provider warnings on some Linux systems
- Input device permission warnings (doesn't affect functionality)
- Xwayland warnings (normal for Wayland systems)

These warnings don't affect application functionality and are normal for Kivy applications.

## 🔮 Future Roadmap

### Phase 1: Core Features
- [ ] Path management (CRUD operations)
- [ ] LLM provider configuration
- [ ] Settings screen
- [ ] Data persistence

### Phase 2: Enhanced UI
- [ ] Material Design with KivyMD
- [ ] Dark/light theme support
- [ ] Animations and transitions
- [ ] Icons and improved styling

### Phase 3: Advanced Features
- [ ] Study session management
- [ ] Progress tracking
- [ ] Content scraping integration
- [ ] Mobile app deployment

## 📚 Documentation

- [Detailed Refactor Documentation](docs/kivy_refactor.md)
- [Framework Comparison](docs/framework_comparison.md)
- [Borderless Window Guide](docs/borderless_window_guide.md)
- [Original README](README.md)

## 🤝 Contributing

The Kivy version provides a stable foundation for development. Key areas for contribution:

1. **UI/UX Improvements**: Better styling and user experience
2. **Feature Implementation**: Core mentorIA functionality
3. **Testing**: Unit tests and integration tests
4. **Documentation**: User guides and API documentation

## 📄 License

Same as the original project - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- **Kivy Team**: For the excellent cross-platform framework
- **Original mentorIA**: For the concept and initial implementation
- **Community**: For feedback and testing

---

**Note**: This Kivy version is the recommended implementation for production use due to its stability and cross-platform capabilities. The original Flet version remains in the `src/` directory for reference.