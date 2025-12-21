# YouTube MP3 Downloader

Application Python avec interface graphique pour télécharger des musiques depuis YouTube au format MP3.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-Personal-green)

## Description

Cette application permet de télécharger facilement des vidéos YouTube et de les convertir en fichiers MP3 avec la qualité audio de votre choix. Interface graphique simple et intuitive.

## Fonctionnalités

- Interface graphique tkinter (aucune dépendance externe)
- Téléchargement YouTube avec yt-dlp
- Conversion automatique en MP3
- Qualité audio personnalisable (0 = meilleure, 9 = plus faible)
- Sélection du dossier de destination
- Logs en temps réel
- Génération d'executable Windows (.exe)
- Icône personnalisée

## Prérequis

- Python 3.x
- yt-dlp
- ffmpeg

## Installation

```bash
# Installer yt-dlp
pip install yt-dlp

# Installer ffmpeg
# Windows: https://ffmpeg.org/download.html
# Ou avec chocolatey: choco install ffmpeg
```

## Utilisation

### Option 1 : Lancer avec Python

```bash
python youtube_downloader.py
```

### Option 2 : Créer un executable .exe

**Méthode automatique** :
```bash
# Double-cliquez sur build_exe.bat
```

**Méthode manuelle** :
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" --icon=app_icon.ico youtube_downloader.py
```

L'executable sera dans `dist\YouTube_MP3_Downloader.exe`

## Interface

1. **URL YouTube** : Collez l'URL de la vidéo
2. **Destination** : Choisissez le dossier de sortie
3. **Qualité Audio** : Sélectionnez la qualité (0-9)
4. **Télécharger** : Lancez le téléchargement

## Personnalisation

### Changer l'icône

Voir `CUSTOM_ICON.md` pour personnaliser l'icône de l'application.

```bash
# Générer une nouvelle icône
python create_icon.py
```

## Structure du projet

```
mp3_downloader/
├── youtube_downloader.py      # Application principale
├── create_icon.py             # Générateur d'icône
├── build_exe.bat              # Script de build exe
├── app_icon.ico               # Icône de l'application
├── requirements.txt           # Dépendances
├── .gitignore                 # Fichiers ignorés par git
├── BUILD_INSTRUCTIONS.md      # Guide de build détaillé
├── CUSTOM_ICON.md             # Guide personnalisation icône
└── README.md                  # Ce fichier
```

## Documentation

- `claude.md` : Documentation complète et détaillée
- `BUILD_INSTRUCTIONS.md` : Instructions pour créer l'executable
- `CUSTOM_ICON.md` : Guide de personnalisation de l'icône

## Dépannage

### yt-dlp non trouvé
```bash
yt-dlp --version  # Vérifier l'installation
pip install yt-dlp  # Réinstaller si nécessaire
```

### ffmpeg non trouvé
```bash
ffmpeg -version  # Vérifier l'installation
```

Téléchargez depuis https://ffmpeg.org/download.html et ajoutez au PATH.

## Licence

Projet créé pour un usage personnel.

## Auteur

Créé avec [Claude Code](https://claude.com/claude-code)
