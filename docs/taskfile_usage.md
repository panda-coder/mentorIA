# Taskfile Usage Guide

This document explains how to use the `Taskfile.yml` to manage common development tasks for the mentorIA project.

## Prerequisites

Install [Task](https://taskfile.dev/) on your system:

```bash
# macOS
brew install go-task/tap/go-task

# Linux (snap)
sudo snap install task --classic

# Windows (chocolatey)
choco install go-task

# Or download from https://github.com/go-task/task/releases
```

## Available Tasks

### Application Execution

| Task | Description | Usage |
|------|-------------|-------|
| `run` | Run the application in default mode (borderless) | `task run` |
| `run-normal` | Run with standard window and title bar | `task run-normal` |
| `run-borderless` | Run with borderless window (custom title bar) | `task run-borderless` |
| `run-fullscreen` | Run in fullscreen mode | `task run-fullscreen` |

### Development Tasks

| Task | Description | Usage |
|------|-------------|-------|
| `install` | Install project dependencies using uv | `task install` |
| `dev` | Run in development mode | `task dev` |
| `setup` | Complete project setup (install + run) | `task setup` |
| `clean` | Clean up cache files and temporary files | `task clean` |

### Configuration Management

| Task | Description | Usage |
|------|-------------|-------|
| `config-show` | Display current window configuration | `task config-show` |
| `config-reset` | Reset configuration to defaults (borderless) | `task config-reset` |

### Information Tasks

| Task | Description | Usage |
|------|-------------|-------|
| `info` | Show project information and structure | `task info` |
| `default` | Show all available tasks | `task` or `task --list` |

## Window Mode Management

The taskfile automatically manages window modes by modifying the `WINDOW_MODE` setting in `src/core/config.py`:

- **Normal Mode**: Temporarily switches to `NORMAL` mode, runs the app, then restores `BORDERLESS`
- **Borderless Mode**: Sets to `BORDERLESS` mode (default)
- **Fullscreen Mode**: Temporarily switches to `FULLSCREEN`, runs the app, then restores `BORDERLESS`

This ensures that the default borderless mode is preserved while allowing easy testing of different window modes.

## Examples

### Quick Start
```bash
# First time setup
task setup

# Regular development
task run

# Test different window modes
task run-normal
task run-fullscreen
```

### Development Workflow
```bash
# Check current configuration
task config-show

# Clean up before testing
task clean

# Run in development mode
task dev

# Show project information
task info
```

### Configuration Management
```bash
# Show current window mode
task config-show

# Reset to defaults if needed
task config-reset
```

## Customization

You can modify the `Taskfile.yml` to add your own tasks or customize existing ones. The file uses Go template syntax with variables defined in the `vars` section:

- `{{.APP_NAME}}`: mentorIA
- `{{.SRC_DIR}}`: src
- `{{.MAIN_FILE}}`: src/main.py

## Troubleshooting

### Task not found
```bash
# Make sure Task is installed
task --version

# Check if Taskfile.yml exists in project root
ls -la Taskfile.yml
```

### Configuration issues
```bash
# Reset configuration to defaults
task config-reset

# Check current configuration
task config-show
```

### Dependencies issues
```bash
# Reinstall dependencies
task install

# Clean and reinstall
task clean
task install
```