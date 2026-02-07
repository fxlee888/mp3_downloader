# 🔴 FIX : Erreur 403 Forbidden - YouTube

## ⚡ Solution Rapide (3 étapes)

### 1️⃣ Mettez à jour yt-dlp
Double-cliquez sur : **`update_ytdlp.bat`**

Ou en ligne de commande :
```bash
pip install --upgrade yt-dlp
```

### 2️⃣ Installez Node.js (IMPORTANT)
- Téléchargez : https://nodejs.org/
- Choisissez la version **LTS** (Long Term Support)
- Installez avec les options par défaut
- **Redémarrez votre ordinateur**

### 3️⃣ Relancez l'application
Le code a déjà été mis à jour avec les options nécessaires.

---

## 🛠️ Vérification

Testez si tout fonctionne :

```bash
# 1. Vérifiez yt-dlp
yt-dlp --version

# 2. Vérifiez Node.js
node --version

# 3. Test de téléchargement
yt-dlp --print title "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

---

## ❓ Ça ne fonctionne toujours pas ?

### Option A : Utilisez les cookies de votre navigateur

Si vous êtes connecté à YouTube ou avez YouTube Premium :

1. Ouvrez `youtube_downloader.py` ligne 182-191
2. Ajoutez cette ligne dans la commande :
```python
'--cookies-from-browser', 'chrome',  # ou 'firefox', 'edge'
```

### Option B : Vérifiez vos dépendances

Double-cliquez sur : **`install_dependencies.bat`**

Cela vérifiera et installera toutes les dépendances nécessaires.

---

## 📖 Documentation complète

- **Guide de dépannage complet** : Voir `TROUBLESHOOTING.md`
- **Documentation principale** : Voir `CLAUDE.md`

---

## 🔍 Pourquoi cette erreur ?

YouTube a renforcé ses protections anti-bots en 2025-2026. Les changements incluent :

1. **Besoin d'un runtime JavaScript** (Node.js ou Deno)
2. **Nouvelles méthodes de streaming** (SABR)
3. **Vérifications plus strictes** des user-agents

yt-dlp nécessite maintenant :
- La dernière version (mises à jour régulières)
- Un runtime JavaScript (Node.js recommandé)
- Des options spéciales pour contourner les restrictions

---

## ✅ Modifications du code

Le fichier `youtube_downloader.py` a été automatiquement mis à jour avec :

```python
'--extractor-args', 'youtube:player_client=android,ios'  # Clients mobiles
'--no-check-certificates'  # Ignore erreurs certificat
'--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
```

Ces options permettent de contourner les restrictions de YouTube.

---

## 🆘 Support

Si le problème persiste après avoir suivi toutes les étapes :

1. Collectez les informations de version :
```bash
yt-dlp --version
node --version
ffmpeg -version
python --version
```

2. Testez avec logs détaillés :
```bash
yt-dlp -v "URL_YOUTUBE"
```

3. Consultez les issues GitHub de yt-dlp : https://github.com/yt-dlp/yt-dlp/issues

---

## 📌 Checklist

- [ ] yt-dlp mis à jour vers la dernière version
- [ ] Node.js installé (version LTS)
- [ ] Ordinateur redémarré
- [ ] Application relancée
- [ ] Test de téléchargement effectué

**Si toutes les cases sont cochées et que ça ne fonctionne toujours pas**, consultez `TROUBLESHOOTING.md` pour les solutions avancées.
