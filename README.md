# Bash Configuration Manager

A robust and extensible tool designed to streamline the customization of your Bash environment. Manage themes, plugins, and fonts through an intuitive terminal interface, enhancing productivity and aesthetic appeal.

## Features

- **Themes**: Apply pre-configured terminal color schemes for distinct visual styles.  
  Example Themes: `Cyber Red`, `Neo Tokyo`, `Stealth Black`, `Midnight Blue`, `Glitch Purple`.  
- **Plugins**: Extend functionality with aliases, shortcuts, and system tools.  
  Example Plugins: `fast_aliases`, `power_prompt`, `sys_monitor`, `docker_helper`, `git_boost`.  
- **Fonts**: Install and activate custom fonts to personalize terminal text rendering.  
  Supported Fonts: `Freshman` from DaFont created by William Boyd, `Font` from NerdFonts
- **Configuration Management**: Persistently track applied themes and installed plugins via JSON configuration.  

## Installation

### Prerequisites
- Python 3.6 or later  
- `pip` for Python package management  
- Dependencies:  
  ```bash
  pip install rich lolcat figlet
  ```
- Optional Tools (required for specific plugins):  
  `bat`, `docker`, `xclip`, `scrot`, `speedtest-cli`, `tldr`.

### Quick Installation
Execute the following command to install the Bash Configuration Manager:  
```bash
wget https://raw.githubusercontent.com/linuxfanboy4/bash-config/refs/heads/main/install.sh && bash install.sh
```

This script clones the repository, verifies Bash availability, and configures the environment. After installation, navigate to the `src` directory and run:  
```bash
python3 main.py
```

## Usage

Launch the manager with `python3 main.py` to access the interactive menu:  

1. **Apply Theme**: Select from a curated list of terminal themes.  
2. **Install Plugin**: Enhance Bash with productivity-focused aliases and tools.  
3. **View Installed Plugins**: Review currently active plugins.  
4. **Install Font**: Integrate custom fonts into your terminal environment.  
5. **Exit**: Close the application.  

## Configuration

- **Persistent Settings**: Applied themes and plugins are stored in `~/.bash_manager_config.json`.  
- **Manual Overrides**: Edit `.bashrc` directly to modify aliases or adjust theme commands.  

## Dependencies

- **Core**: Python 3, `rich`, `lolcat`, `figlet`.  
- **Plugin-Specific**:  
  - `bat`: Required for `colorizer` plugin.  
  - `docker`: Required for `docker_helper` and `docker_compose`.  
  - `xclip`: Required for `clipboard` functionality.  

## License

Distributed under the MIT License. See `LICENSE` for details.

## Contributions

Contributions are welcomed. Submit issues for bug reports or feature requests. Fork the repository and create pull requests for enhancements.
