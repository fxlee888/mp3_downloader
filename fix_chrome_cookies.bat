@echo off
echo ========================================
echo Fix pour les cookies Chrome (DPAPI)
echo ========================================
echo.

echo Installation de pycryptodomex...
pip install pycryptodomex
echo.

echo Installation de pycryptodome...
pip install pycryptodome
echo.

echo Mise a jour de yt-dlp...
pip install --upgrade yt-dlp
echo.

echo ========================================
echo Installation terminee!
echo ========================================
echo.
echo Relancez l'application et reessayez.
echo.
echo Si ca ne fonctionne toujours pas :
echo 1. Utilisez Firefox a la place de Chrome
echo 2. Ou utilisez la version sans cookies
echo.
echo Appuyez sur une touche pour fermer...
pause > nul
