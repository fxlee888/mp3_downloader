# YouTube MP3 Downloader

Application Python avec interface graphique pour télécharger des musiques depuis YouTube au format MP3.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-Personal-green)

## Description

Cette application permet de télécharger facilement des vidéos YouTube et de les convertir en fichiers MP3 avec la qualité audio de votre choix. Interface graphique simple et intuitive.

## Fonctionnalités

- ✨ **Système multi-stratégies intelligent** - Essaie automatiquement 4 stratégies jusqu'au succès
- 🎨 Interface graphique tkinter (aucune dépendance externe)
- 📥 Téléchargement YouTube avec yt-dlp (dernière version)
- 🎵 Conversion automatique en MP3 haute qualité
- 🔧 Qualité audio personnalisable (0 = meilleure, 9 = plus faible)
- 📁 Sélection du dossier de destination
- 📊 Logs en temps réel avec progression détaillée
- 🍪 Support des cookies Firefox pour l'authentification
- 🚀 Génération d'executable Windows (.exe)
- 🎨 Icône personnalisée (note de musique verte)

## Prérequis

### Obligatoires
- **Python 3.x**
- **yt-dlp** (dernière version - mise à jour régulière requise)
- **ffmpeg** (pour la conversion MP3)
- **Node.js** (requis pour résoudre les challenges JavaScript de YouTube)

### Recommandés
- **Firefox** (pour l'authentification par cookies - meilleur taux de succès)

## Installation

### Méthode automatique (Recommandée)

Double-cliquez sur `install_dependencies.bat` pour installer/vérifier automatiquement toutes les dépendances.

### Méthode manuelle

```bash
# 1. Installer/Mettre à jour yt-dlp (IMPORTANT - à faire régulièrement)
pip install --upgrade yt-dlp

# 2. Installer Node.js (REQUIS)
# Téléchargez depuis: https://nodejs.org/
# Choisissez la version LTS (Long Term Support)
# Redémarrez après l'installation

# 3. Installer Firefox (RECOMMANDÉ)
# Téléchargez depuis: https://www.mozilla.org/firefox/

# 4. Installer ffmpeg
# Windows: https://ffmpeg.org/download.html
# Ou avec chocolatey: choco install ffmpeg
```

### Vérifier les installations

```bash
yt-dlp --version   # Devrait afficher 2025.x ou plus récent
node --version     # Devrait afficher v16.x ou plus récent
ffmpeg -version    # Devrait afficher la version de ffmpeg
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

### Option 3 : Mode CLI en lot (download_batch.py)

Pour télécharger plusieurs vidéos d'un coup, sans interface graphique, utilisez `download_batch.py`. Il réutilise le même système multi-stratégies que l'application GUI (voir `download_strategies.py`).

**Syntaxe :**

```bash
python download_batch.py [urls...] -d DESTINATION [-f FICHIER] [-q QUALITE]
```

| Option | Description |
|---|---|
| `urls` (positionnel) | Une ou plusieurs URLs YouTube, séparées par des espaces |
| `-f`, `--file` | Fichier texte avec une URL par ligne (les lignes vides ou commençant par `#` sont ignorées) |
| `-d`, `--destination` | **Obligatoire.** Dossier de destination (créé automatiquement s'il n'existe pas) |
| `-q`, `--quality` | Qualité audio 0-9 (0 = meilleure, défaut) |

**Exemples :**

```bash
# Une ou plusieurs URLs directement en argument
python download_batch.py "https://www.youtube.com/watch?v=XXXX" -d "D:\Musique" -q 0

# Liste d'URLs depuis un fichier texte (une URL par ligne)
python download_batch.py -f "urls.txt" -d "D:\Musique" -q 5
```

Le script traite les URLs une par une, affiche la progression et un résumé final (`X/Y téléchargements réussis`). Les URLs contenant un paramètre `&list=` ne téléchargent que la vidéo ciblée (`--no-playlist`), jamais la playlist entière.

## Système Multi-Stratégies

L'application utilise un **système intelligent de tentatives multiples** pour maximiser les chances de succès :

1. 🟢 **Cookies Firefox + Client Android** - Idéal pour vidéos avec authentification
2. 🟢 **Cookies Firefox + Client Web** - Stratégie par défaut (la plus fiable)
3. 🟡 **Sans cookies + Client iOS** - Pour vidéos publiques
4. 🟡 **Mode basique** - Dernière tentative de secours

Si une stratégie échoue, l'application passe automatiquement à la suivante. Vous verrez dans les logs quelle stratégie a réussi !

## Interface

1. **URL YouTube** : Collez l'URL de la vidéo
2. **Destination** : Choisissez le dossier de sortie
3. **Qualité Audio** : Sélectionnez la qualité (0-9)
4. **Télécharger** : Lancez le téléchargement
5. **Logs** : Suivez la progression en temps réel

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
├── youtube_downloader.py      # Application principale (GUI)
├── download_batch.py          # Téléchargement en lot (CLI)
├── download_strategies.py     # Stratégies yt-dlp partagées (GUI + CLI)
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

- `CLAUDE.md` : Documentation complète et détaillée du projet
- `TROUBLESHOOTING.md` : **Guide de dépannage complet** (erreurs 403, problèmes de téléchargement, etc.)
- `BUILD_INSTRUCTIONS.md` : Instructions pour créer l'executable
- `CUSTOM_ICON.md` : Guide de personnalisation de l'icône

## Dépannage

### ⚠️ Erreur 403 / Signature solving failed

**Solutions rapides :**
1. Double-cliquez sur `update_ytdlp.bat` (OBLIGATOIRE)
2. Vérifiez que Node.js est installé : `node --version`
3. Vérifiez que Firefox est installé
4. Redémarrez votre ordinateur
5. Relancez l'application

**📖 Pour plus de détails, consultez `TROUBLESHOOTING.md`**

### yt-dlp non trouvé
```bash
yt-dlp --version              # Vérifier l'installation
pip install --upgrade yt-dlp  # Installer/Mettre à jour
```

### Node.js non trouvé
```bash
node --version  # Vérifier l'installation
```
Si non installé : https://nodejs.org/ (version LTS)

### ffmpeg non trouvé
```bash
ffmpeg -version  # Vérifier l'installation
```
Si non installé : https://ffmpeg.org/download.html

### "Skipping client X since it does not support cookies"

C'est **normal** ! L'application essaie automatiquement la stratégie suivante. Aucune action requise.

## Licence

Projet créé pour un usage personnel.

## Auteur

Créé avec [Claude Code](https://claude.com/claude-code)
