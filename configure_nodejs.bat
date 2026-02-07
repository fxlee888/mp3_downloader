@echo off
echo ========================================
echo Configuration de Node.js pour yt-dlp
echo ========================================
echo.

echo [1] Verification de Node.js...
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Node.js n'est pas trouve dans le PATH
    echo.
    echo Solutions :
    echo 1. Installez Node.js depuis https://nodejs.org/
    echo 2. Redemarrez votre ordinateur
    echo 3. Verifiez que Node.js est dans le PATH
    echo.
    pause
    exit /b 1
)

echo [OK] Node.js trouve
node --version
echo.

echo [2] Chemin de node.exe...
for /f "delims=" %%i in ('where node') do set NODE_PATH=%%i
echo %NODE_PATH%
echo.

echo [3] Configuration de yt-dlp pour utiliser Node.js...
echo.

REM Creer le fichier de configuration yt-dlp
set CONFIG_DIR=%APPDATA%\yt-dlp
set CONFIG_FILE=%CONFIG_DIR%\config

if not exist "%CONFIG_DIR%" mkdir "%CONFIG_DIR%"

echo # Configuration yt-dlp > "%CONFIG_FILE%"
echo --extractor-args youtube:player_client=ios >> "%CONFIG_FILE%"
echo --no-check-certificates >> "%CONFIG_FILE%"

echo [OK] Fichier de configuration cree : %CONFIG_FILE%
echo.

echo [4] Test de yt-dlp avec Node.js...
echo.

REM Test avec une video simple
yt-dlp --print title "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo [SUCCESS] Configuration reussie !
    echo ========================================
    echo.
    echo Node.js est maintenant configure avec yt-dlp.
    echo Vous pouvez maintenant utiliser l'application.
) else (
    echo.
    echo ========================================
    echo [ATTENTION] Le test a echoue
    echo ========================================
    echo.
    echo Solutions alternatives :
    echo 1. Utilisez la version avec fichier cookies
    echo 2. Exportez vos cookies YouTube
    echo 3. Consultez EXPORT_COOKIES_GUIDE.md
)

echo.
echo Appuyez sur une touche pour fermer...
pause > nul
