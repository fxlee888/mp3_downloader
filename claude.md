# YouTube MP3 Downloader

Application Python avec interface graphique pour télécharger des musiques depuis YouTube au format MP3.

## Description

Cette application permet de télécharger facilement des vidéos YouTube et de les convertir en fichiers MP3 avec la qualité audio de votre choix. Elle utilise `yt-dlp` et `ffmpeg` pour effectuer les téléchargements et conversions.

## Prérequis

- Python 3.x
- yt-dlp (dernière version)
- ffmpeg (installé)
- **Node.js (RECOMMANDÉ)** - Requis pour certaines vidéos YouTube

## Installation des dépendances

### Méthode automatique (Recommandée)

Double-cliquez sur `install_dependencies.bat` pour installer/vérifier automatiquement toutes les dépendances.

### Méthode manuelle

Si vous n'avez pas encore installé les outils nécessaires :

```bash
# 1. Installer/Mettre à jour yt-dlp (IMPORTANT)
pip install --upgrade yt-dlp

# 2. Installer ffmpeg (Windows)
# Téléchargez depuis https://ffmpeg.org/download.html
# Ou utilisez chocolatey: choco install ffmpeg

# 3. Installer Node.js (RECOMMANDÉ)
# Téléchargez depuis https://nodejs.org/
# Choisissez la version LTS (Long Term Support)
```

**⚠️ IMPORTANT :** YouTube change régulièrement ses protections. Mettez TOUJOURS à jour yt-dlp avant utilisation avec `update_ytdlp.bat` ou `pip install --upgrade yt-dlp`.

## Utilisation

### Option 1 : Lancer avec Python

```bash
python youtube_downloader.py
```

### Option 2 : Créer un fichier .exe (Recommandé)

Pour créer un executable .exe et lancer l'application sans passer par Python :

**Méthode automatique** :
1. Double-cliquez sur `build_exe.bat`
2. Attendez la fin de la compilation
3. L'executable sera dans `dist\YouTube_MP3_Downloader.exe`

**Méthode manuelle** :
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" youtube_downloader.py
```

Voir `BUILD_INSTRUCTIONS.md` pour plus de détails.

**Personnalisation de l'icône** :
- L'application utilise une icône personnalisée (note de musique verte)
- Vous pouvez créer votre propre icône avec `python create_icon.py`
- Ou remplacer `app_icon.ico` par votre propre fichier .ico
- Voir `CUSTOM_ICON.md` pour plus d'options

### Interface graphique

L'application présente une interface simple avec :

1. **URL YouTube** : Collez l'URL de la vidéo YouTube à télécharger
2. **Destination** : Sélectionnez le dossier où enregistrer le fichier MP3
   - Par défaut : dossier "Téléchargements"
   - Cliquez sur "Parcourir..." pour changer
3. **Qualité Audio** : Menu déroulant pour choisir la qualité
   - **0** = Meilleure qualité (recommandé)
   - **9** = Qualité la plus faible
   - Valeurs intermédiaires : 1-8
4. **Bouton Télécharger** : Lance le téléchargement
5. **Zone de logs** : Affiche la progression et les messages

## Qualité Audio

L'option `--audio-quality` accepte des valeurs de 0 à 9 :

- **0** : Meilleure qualité audio disponible (fichier plus volumineux)
- **4** : Qualité moyenne (bon compromis)
- **9** : Qualité la plus faible (fichier plus petit)

## Fonctionnalités

- Interface graphique intuitive avec tkinter
- Sélection facile du dossier de destination
- Choix de la qualité audio (0-9)
- Affichage en temps réel de la progression
- Support de tous les formats vidéo YouTube
- Conversion automatique en MP3
- Logs détaillés du processus

## Commande équivalente en ligne de commande

L'application exécute la commande suivante :

```bash
yt-dlp -x --audio-format mp3 --audio-quality [QUALITE] [URL]
```

Options :
- `-x` : Extrait uniquement l'audio
- `--audio-format mp3` : Convertit en format MP3
- `--audio-quality [0-9]` : Définit la qualité audio
- `-o` : Template pour le nom du fichier de sortie

## Structure du projet

```
mp3_downloader/
├── youtube_downloader.py      # Application principale
├── build_exe.bat              # Script pour créer l'executable
├── install_dependencies.bat   # Installation automatique des dépendances
├── update_ytdlp.bat           # Mise à jour rapide de yt-dlp
├── create_icon.py             # Script pour générer une icône personnalisée
├── app_icon.ico               # Icône de l'application (note de musique)
├── requirements.txt           # Dépendances Python
├── BUILD_INSTRUCTIONS.md      # Instructions détaillées pour créer l'exe
├── CUSTOM_ICON.md             # Guide pour personnaliser l'icône
├── TROUBLESHOOTING.md         # Guide de dépannage complet (Erreur 403, etc.)
├── CLAUDE.md                  # Documentation principale
└── dist/                      # Dossier contenant l'executable après build
    └── YouTube_MP3_Downloader.exe
```

## Caractéristiques techniques

### Architecture

- **Interface graphique** : tkinter (bibliothèque standard Python)
- **Téléchargement** : yt-dlp via subprocess
- **Threading** : Téléchargement asynchrone pour ne pas bloquer l'interface
- **Validation** : Vérification des entrées utilisateur

### Composants principaux

- `YouTubeDownloader` : Classe principale de l'application
  - `setup_ui()` : Configuration de l'interface graphique
  - `browse_destination()` : Dialogue de sélection de dossier
  - `validate_inputs()` : Validation des champs
  - `start_download()` : Lance le téléchargement dans un thread
  - `download()` : Effectue le téléchargement avec yt-dlp
  - `log()` : Affiche des messages dans la zone de logs
  - `update_status()` : Met à jour la barre de statut

## Gestion des erreurs

L'application gère les erreurs suivantes :

- URL manquante ou invalide
- Dossier de destination inexistant
- yt-dlp non trouvé dans le PATH
- Erreurs de téléchargement
- Téléchargement déjà en cours

## Messages d'état

- **Prêt** : Application en attente
- **Téléchargement en cours...** : Téléchargement actif
- **Téléchargement réussi** : Terminé avec succès
- **Erreur** : Problème rencontré (voir logs)

## Conseils d'utilisation

1. **Qualité recommandée** : Utilisez 0 pour la meilleure qualité
2. **Vérifiez l'URL** : Assurez-vous que l'URL YouTube est complète
3. **Espace disque** : Vérifiez que vous avez suffisamment d'espace
4. **Connexion internet** : Une connexion stable améliore les téléchargements
5. **Formats supportés** : Fonctionne avec toutes les vidéos YouTube publiques

## Dépannage

### 🔴 Erreur 403 Forbidden (Erreur YouTube)

**Symptômes :**
```
ERROR: unable to download video data: HTTP Error 403: Forbidden
WARNING: No supported JavaScript runtime could be found
```

**Solutions rapides :**

1. **Double-cliquez sur `update_ytdlp.bat`** - Met à jour yt-dlp (OBLIGATOIRE)
2. **Installez Node.js** depuis https://nodejs.org/ (version LTS)
3. **Redémarrez** votre ordinateur après l'installation
4. **Relancez** l'application

**Le code a été mis à jour automatiquement** avec les options suivantes pour contourner les restrictions YouTube :
- Utilisation des clients mobiles (Android/iOS)
- User-agent personnalisé
- Ignore les erreurs de certificat

📖 **Pour plus de détails, consultez `TROUBLESHOOTING.md`**

### yt-dlp non trouvé

Si vous obtenez l'erreur "yt-dlp n'est pas trouvé" :

1. Double-cliquez sur `install_dependencies.bat`
2. Ou manuellement : `pip install yt-dlp`
3. Vérifiez l'installation : `yt-dlp --version`
4. Ajoutez Python au PATH système si nécessaire

### ffmpeg non trouvé

Si la conversion échoue :

1. Double-cliquez sur `install_dependencies.bat` pour vérifier
2. Vérifiez l'installation : `ffmpeg -version`
3. Téléchargez depuis https://ffmpeg.org/download.html
4. Ou utilisez Chocolatey : `choco install ffmpeg`
5. Ajoutez ffmpeg au PATH système

### Erreur de téléchargement générique

- Vérifiez que l'URL YouTube est complète et correcte
- Vérifiez votre connexion internet
- Mettez à jour yt-dlp : `pip install --upgrade yt-dlp`
- Consultez `TROUBLESHOOTING.md` pour plus de solutions
- Consultez les logs dans l'application pour plus de détails

## Améliorations futures possibles

- Support de playlists YouTube
- Choix du format audio (MP3, AAC, FLAC, etc.)
- Téléchargements multiples simultanés
- Historique des téléchargements
- Ajout de métadonnées (titre, artiste, album)
- Miniatures automatiques
- Mode dark/light

## Licence

Projet créé pour un usage personnel.

## Auteur

Créé avec Claude Code
