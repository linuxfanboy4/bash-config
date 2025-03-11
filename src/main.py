import os
import subprocess
import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from fonts import install_font
from themes import themes
from plugins import plugins

console = Console()
CONFIG_FILE = os.path.expanduser("~/.bash_manager_config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"theme": None, "plugins": []}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def apply_theme(theme_name):
    if theme_name in themes:
        subprocess.Popen(["bash", "-c", themes[theme_name]], shell=False)
        config = load_config()
        config["theme"] = theme_name
        save_config(config)

def install_plugin(plugin_name):
    if plugin_name in plugins:
        subprocess.run(["bash", "-c", plugins[plugin_name]], shell=False)
        config = load_config()
        if plugin_name not in config["plugins"]:
            config["plugins"].append(plugin_name)
        save_config(config)

def show_menu():
    subprocess.run("figlet 'Bash' | lolcat", shell=True)

    while True:
        console.print("\n[bold cyan]Bash Configuration Manager[/bold cyan]")
        console.print("[1] Apply Theme")
        console.print("[2] Install Plugin")
        console.print("[3] View Installed Plugins")
        console.print("[4] Install Font")
        console.print("[5] Exit")

        choice = Prompt.ask("\n[bold yellow]Choose an option[/bold yellow]", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            theme_table = Table(title="Available Themes", show_lines=True)
            theme_table.add_column("Theme", style="magenta")
            for theme in themes.keys():
                theme_table.add_row(theme)
            console.print(theme_table)
            theme_choice = Prompt.ask("\n[bold green]Enter theme name[/bold green]", choices=list(themes.keys()))
            apply_theme(theme_choice)
            console.print(f"[bold green]Applied theme:[/bold green] {theme_choice}")

        elif choice == "2":
            plugin_table = Table(title="Available Plugins", show_lines=True)
            plugin_table.add_column("Plugin", style="blue")
            for plugin in plugins.keys():
                plugin_table.add_row(plugin)
            console.print(plugin_table)
            plugin_choice = Prompt.ask("\n[bold green]Enter plugin name[/bold green]", choices=list(plugins.keys()))
            install_plugin(plugin_choice)
            console.print(f"[bold green]Installed plugin:[/bold green] {plugin_choice}")

        elif choice == "3":
            config = load_config()
            console.print(f"[bold yellow]Installed Plugins:[/bold yellow] {', '.join(config['plugins']) if config['plugins'] else 'None'}")

        elif choice == "4":
            font_table = Table(title="Available Fonts", show_lines=True)
            font_table.add_column("Font", style="yellow")
            for font in ["Freshman", "Font"]:
                font_table.add_row(font)
            console.print(font_table)
            font_choice = Prompt.ask("\n[bold green]Enter font name[/bold green]", choices=["Freshman", "Font"])
            install_font(font_choice)
            console.print(f"[bold green]Installed font:[/bold green] {font_choice}")

        elif choice == "5":
            console.print("[bold red]Exiting...[/bold red]")
            break

if __name__ == "__main__":
    show_menu()
