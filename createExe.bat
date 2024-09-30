@echo off
cd C:\Users\burne\PycharmProjects\Zidian
call venv\Scripts\activate
pyinstaller --onefile zidian.py
echo .exe file created!
pause
