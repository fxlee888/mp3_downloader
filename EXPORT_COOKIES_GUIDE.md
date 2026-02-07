# 🍪 Guide : Exporter les cookies YouTube

## Pourquoi exporter les cookies ?

YouTube demande maintenant : **"Sign in to confirm you're not a bot"**

Les cookies permettent à yt-dlp de télécharger comme si c'était vous (utilisateur authentifié).

---

## ⭐ Méthode 1 : Extension de navigateur (RECOMMANDÉE)

### Pour Chrome / Edge / Brave

1. **Installez l'extension "Get cookies.txt LOCALLY"**
   - Chrome Web Store : https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
   - C'est une extension open-source qui exporte les cookies localement

2. **Allez sur YouTube**
   - Ouvrez : https://www.youtube.com/
   - Assurez-vous d'être connecté (si vous avez un compte)

3. **Exportez les cookies**
   - Cliquez sur l'icône de l'extension (puzzle en haut à droite)
   - Cliquez sur "Get cookies.txt LOCALLY"
   - Cliquez sur "Export" ou l'icône de téléchargement
   - Les cookies sont automatiquement téléchargés dans un fichier `youtube.com_cookies.txt`

4. **Déplacez le fichier**
   ```
   Déplacez le fichier téléchargé vers :
   D:\Documents\FX\PROJECTS\mp3_downloader\youtube_cookies.txt
   ```

5. **Utilisez la version avec fichier cookies**
   ```bash
   python youtube_downloader_with_cookies_file.py
   ```

---

### Pour Firefox

1. **Installez l'extension "cookies.txt"**
   - Firefox Add-ons : https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/

2. **Allez sur YouTube**
   - Ouvrez : https://www.youtube.com/
   - Connectez-vous si nécessaire

3. **Exportez les cookies**
   - Cliquez sur l'icône de l'extension
   - Cliquez sur "Export Cookies"
   - Sauvegardez le fichier comme `youtube_cookies.txt`

4. **Déplacez le fichier vers le dossier du projet**

---

## 🔧 Méthode 2 : Ligne de commande (AVANCÉ)

### Avec Chrome

Si vous avez installé `pycryptodomex` (via `fix_chrome_cookies.bat`) :

```bash
# Testez d'abord si ça fonctionne
yt-dlp --cookies-from-browser chrome --print title "https://www.youtube.com/watch?v=3ArJlad2q74"

# Si ça fonctionne, exportez les cookies
yt-dlp --cookies-from-browser chrome --cookies cookies.txt --skip-download "https://www.youtube.com/"
```

### Avec Firefox (pas de problème DPAPI)

```bash
# Firefox fonctionne directement
yt-dlp --cookies-from-browser firefox --print title "https://www.youtube.com/watch?v=3ArJlad2q74"

# Exportez les cookies
yt-dlp --cookies-from-browser firefox --cookies youtube_cookies.txt --skip-download "https://www.youtube.com/"
```

---

## 📋 Vérification du fichier cookies

Le fichier `youtube_cookies.txt` doit ressembler à ça :

```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	TRUE	...	CONSENT	YES+...
.youtube.com	TRUE	/	FALSE	...	VISITOR_INFO1_LIVE	...
...
```

---

## 🚀 Utilisation après export

Une fois le fichier `youtube_cookies.txt` créé :

```bash
python youtube_downloader_with_cookies_file.py
```

Ou testez en ligne de commande :

```bash
yt-dlp -x --audio-format mp3 --cookies youtube_cookies.txt "https://www.youtube.com/watch?v=3ArJlad2q74"
```

---

## ❓ Problèmes courants

### Les cookies expirent
- **Solution :** Ré-exportez les cookies régulièrement (tous les mois)

### L'extension ne fonctionne pas
- **Solution :** Essayez l'autre méthode (Firefox ou ligne de commande)

### "Invalid cookie file"
- **Solution :** Vérifiez que le fichier est au bon format (Netscape)

---

## 🔗 Liens utiles

- **Extension Chrome :** https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
- **Extension Firefox :** https://addons.mozilla.org/firefox/addon/cookies-txt/
- **Wiki yt-dlp :** https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp

---

## 💡 Conseil de sécurité

⚠️ **Ne partagez JAMAIS votre fichier cookies !**
- Il contient vos informations de connexion
- Quelqu'un pourrait accéder à votre compte YouTube avec ces cookies
- Gardez le fichier dans le dossier du projet uniquement
