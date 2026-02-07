@echo off
echo ========================================
echo Test de detection de Node.js par yt-dlp
echo ========================================
echo.

echo [1] Verification de Node.js dans le PATH...
where node >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Node.js trouve dans le PATH
    node --version
) else (
    echo [ERREUR] Node.js n'est pas trouve dans le PATH
    echo.
    echo Solutions :
    echo 1. Redemarrez votre ordinateur apres l'installation de Node.js
    echo 2. Ajoutez Node.js au PATH manuellement
    echo 3. Reinstallez Node.js avec l'option "Add to PATH"
    pause
    exit /b 1
)
echo.

echo [2] Verification du chemin complet de node.exe...
where node
echo.

echo [3] Test de yt-dlp avec runtime JavaScript explicite...
echo.
yt-dlp --print title --extractor-args "youtube:player_client=ios" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
echo.

if %errorlevel% equ 0 (
    echo ========================================
    echo [SUCCESS] yt-dlp fonctionne correctement!
    echo ========================================
) else (
    echo ========================================
    echo [ERREUR] yt-dlp a rencontre un probleme
    echo ========================================
    echo.
    echo Essayez cette commande alternative :
    echo yt-dlp --cookies-from-browser chrome "URL_YOUTUBE"
)

echo.
echo Appuyez sur une touche pour fermer...
pause > nul
