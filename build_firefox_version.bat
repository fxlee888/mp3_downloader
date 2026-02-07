@echo off
echo ========================================
echo Build YouTube MP3 Downloader (Firefox)
echo ========================================
echo.

echo [1/4] Verification de PyInstaller...
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller n'est pas installe. Installation en cours...
    pip install pyinstaller
    echo.
)

echo [2/4] Nettoyage des anciens builds...
if exist "dist\YouTube_MP3_Downloader.exe" del "dist\YouTube_MP3_Downloader.exe"
if exist "build" rmdir /s /q "build"
echo.

echo [3/4] Creation de l'executable...
echo Cela peut prendre 1-2 minutes...
echo.

REM Build avec PyInstaller
pyinstaller --onefile --windowed ^
    --name "YouTube_MP3_Downloader" ^
    --icon "app_icon.ico" ^
    --add-data "app_icon.ico;." ^
    youtube_downloader_cookies.py

if %errorlevel% neq 0 (
    echo.
    echo [ERREUR] La compilation a echoue!
    pause
    exit /b 1
)

echo.
echo [4/4] Verification de l'executable...
if exist "dist\YouTube_MP3_Downloader.exe" (
    echo.
    echo ========================================
    echo [SUCCESS] Build reussi!
    echo ========================================
    echo.
    echo Executable cree : dist\YouTube_MP3_Downloader.exe
    echo.
    echo Vous pouvez maintenant :
    echo 1. Tester l'executable : dist\YouTube_MP3_Downloader.exe
    echo 2. Mettre a jour votre raccourci de startup avec ce nouveau fichier
    echo.
    echo L'application utilisera automatiquement :
    echo - Firefox avec cookies automatiques
    echo - Node.js pour les challenges YouTube
    echo - Configuration yt-dlp dans %%APPDATA%%\yt-dlp\config
    echo.
) else (
    echo [ERREUR] L'executable n'a pas ete cree!
)

echo Appuyez sur une touche pour fermer...
pause > nul
