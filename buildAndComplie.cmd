@echo off
pip install -r requirements.txt
pyinstaller src/main.py --hidden-import pkg_resources --hidden-import infi.systray --add-data="temp.ico;." --noconsole --onefile
