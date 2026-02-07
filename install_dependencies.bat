@echo off
echo ========================================
echo Installation des dependances
echo YouTube MP3 Downloader
echo ========================================
echo.

echo [1/4] Mise a jour de pip...
python -m pip install --upgrade pip
echo.

echo [2/4] Installation/Mise a jour de yt-dlp...
pip install --upgrade yt-dlp
echo.

echo [3/4] Verification de ffmpeg...
where ffmpeg >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] ffmpeg est installe
    ffmpeg -version | findstr "ffmpeg version"
) else (
    echo [ATTENTION] ffmpeg n'est pas trouve dans le PATH
    echo.
    echo Veuillez installer ffmpeg :
    echo 1. Telecharger depuis : https://ffmpeg.org/download.html
    echo 2. Ou utiliser Chocolatey : choco install ffmpeg
    echo 3. Ajouter au PATH systeme
)
echo.

echo [4/4] Verification de Node.js (runtime JavaScript)...
where node >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Node.js est installe
    node --version
) else (
    echo [RECOMMANDE] Node.js n'est pas installe
    echo.
    echo yt-dlp necessite un runtime JavaScript pour certaines videos YouTube.
    echo.
    echo Veuillez installer Node.js :
    echo 1. Telecharger depuis : https://nodejs.org/
    echo 2. Choisir la version LTS ^(Long Term Support^)
    echo 3. Installer avec les options par defaut
    echo 4. Redemarrer votre ordinateur
)
echo.

echo ========================================
echo Verification de yt-dlp...
echo ========================================
yt-dlp --version
echo.

echo ========================================
echo Installation terminee!
echo ========================================
echo.
echo Prochaines etapes :
echo 1. Si ffmpeg n'est pas installe, installez-le
echo 2. Si Node.js n'est pas installe, installez-le (recommande)
echo 3. Redemarrez votre ordinateur si vous avez installe de nouveaux logiciels
echo 4. Lancez l'application YouTube MP3 Downloader
echo.
echo Appuyez sur une touche pour fermer...
pause > nul
