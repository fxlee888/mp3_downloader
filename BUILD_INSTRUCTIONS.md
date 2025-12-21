# Instructions pour créer un fichier .exe

## Méthode 1 : Automatique (Recommandée)

Double-cliquez simplement sur le fichier :
```
build_exe.bat
```

L'executable sera créé automatiquement dans le dossier `dist\YouTube_MP3_Downloader.exe`

## Méthode 2 : Manuelle

### 1. Installer PyInstaller

```bash
pip install pyinstaller
```

### 2. Créer l'executable

```bash
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" youtube_downloader.py
```

### Options expliquées :

- `--onefile` : Crée un seul fichier .exe (tout est inclus)
- `--windowed` : Pas de console en arrière-plan (mode GUI uniquement)
- `--name "YouTube_MP3_Downloader"` : Nom de l'executable

### 3. Récupérer l'executable

L'executable se trouvera dans :
```
dist\YouTube_MP3_Downloader.exe
```

## Avec un icône personnalisé (optionnel)

Si vous avez un fichier .ico :

```bash
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" --icon=votre_icone.ico youtube_downloader.py
```

## Distribution

Une fois l'executable créé, vous pouvez :

1. Copier `YouTube_MP3_Downloader.exe` n'importe où
2. Le partager avec d'autres utilisateurs
3. Créer un raccourci sur le bureau

**IMPORTANT** :
- yt-dlp et ffmpeg doivent TOUJOURS être installés sur le système où l'exe est exécuté
- L'exe ne contient que l'application Python, pas yt-dlp ni ffmpeg

## Taille approximative

- Avec `--onefile` : ~15-20 MB
- Temps de création : 30-60 secondes

## Dépannage

### Erreur "PyInstaller not found"
```bash
pip install --upgrade pyinstaller
```

### L'exe ne se lance pas
- Vérifiez que Python est bien installé lors de la création
- Essayez sans `--windowed` pour voir les erreurs

### Console qui apparaît
- Assurez-vous d'utiliser l'option `--windowed`

## Nettoyage

Après la création, vous pouvez supprimer :
- Le dossier `build/` (fichiers temporaires)
- Le fichier `YouTube_MP3_Downloader.spec`

Gardez uniquement `dist\YouTube_MP3_Downloader.exe`
