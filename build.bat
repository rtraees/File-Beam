
@echo off
echo Installing requirements...
pip install -r requirements.txt

echo Building Executable...
pyinstaller --noconfirm --onefile --windowed --name "File Beam" --add-data "templates;templates" --icon=NONE file_beam.py

echo Build Complete!
echo You can find the executable in the 'dist' folder.
pause
