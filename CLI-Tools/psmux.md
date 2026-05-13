# psmux - Terminal Multiplexer for Windows

**psmux** is a native Windows terminal multiplexer built from the ground up in Rust. It's the real tmux for Windows - not a port, not a wrapper, not a workaround. It uses Windows ConPTY directly, speaks the tmux command language, reads your `.tmux.conf`, and supports tmux themes.

## Project Information

- **Version**: 0.2.2
- **Language**: Rust (opt-level 3, full LTO, single codegen unit for maximum performance)
- **License**: MIT
- **Repository**: https://github.com/marlocarlo/psmux
- **Aliases**: psmux ships with `tmux` and `pmux` aliases - use any command you prefer!

## Key Features

- 🦠 **Made in Rust**: Maximum performance with sub-100ms session creation
- 🖱️ **Full mouse support**: Click panes, drag-resize borders, scroll, click tabs, select text
- 🎨 **tmux theme support**: 16 named colors + 256 indexed + 24-bit true color
- 📋 **Reads your `.tmux.conf`**: Drop-in config compatibility, zero learning curve
- ⚡ **83 tmux-compatible commands**: Full scripting and automation support
- 🪟 **Windows-native**: ConPTY, Win32 API, works with PowerShell, cmd, bash, WSL, nushell
- 📦 **Single binary, no dependencies**: Easy installation and setup
- 🤖 **Claude Code agent teams**: First-class support for teammate pane spawning
- 🌐 **CJK/IME input**: Full support for Chinese, Japanese, and Korean input methods

## Requirements

- Windows 10 or Windows 11
- **PowerShell 7+** (recommended) or cmd.exe
  - Install via: `winget install --id Microsoft.PowerShell`
  - Or visit: https://aka.ms/powershell

## Installation

### Using WinGet (Recommended)
```powershell
winget install psmux
```

### Using Cargo
```powershell
cargo install psmux
```
This installs `psmux`, `pmux`, and `tmux` binaries to your Cargo bin directory.

### Using Scoop
```powershell
scoop bucket add psmux https://github.com/psmux/scoop-psmux
scoop install psmux
```

### Using Chocolatey
```powershell
choco install psmux
```

### From GitHub Releases
Download the latest `.zip` from [GitHub Releases](https://github.com/psmux/psmux/releases) and add to your PATH.

### From Source
```powershell
git clone https://github.com/psmux/psmux.git
cd psmux
cargo build --release
```
Built binaries:
```
target\release\psmux.exe
target\release\pmux.exe
target\release\tmux.exe
```

## Updating

### Using WinGet
```powershell
winget upgrade psmux
```

### Using Cargo
```powershell
cargo install psmux --force
```

### Using Scoop
```powershell
scoop update psmux
```

### Using Chocolatey
```powershell
choco upgrade psmux
```

## Basic Usage

Use `psmux`, `pmux`, or `tmux` — they're identical:

```powershell
psmux                          # Start a new session or attach to existing one
psmux new-session -s work      # Create a new session named "work"
psmux ls                       # List all sessions
psmux attach -t work           # Attach to session "work"
psmux --help                   # Show help message
psmux --version                # Show version information
```

## Commands

### Session Management
- `psmux` (no command) - Start a new session or attach to existing one
- `new-session` - Create a new session
  - `-s <name>` - Session name (default: "default")
  - `-d` - Start detached (in background)
- `attach, attach-session` - Attach to an existing session
  - `-t <name>` - Target session name
- `ls, list-sessions` - List all active sessions

### Window and Pane Management
- `new-window` - Create a new window in current session
- `split-window` - Split current pane
  - `-h` - Split horizontally (side by side)
  - `-v` - Split vertically (top/bottom, default)
- `kill-pane` - Close the current pane
- `capture-pane` - Capture the content of current pane

### Other Commands
- `server` - Run as a server (internal use)
- `help` - Show help message
- `version` - Show version information

## Keyboard Shortcuts

**Default prefix**: `Ctrl+B` (same as tmux)

### Window Management
| Key | Action |
|-----|--------|
| `Prefix + c` | Create new window |
| `Prefix + n` | Next window |
| `Prefix + p` | Previous window |
| `Prefix + l` | Last (previously active) window |
| `Prefix + w` | Interactive session/window/pane chooser |
| `Prefix + &` | Kill current window (with confirmation) |
| `Prefix + ,` | Rename current window |
| `Prefix + '` | Prompt for window index (jump to any window) |
| `Prefix + 0-9` | Select window by number |

### Pane Splitting
| Key | Action |
|-----|--------|
| `Prefix + %` | Split pane left/right (horizontal) |
| `Prefix + "` | Split pane top/bottom (vertical) |

### Pane Navigation
| Key | Action |
|-----|--------|
| `Prefix + Arrow` | Navigate between panes (Up/Down/Left/Right), wraps at edges |
| `Prefix + o` | Select next pane (rotate) |
| `Prefix + ;` | Last (previously active) pane |
| `Prefix + q` | Display pane numbers (type number to switch, auto-dismisses) |

### Pane Management
| Key | Action |
|-----|--------|
| `Prefix + x` | Kill current pane (with confirmation) |
| `Prefix + z` | Toggle pane zoom (fullscreen) |
| `Prefix + {` | Swap pane up |
| `Prefix + }` | Swap pane down |
| `Prefix + !` | Break pane out to new window |

### Pane Resize
| Key | Action |
|-----|--------|
| `Prefix + Ctrl+Arrow` | Resize pane by 1 cell |
| `Prefix + Alt+Arrow` | Resize pane by 5 cells |

### Layout
| Key | Action |
|-----|--------|
| `Prefix + Space` | Cycle to next layout |
| `Prefix + Alt+1` | Even-horizontal layout |
| `Prefix + Alt+2` | Even-vertical layout |
| `Prefix + Alt+3` | Main-horizontal layout |
| `Prefix + Alt+4` | Main-vertical layout |
| `Prefix + Alt+5` | Tiled layout |

### Session
| Key | Action |
|-----|--------|
| `Prefix + d` | Detach from session |
| `Prefix + $` | Rename session |
| `Prefix + s` | Session chooser/switcher |
| `Prefix + (` | Switch to previous session |
| `Prefix + )` | Switch to next session |

### Copy / Paste
| Key | Action |
|-----|--------|
| `Prefix + [` | Enter copy/scroll mode |
| `Prefix + ]` | Paste from buffer |
| `Prefix + =` | Interactive buffer chooser |

### Miscellaneous
| Key | Action |
|-----|--------|
| `Prefix + :` | Enter command mode |
| `Prefix + ?` | List keybindings (help overlay) |
| `Prefix + i` | Display window/pane info |
| `Prefix + t` | Clock mode |

## Copy Mode (Vim Keybindings)

Enter copy mode with `Prefix + [` to scroll through terminal history with vim-style keybindings.

### Cursor Movement
| Key | Action |
|-----|--------|
| `h` / `Left` | Move cursor left |
| `j` / `Down` | Move cursor down |
| `k` / `Up` | Move cursor up |
| `l` / `Right` | Move cursor right |

### Word Motions
| Key | Action |
|-----|--------|
| `w` / `b` / `e` | Next word / prev word / end of word |
| `W` / `B` / `E` | WORD variants (whitespace-delimited) |

### Line Motions
| Key | Action |
|-----|--------|
| `0` / `Home` | Start of line |
| `$` / `End` | End of line |
| `^` | First non-blank character |

### Scrolling
| Key | Action |
|-----|--------|
| `Ctrl+u` / `Ctrl+d` | Half page up / down |
| `Ctrl+b` / `PageUp` | Full page up |
| `Ctrl+f` / `PageDown` | Full page down |
| `g` | Top of scrollback |
| `G` | Bottom (live output) |

### Screen Position
| Key | Action |
|-----|--------|
| `H` | Jump to top of visible area |
| `M` | Jump to middle of visible area |
| `L` | Jump to bottom of visible area |

### Character Find
| Key | Action |
|-----|--------|
| `f{char}` / `F{char}` | Find char forward / backward |
| `t{char}` / `T{char}` | Till char forward / backward |

### Bracket / Paragraph
| Key | Action |
|-----|--------|
| `%` | Jump to matching bracket (`()`, `[]`, `{}`, `<>`) |
| `{` | Jump to previous paragraph (blank line) |
| `}` | Jump to next paragraph (blank line) |

### Selection
| Key | Action |
|-----|--------|
| `Space` | Begin character selection |
| `v` | Toggle rectangle selection |
| `V` | Line selection |
| `Ctrl+v` | Toggle rectangle selection |
| `o` | Swap cursor/anchor ends |

### Yank (Copy)
| Key | Action |
|-----|--------|
| `y` / `Enter` | Copy selection and exit |
| `D` | Copy to end of line and exit |
| `A` | Append selection to buffer |

### Search
| Key | Action |
|-----|--------|
| `/` | Search forward |
| `?` | Search backward |
| `n` / `N` | Next / previous match |

### Exit
| Key | Action |
|-----|--------|
| `Esc` / `q` | Exit copy mode |
| `Ctrl+C` / `Ctrl+G` | Exit copy mode |

## Mouse Bindings

When `mouse on` (default):

| Action | Behavior |
|--------|----------|
| Left-click status tab | Switch to clicked window |
| Left-click pane | Focus that pane |
| Left-click/drag border | Resize split interactively |
| Scroll up/down | Scroll pane (or enter copy mode at prompt) |
| Mouse drag in copy mode | Select text → auto-copy on release |
| Right-click | Paste clipboard |

## Command Prompt

Press `Prefix + :` to open the command prompt at the bottom of the screen.

### Command Prompt Editing Keys
| Key | Action |
|-----|--------|
| `Left` / `Right` | Move cursor within the command |
| `Home` / `Ctrl+A` | Jump to start of line |
| `End` / `Ctrl+E` | Jump to end of line |
| `Backspace` | Delete character before cursor |
| `Delete` | Delete character at cursor |
| `Up` / `Down` | Browse command history (previous/next) |
| `Tab` | Command name completion |
| `Enter` | Execute the command |
| `Escape` | Cancel and close the prompt |

### Example Commands
- `:split-window -h` - Split horizontally
- `:new-window -n logs` - Create a named window
- `:source-file ~/.psmux.conf` - Reload your config
- `:set -g status-style "bg=blue"` - Change a setting live
- `:list-keys` - See all current key bindings

## Configuration Files

### Config File Locations
- `%USERPROFILE%\.psmux.conf` - Main configuration file
- `%USERPROFILE%\.psmuxrc` - Alternative configuration file
- `%USERPROFILE%\.tmux.conf` - Also supported for tmux compatibility

### Environment Variables
- `PSMUX_SESSION_NAME` - Default session name
- `PSMUX_DEFAULT_SESSION` - Fallback default session name
- `PSMUX_CURSOR_STYLE` - Cursor style (block, underline, bar)
- `PSMUX_CURSOR_BLINK` - Cursor blinking (true/false)

### Changing Prefix Key
```bash
# In your .psmux.conf
set -g prefix C-a
unbind C-b
bind C-a send-prefix
```

## Developer Workflow in Windows Terminal

### Starting a Development Session
```powershell
# Create a named session for your project
psmux new-session -s myproject

# Or start detached and work in multiple terminals
psmux new-session -s myproject -d
```

### Typical Development Layout
1. **Main editor pane** - Left side, largest
2. **Terminal/commands** - Right side, split vertically
3. **Logs/output** - Bottom right
4. **Git status** - Top right

### Session Management for Development
```powershell
# List all sessions
psmux ls

# Attach to your project session
psmux attach -t myproject

# Detach and leave running
# Press: Prefix + d

# Kill a session when done
psmux kill-session -t myproject
```

### Integration with Claude Code
psmux has first-class support for Claude Code agent teams. When Claude Code runs inside a psmux session, teammate agents automatically spawn in separate tmux panes instead of running in-process.

```powershell
psmux new-session -s work    # Start a psmux session
claude                        # Run Claude Code — agent teams just work
```

## Advanced Features

### Session Persistence
- Sessions survive SSH disconnects and terminal crashes
- Detach with `Prefix + d`, reconnect with `psmux attach` from any terminal
- Warm sessions (`set -g warm on`, default) pre-spawn background servers for instant session creation

### Layouts
- 5 built-in layouts: even-horizontal, even-vertical, main-horizontal, main-vertical, tiled
- Cycle through layouts with `Prefix + Space`
- Direct layout access with `Prefix + Alt+1-5`

### Interactive Choosers
- `Prefix + w` - Browse and select sessions, windows, and panes
- `Prefix + s` - Session chooser/switcher
- `Prefix + =` - Pick from paste buffers
- `Prefix + ?` - List keybindings
- All choosers support digit-jump (type number + Enter to jump)

### Repeat Mode
Navigation and resize bindings support repeat mode: after pressing the prefix key once, successive keypresses within the `repeat-time` window (default 500ms) trigger the action without needing to re-enter the prefix.

## Performance

- **Sub-100ms session creation**
- **Near-zero overhead** over shell startup
- **Optimized Rust implementation** with opt-level 3, full LTO
- **Single binary** with no external dependencies

## Related Projects

- **pstop** - htop for Windows with real-time system monitoring
- **psnet** - Real-time TUI network monitor with live speed graphs
- **Tmux Plugin Panel** - TUI plugin & theme manager for tmux and psmux
- **OMP Manager** - Oh My Posh setup wizard for browsing 100+ themes

## Documentation

For more detailed information, see:
- [Features](https://github.com/marlocarlo/psmux/blob/master/docs/features.md)
- [Key Bindings](https://github.com/marlocarlo/psmux/blob/master/docs/keybindings.md)
- [Configuration](https://github.com/marlocarlo/psmux/blob/master/docs/configuration.md)
- [Scripting](https://github.com/marlocarlo/psmux/blob/master/docs/scripting.md)
- [Plugins & Themes](https://github.com/marlocarlo/psmux/blob/master/docs/plugins.md)
- [Claude Code Integration](https://github.com/marlocarlo/psmux/blob/master/docs/claude-code.md)
- [FAQ](https://github.com/marlocarlo/psmux/blob/master/docs/faq.md)

## Contributing

Contributions welcome — bug reports, PRs, docs, and test scripts via [GitHub Issues](https://github.com/psmux/psmux/issues).

If psmux helps your Windows workflow, consider giving it a ⭐ on GitHub!
