# 📦 Utilisation de l'exécutable YouTube MP3 Downloader

## ✅ Exécutable créé avec succès !

**Emplacement :** `D:\Documents\FX\PROJECTS\mp3_downloader\dist\YouTube_MP3_Downloader.exe`

**Taille :** 11 MB

**Version :** Firefox avec cookies automatiques

---

## 🚀 Mise à jour de votre raccourci de startup

### **Étape 1 : Localiser votre raccourci**

Votre raccourci de startup est probablement ici :
```
C:\Users\fxlee\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
```

### **Étape 2 : Mettre à jour le chemin**

1. **Clic droit** sur le raccourci → **Propriétés**

2. **Modifier le champ "Cible"** :
   ```
   D:\Documents\FX\PROJECTS\mp3_downloader\dist\YouTube_MP3_Downloader.exe
   ```

3. **Modifier le champ "Démarrer dans"** :
   ```
   D:\Documents\FX\PROJECTS\mp3_downloader\dist
   ```

4. **Cliquer sur "OK"**

### **Étape 3 : Tester**

Double-cliquez sur l'exécutable pour vérifier qu'il se lance correctement :
```
D:\Documents\FX\PROJECTS\mp3_downloader\dist\YouTube_MP3_Downloader.exe
```

---

## 🎯 Ce que fait l'exécutable

✅ **Lance l'application avec interface graphique**
✅ **Utilise Firefox automatiquement** pour les cookies
✅ **Node.js intégré** pour résoudre les challenges YouTube
✅ **Configuration automatique** depuis %APPDATA%\yt-dlp\config

---

## 📋 Prérequis pour l'exécutable

L'exécutable est **autonome** mais nécessite :

| Composant | Requis | Raison |
|-----------|--------|--------|
| **Firefox** | ✅ Oui | Pour lire les cookies |
| **yt-dlp** | ✅ Oui | Pour télécharger |
| **Node.js** | ✅ Oui | Pour les challenges YouTube |
| **ffmpeg** | ✅ Oui | Pour convertir en MP3 |
| **Python** | ❌ Non | Embarqué dans l'exe |
| **tkinter** | ❌ Non | Embarqué dans l'exe |

### **Vérification rapide :**

```bash
# Vérifier que tout est installé
yt-dlp --version
node --version
ffmpeg -version

# Si quelque chose manque, réinstallez
pip install -U "yt-dlp[default]"
```

---

## 🔧 Configuration automatique

L'exécutable utilise automatiquement :

**1. Configuration yt-dlp**
- Emplacement : `C:\Users\fxlee\AppData\Roaming\yt-dlp\config`
- Contenu :
  ```
  --js-runtimes node
  --extractor-args "youtube:player_client=web;player_skip=configs"
  ```

**2. Cookies Firefox**
- Lus automatiquement depuis le profil Firefox
- Aucune configuration nécessaire

**3. Node.js**
- Détecté automatiquement : `D:\Program Files\nodejs\node.exe`
- Utilisé pour résoudre les signatures YouTube

---

## 🎵 Utilisation

### **Lancement manuel :**
Double-cliquez sur :
```
D:\Documents\FX\PROJECTS\mp3_downloader\dist\YouTube_MP3_Downloader.exe
```

### **Lancement automatique au démarrage :**
Le raccourci dans votre dossier Startup lancera l'application automatiquement.

### **Interface :**

1. **URL YouTube** : Collez l'URL de la vidéo
2. **Destination** : Choisissez où enregistrer (par défaut : Téléchargements)
3. **Qualité Audio** : 0 = meilleure, 9 = plus faible
4. **Navigateur** : Firefox (par défaut)
5. **Télécharger** : Cliquez et attendez !

---

## 🆘 Dépannage

### **L'exécutable ne se lance pas**

**Vérifiez les dépendances :**
```bash
yt-dlp --version
node --version
ffmpeg -version
```

**Testez en ligne de commande :**
```bash
yt-dlp --print title --cookies-from-browser firefox "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### **"yt-dlp n'est pas trouvé"**

L'exécutable appelle `yt-dlp` en externe. Vérifiez :
```bash
where yt-dlp
```

Si non trouvé :
```bash
pip install -U "yt-dlp[default]"
```

### **"Node.js non détecté"**

Vérifiez la configuration :
```bash
cat %APPDATA%\yt-dlp\config
```

Devrait contenir :
```
--js-runtimes node
```

### **"Firefox cookies not found"**

1. Ouvrez Firefox
2. Allez sur https://www.youtube.com/
3. Fermez Firefox complètement
4. Relancez l'exécutable

---

## 📊 Avantages de l'exécutable

| Avantage | Description |
|----------|-------------|
| **Autonome** | Pas besoin de Python installé |
| **Icône personnalisée** | Note de musique verte |
| **Portable** | Peut être copié sur une clé USB |
| **Startup** | Lance automatiquement au démarrage |
| **Simple** | Double-clic et c'est parti |

---

## 🔄 Reconstruire l'exécutable

Si vous modifiez le code Python, reconstruisez avec :

```bash
# Méthode automatique
build_firefox_version.bat

# Ou méthode manuelle
pyinstaller --onefile --windowed --name "YouTube_MP3_Downloader" --icon "app_icon.ico" youtube_downloader_cookies.py --clean
```

L'exécutable sera dans : `dist\YouTube_MP3_Downloader.exe`

---

## 📝 Notes importantes

### **Configuration partagée**

L'exécutable et le script Python partagent la même configuration :
- `%APPDATA%\yt-dlp\config`

Si vous modifiez cette configuration, les deux versions seront affectées.

### **Mise à jour de yt-dlp**

Pour mettre à jour yt-dlp :
```bash
pip install -U "yt-dlp[default]"
```

L'exécutable utilisera automatiquement la nouvelle version.

### **Logs et erreurs**

Les logs sont affichés dans l'interface graphique de l'application.

---

## 🎯 Résumé

**Votre exécutable est prêt !**

1. ✅ Exécutable créé : `dist\YouTube_MP3_Downloader.exe` (11 MB)
2. ✅ Icône personnalisée incluse
3. ✅ Firefox + Node.js + yt-dlp configurés
4. ✅ Prêt pour votre raccourci de startup

**Mettez à jour votre raccourci et profitez ! 🎵**

---

*Créé avec Claude Code - Février 2026*
