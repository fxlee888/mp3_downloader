# Guide de Dépannage - YouTube MP3 Downloader

## Erreur 403 Forbidden

### Symptômes
```
ERROR: unable to download video data: HTTP Error 403: Forbidden
WARNING: No supported JavaScript runtime could be found
```

### Solutions (dans l'ordre)

#### 1. Mettre à jour yt-dlp (OBLIGATOIRE)

**Double-cliquez sur `update_ytdlp.bat`** ou exécutez :

```bash
pip install --upgrade yt-dlp
```

YouTube change régulièrement ses protections. Utilisez TOUJOURS la dernière version de yt-dlp.

#### 2. Installer Node.js (Recommandé)

yt-dlp nécessite un runtime JavaScript pour certaines vidéos YouTube.

**Option A : Installer Node.js**
1. Téléchargez depuis https://nodejs.org/
2. Installez la version LTS (Long Term Support)
3. Redémarrez votre terminal/application

**Option B : Installer Deno**
```bash
# Windows (PowerShell)
irm https://deno.land/install.ps1 | iex

# Avec Chocolatey
choco install deno
```

#### 3. Vérifier les versions

```bash
# Vérifier yt-dlp
yt-dlp --version

# Vérifier Node.js (si installé)
node --version

# Vérifier ffmpeg
ffmpeg -version
```

#### 4. Utiliser les cookies du navigateur (Alternative)

Si vous avez un compte YouTube Premium ou si vous êtes connecté :

Modifiez la commande dans le code pour ajouter :
```python
'--cookies-from-browser', 'chrome',  # ou 'firefox', 'edge', etc.
```

#### 5. Test manuel en ligne de commande

Testez si yt-dlp fonctionne en ligne de commande :

```bash
# Test basique
yt-dlp --print title "URL_YOUTUBE"

# Test avec les nouvelles options
yt-dlp -x --audio-format mp3 --extractor-args "youtube:player_client=android,ios" "URL_YOUTUBE"

# Test avec cookies
yt-dlp -x --audio-format mp3 --cookies-from-browser chrome "URL_YOUTUBE"
```

### Options ajoutées au code

Le code a été mis à jour avec ces options :

```python
'--extractor-args', 'youtube:player_client=android,ios'  # Utilise clients mobiles
'--no-check-certificates'  # Ignore erreurs de certificat
'--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
```

## Autres erreurs courantes

### "yt-dlp n'est pas trouvé"

**Solution :**
1. Vérifiez l'installation : `pip install yt-dlp`
2. Ajoutez Python et Scripts au PATH système
3. Redémarrez votre terminal/ordinateur

### "ffmpeg n'est pas trouvé"

**Solution :**
1. Téléchargez ffmpeg : https://ffmpeg.org/download.html
2. Ou utilisez Chocolatey : `choco install ffmpeg`
3. Ajoutez au PATH système
4. Redémarrez votre terminal/ordinateur

### Vidéo géo-restreinte

Certaines vidéos ne sont pas disponibles dans votre pays.

**Solution :**
- Utilisez un VPN
- Ou ajoutez l'option : `'--geo-bypass'` dans le code

### Vidéo à accès restreint (privée/non répertoriée)

**Solution :**
- Utilisez les cookies : `'--cookies-from-browser', 'chrome'`
- Ou exportez les cookies : `'--cookies', 'cookies.txt'`

### Playlist vs Vidéo unique

Pour télécharger une playlist entière :

**Solution :**
Ajoutez l'option : `'--yes-playlist'`

## Vérifications préalables

### Checklist avant téléchargement

- [ ] yt-dlp est à jour (dernière version)
- [ ] Node.js ou Deno est installé
- [ ] ffmpeg est installé et dans le PATH
- [ ] L'URL YouTube est complète et valide
- [ ] Vous avez une connexion internet stable
- [ ] Vous avez suffisamment d'espace disque

### URLs valides

✅ **Valides :**
- `https://www.youtube.com/watch?v=XXXXXXXXXXX`
- `https://youtu.be/XXXXXXXXXXX`
- `https://www.youtube.com/watch?v=XXXXXXXXXXX&t=10s`

❌ **Invalides :**
- `youtube.com/watch?v=XXX` (manque https://)
- `www.youtube.com` (pas de vidéo)
- URLs raccourcies non-YouTube

## Logs utiles pour diagnostic

Si le problème persiste, collectez ces informations :

```bash
# Version de yt-dlp
yt-dlp --version

# Version de ffmpeg
ffmpeg -version

# Version de Python
python --version

# Test de téléchargement avec logs détaillés
yt-dlp -v --print-traffic "URL_YOUTUBE"
```

## Modifications avancées du code

### Ajouter plus d'options de contournement

Dans `youtube_downloader.py`, ligne 182-191, vous pouvez ajouter :

```python
command = [
    'yt-dlp',
    '-x',
    '--audio-format', 'mp3',
    '--audio-quality', quality,
    '-o', os.path.join(destination, '%(title)s.%(ext)s'),
    '--extractor-args', 'youtube:player_client=android,ios',
    '--no-check-certificates',
    '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    # Options supplémentaires (décommenter si nécessaire)
    # '--cookies-from-browser', 'chrome',  # Utilise cookies Chrome
    # '--geo-bypass',  # Contourne restrictions géographiques
    # '--proxy', 'http://proxy:port',  # Utilise un proxy
    # '--socket-timeout', '30',  # Timeout pour connexion
    # '--retries', '10',  # Nombre de tentatives
    url
]
```

### Activer le mode verbose pour debugging

Ajoutez `'--verbose'` ou `'-v'` dans la commande pour plus de logs.

## Support et ressources

- **Documentation yt-dlp :** https://github.com/yt-dlp/yt-dlp
- **Issues yt-dlp :** https://github.com/yt-dlp/yt-dlp/issues
- **Wiki EJS (JavaScript runtime) :** https://github.com/yt-dlp/yt-dlp/wiki/EJS
- **SABR streaming issue :** https://github.com/yt-dlp/yt-dlp/issues/12482

## Résumé rapide

**Si vous avez l'erreur 403 :**

1. 🔄 **Mettre à jour yt-dlp** : `pip install --upgrade yt-dlp`
2. 📦 **Installer Node.js** : https://nodejs.org/
3. ✅ **Tester** : Relancer l'application
4. 🍪 **Si échec** : Ajouter `--cookies-from-browser chrome` dans le code
5. 🆘 **Si toujours échec** : Ouvrir une issue avec les logs détaillés
