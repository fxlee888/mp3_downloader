# Comment personnaliser l'icône de l'application

## Icône actuelle

L'application utilise maintenant une icône personnalisée avec une note de musique verte.

Fichier : `app_icon.ico`

## Option 1 : Utiliser votre propre icône

Si vous avez déjà un fichier .ico :

1. **Remplacez** le fichier `app_icon.ico` par votre icône
2. **Lancez** `build_exe.bat` pour reconstruire l'exe
3. Votre nouvelle icône sera appliquée

## Option 2 : Convertir une image en .ico

Si vous avez une image (PNG, JPG, etc.) :

### Sites en ligne (gratuits)

- **ConvertICO** : https://convertico.com/
- **ICO Convert** : https://icoconvert.com/
- **Online-Convert** : https://image.online-convert.com/convert-to-ico

### Étapes :

1. Téléchargez votre image sur un de ces sites
2. Choisissez les tailles (recommandé : 16, 32, 48, 64, 128, 256)
3. Téléchargez le fichier .ico généré
4. Renommez-le en `app_icon.ico`
5. Placez-le dans le dossier du projet
6. Lancez `build_exe.bat`

## Option 3 : Générer une nouvelle icône avec Python

Vous pouvez modifier le script `create_icon.py` pour créer votre propre design :

```bash
python create_icon.py
```

Le script crée une icône avec :
- Fond vert (couleur personnalisable)
- Note de musique blanche
- Multiples tailles (16x16 à 256x256)

### Personnaliser les couleurs

Éditez `create_icon.py` et modifiez :

```python
# Ligne pour changer la couleur de fond
img = Image.new('RGB', (size, size), color='#1DB954')  # Vert
# Changez '#1DB954' par votre couleur (format hexadécimal)

# Exemples de couleurs :
# Rouge : '#FF0000'
# Bleu : '#0000FF'
# Orange : '#FF8C00'
# Violet : '#9B59B6'
# Noir : '#000000'
```

## Option 4 : Télécharger des icônes gratuites

Sites avec icônes gratuites :

- **Flaticon** : https://www.flaticon.com/ (cherchez "music", "download", etc.)
- **Icons8** : https://icons8.com/
- **IconArchive** : https://iconarchive.com/

Assurez-vous que l'icône est :
- Au format .ico
- Ou convertissez-la avec un site en ligne

## Spécifications techniques

Pour une icône optimale :

- **Format** : .ico (Windows Icon)
- **Tailles recommandées** : 16, 32, 48, 64, 128, 256 pixels
- **Profondeur** : 32 bits (pour transparence)
- **Fond** : Transparent ou opaque selon préférence

## Reconstruire l'exe après changement d'icône

Après avoir changé l'icône :

```bash
# Double-cliquez sur :
build_exe.bat

# Ou en ligne de commande :
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" --icon=app_icon.ico youtube_downloader.py
```

## Vérifier que l'icône a changé

1. Allez dans le dossier `dist\`
2. L'icône de `YouTube_MP3_Downloader.exe` devrait afficher votre nouvelle icône
3. Clic droit → Propriétés → Vérifiez l'icône dans l'onglet Général

## Dépendances pour create_icon.py

Si vous voulez utiliser le script Python pour créer des icônes :

```bash
pip install Pillow
```

Pillow est une bibliothèque de traitement d'images pour Python.
