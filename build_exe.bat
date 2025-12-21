@echo off
echo ========================================
echo Creation de l'executable YouTube Downloader
echo ========================================
echo.

REM Installation de PyInstaller si necessaire
echo Installation de PyInstaller...
pip install pyinstaller
echo.

REM Creation de l'executable
echo Creation de l'executable...
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" --icon=app_icon.ico youtube_downloader.py

echo.
echo ========================================
echo Termine !
echo ========================================
echo.
echo L'executable se trouve dans le dossier : dist\YouTube_MP3_Downloader.exe
echo.
pause
