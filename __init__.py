from flask import Flask
from app import oefen
# import subprocess
import os
# import psutil


# def is_sass_running():
#     """Check of er al een sass --watch proces draait."""
#     for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
#         try:
#             if proc.info['cmdline'] and "sass" in proc.info['cmdline'][0]:
#                 if "--watch" in proc.info['cmdline']:
#                     return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue
#     return False


# def compile_scss_watch():
#     """Start SCSS watcher in achtergrond als hij nog niet draait."""
#     input_scss = os.path.join("assets", "scss", "style.scss")
#     output_css = os.path.join("static", "css", "style.css")

#     # Zorg dat map bestaat
#     os.makedirs(os.path.dirname(output_css), exist_ok=True)

#     sass_cmd = r"C:\Users\abdiw\AppData\Roaming\npm\sass.cmd"

#     # Start dit is_sass_running fucnctie alleen als er nog geen watcher actief is
#     if not is_sass_running():
#         subprocess.Popen(
#             [sass_cmd, input_scss, output_css, "--watch"]
#         )

#     else:
#         print("⚡ Sass watcher draait al, niet opnieuw gestart.")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(oefen)

    # Start watcher op achtergrond
    # compile_scss_watch()

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
