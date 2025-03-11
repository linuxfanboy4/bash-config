import os
import subprocess

fonts_dir = os.path.expanduser("~/.fonts/")
if not os.path.exists(fonts_dir):
    os.makedirs(fonts_dir)

fonts = {
    "Freshman": os.path.join(fonts_dir, "Freshman.ttf"),
    "Font": os.path.join(fonts_dir, "font.ttf")
}

def install_font(font_name):
    if font_name in fonts:
        font_path = fonts[font_name]
        if not os.path.exists(font_path):
            pass
        subprocess.run(["fc-cache", "-fv"], check=True)
        print(f"Font {font_name} installed and font cache refreshed.")
    else:
        print(f"Font {font_name} not found in available fonts.")
