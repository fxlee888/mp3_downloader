# Guide de Dépannage - YouTube MP3 Downloader

## 🆕 Système Multi-Stratégies (Mis à jour !)

L'application utilise maintenant un **système intelligent avec 4 stratégies** qui s'exécutent automatiquement jusqu'à ce qu'une fonctionne.

### Les 4 Stratégies (dans l'ordre)

1. **🟢 Cookies Firefox + Client Android**
   - Utilise vos cookies Firefox pour l'authentification
   - Client Android (compatible cookies)
   - Idéal pour vidéos nécessitant une connexion

2. **🟢 Cookies Firefox + Client Web**
   - Client web par défaut avec authentification
   - Fonctionne pour la plupart des vidéos
   - **Stratégie la plus fiable actuellement**

3. **🟡 Sans cookies + Client iOS**
   - Client iOS sans authentification
   - Pour vidéos publiques sans restrictions
   - Plus léger mais moins polyvalent

4. **🟡 Mode basique**
   - Utilise uniquement les composants distants
   - Dernière tentative de secours
   - Mode minimal

### 🎯 Ce qui se passe automatiquement

✅ Si **Stratégie 1** échoue → Essaie **Stratégie 2**
✅ Si **Stratégie 2** échoue → Essaie **Stratégie 3**
✅ Si **Stratégie 3** échoue → Essaie **Stratégie 4**
❌ Si **toutes échouent** → Message d'erreur avec suggestions

## 🔴 Erreur 403 Forbidden / Signature solving failed

### Symptômes
```
ERROR: unable to download video data: HTTP Error 403: Forbidden
WARNING: [youtube] [jsc] Remote component challenge solver script (node) was skipped
WARNING: Signature solving failed: Some formats may be missing
WARNING: n challenge solving failed
ERROR: Requested format is not available
WARNING: Only images are available for download
```

### Solutions (dans l'ordre)

#### 1. ✅ Mettre à jour yt-dlp (OBLIGATOIRE)

**Double-cliquez sur `update_ytdlp.bat`** ou exécutez :

```bash
pip install --upgrade yt-dlp
```

⚠️ **IMPORTANT :** YouTube change régulièrement ses protections. Utilisez TOUJOURS la dernière version de yt-dlp.

#### 2. ✅ Installer Node.js (REQUIS)

yt-dlp nécessite Node.js pour résoudre les challenges JavaScript de YouTube.

**Installation :**
1. Téléchargez depuis https://nodejs.org/
2. Choisissez la version **LTS (Long Term Support)**
3. Installez avec les options par défaut
4. **Redémarrez votre ordinateur**
5. Vérifiez : `node --version`

**Pourquoi Node.js est requis ?**
- YouTube impose des "signature challenges" et "n challenges"
- Ces protections JavaScript nécessitent un runtime JS
- Node.js résout automatiquement ces challenges

#### 3. ✅ Installer Firefox (Recommandé)

Firefox est utilisé pour l'authentification par cookies.

**Installation :**
1. Téléchargez depuis https://www.mozilla.org/firefox/
2. Installez normalement
3. Ouvrez Firefox au moins une fois
4. Visitez youtube.com (optionnel : connectez-vous)

**Pourquoi Firefox ?**
- Les stratégies 1 et 2 utilisent vos cookies Firefox
- Permet d'accéder aux vidéos restreintes
- Meilleur taux de succès

**Alternative :**
Vous pouvez modifier le code pour utiliser Chrome :
```python
'--cookies-from-browser', 'chrome',  # Au lieu de 'firefox'
```

#### 4. ✅ Vérifier votre connexion internet

L'application télécharge automatiquement des composants depuis GitHub :
- `--remote-components ejs:github` télécharge des scripts de résolution
- Ces scripts sont nécessaires pour contourner les protections YouTube
- Une connexion internet stable est requise

#### 5. ✅ Vérifier les versions

```bash
# Vérifier yt-dlp (minimum 2025.x)
yt-dlp --version

# Vérifier Node.js (minimum 16.x)
node --version

# Vérifier ffmpeg
ffmpeg -version

# Vérifier Python
python --version
```

### Options utilisées par le code

Le code utilise maintenant ces options avancées :

**Pour toutes les stratégies :**
```python
'--remote-components', 'ejs:github',  # OBLIGATOIRE - Télécharge scripts de résolution
'--no-check-certificates',            # Ignore erreurs de certificat
'--extractor-retries', '3',           # 3 tentatives par stratégie
```

**Stratégie 1 & 2 (avec cookies) :**
```python
'--cookies-from-browser', 'firefox',  # Utilise cookies Firefox
'--extractor-args', 'youtube:player_client=android',  # Client Android (stratégie 1)
```

**Stratégie 3 (sans cookies) :**
```python
'--extractor-args', 'youtube:player_client=ios',  # Client iOS
'--user-agent', 'Mozilla/5.0 (iPhone; ...)',      # User-agent iOS
```

## Autres erreurs courantes

### "yt-dlp n'est pas trouvé"

**Symptôme :**
```
FileNotFoundError: yt-dlp
```

**Solution :**
1. Installez yt-dlp : `pip install yt-dlp`
2. Vérifiez : `yt-dlp --version`
3. Ajoutez Python/Scripts au PATH système si nécessaire
4. Redémarrez votre terminal/ordinateur

### "ffmpeg n'est pas trouvé"

**Symptôme :**
La conversion MP3 échoue après le téléchargement.

**Solution :**
1. **Option A - Téléchargement manuel :**
   - Téléchargez depuis https://ffmpeg.org/download.html
   - Extrayez et ajoutez au PATH système

2. **Option B - Chocolatey :**
   ```bash
   choco install ffmpeg
   ```

3. Vérifiez : `ffmpeg -version`
4. Redémarrez votre ordinateur

### "Skipping client X since it does not support cookies"

**Symptôme :**
```
WARNING: Skipping client "android" since it does not support cookies
WARNING: Skipping client "ios" since it does not support cookies
```

**Explication :**
- C'est **normal** ! L'application essaie automatiquement la stratégie suivante
- Les clients Android/iOS ne supportent pas toujours les cookies
- L'application passera à une stratégie compatible

**Aucune action requise** - Le système multi-stratégies gère cela automatiquement.

### Vidéo géo-restreinte

**Symptôme :**
```
ERROR: This video is not available in your country
```

**Solution :**
- Utilisez un VPN
- Ou modifiez le code pour ajouter : `'--geo-bypass'`

### Vidéo privée / non répertoriée

**Symptôme :**
```
ERROR: This video is private
ERROR: This video is unavailable
```

**Solution :**
- Assurez-vous d'être connecté à YouTube dans Firefox
- Les cookies Firefox donneront accès aux vidéos de votre compte
- Ou utilisez : `'--cookies', 'cookies.txt'` (export manuel)

### Vidéo restreinte par âge

**Solution :**
Les cookies Firefox permettent généralement de contourner cette restriction si vous êtes connecté.

### Playlist vs Vidéo unique

**Pour télécharger une playlist entière :**

Modifiez le code pour ajouter :
```python
'--yes-playlist',  # Active le téléchargement de playlist
```

**Pour télécharger UNE SEULE vidéo d'une playlist :**
```python
'--no-playlist',  # Force vidéo unique
```

## Vérifications préalables

### Checklist avant téléchargement

- [ ] yt-dlp est à jour (dernière version 2025.x)
- [ ] Node.js est installé (version LTS 16.x ou plus)
- [ ] Firefox est installé (pour les cookies)
- [ ] ffmpeg est installé et dans le PATH
- [ ] L'URL YouTube est complète et valide
- [ ] Vous avez une connexion internet stable
- [ ] Vous avez suffisamment d'espace disque

### URLs valides

✅ **Valides :**
- `https://www.youtube.com/watch?v=XXXXXXXXXXX`
- `https://youtu.be/XXXXXXXXXXX`
- `https://www.youtube.com/watch?v=XXXXXXXXXXX&t=10s`
- `https://www.youtube.com/watch?v=XXXXXXXXXXX&list=YYYYYYY` (vidéo dans playlist)

❌ **Invalides :**
- `youtube.com/watch?v=XXX` (manque https://)
- `www.youtube.com` (pas de vidéo)
- URLs raccourcies non-YouTube
- URLs de shorts (parfois problématiques)

## Test manuel en ligne de commande

Si l'application échoue, testez directement en ligne de commande :

### Test basique
```bash
yt-dlp --print title "URL_YOUTUBE"
```

### Test avec composants distants (recommandé)
```bash
yt-dlp -x --audio-format mp3 --remote-components ejs:github "URL_YOUTUBE"
```

### Test avec cookies Firefox
```bash
yt-dlp -x --audio-format mp3 --remote-components ejs:github --cookies-from-browser firefox "URL_YOUTUBE"
```

### Test avec client Android
```bash
yt-dlp -x --audio-format mp3 --remote-components ejs:github --cookies-from-browser firefox --extractor-args "youtube:player_client=android" "URL_YOUTUBE"
```

### Test avec logs détaillés (debugging)
```bash
yt-dlp -v --print-traffic --remote-components ejs:github "URL_YOUTUBE"
```

## Logs utiles pour diagnostic

Si le problème persiste, collectez ces informations :

```bash
# Versions
yt-dlp --version
node --version
ffmpeg -version
python --version

# Test avec logs détaillés
yt-dlp -v --remote-components ejs:github "URL_YOUTUBE" > logs.txt 2>&1
```

Ensuite, ouvrez une issue avec ces logs sur :
- https://github.com/yt-dlp/yt-dlp/issues (pour yt-dlp)
- Ou consultez la documentation du projet

## Modifications avancées du code

### Utiliser Chrome au lieu de Firefox

Dans `youtube_downloader.py`, remplacez dans les stratégies :
```python
'--cookies-from-browser', 'chrome',  # Au lieu de 'firefox'
```

Navigateurs supportés : `chrome`, `firefox`, `edge`, `opera`, `brave`, `safari`

### Ajouter des options supplémentaires

Ajoutez dans les stratégies existantes :
```python
# Contourne restrictions géographiques
'--geo-bypass',

# Utilise un proxy
'--proxy', 'http://proxy:port',

# Timeout de connexion
'--socket-timeout', '30',

# Mode verbose pour debugging
'--verbose',

# Limite de vitesse
'--limit-rate', '1M',
```

### Créer une nouvelle stratégie personnalisée

Dans `youtube_downloader.py`, ajoutez dans la liste `strategies` :
```python
{
    'name': 'Ma stratégie personnalisée',
    'args': [
        '--remote-components', 'ejs:github',
        '--cookies-from-browser', 'chrome',  # Votre navigateur
        '--geo-bypass',                       # Vos options
        # ... autres options
    ]
}
```

## Support et ressources

- **Documentation yt-dlp :** https://github.com/yt-dlp/yt-dlp
- **Wiki EJS (JavaScript runtime) :** https://github.com/yt-dlp/yt-dlp/wiki/EJS
- **Remote components :** https://github.com/yt-dlp/yt-dlp/wiki/Remote-components
- **Issues yt-dlp :** https://github.com/yt-dlp/yt-dlp/issues
- **SABR streaming issue :** https://github.com/yt-dlp/yt-dlp/issues/12482
- **Node.js :** https://nodejs.org/

## Résumé rapide

**Si vous avez l'erreur 403 / Signature solving failed :**

1. 🔄 **Mettre à jour yt-dlp** : `pip install --upgrade yt-dlp` (OBLIGATOIRE)
2. 📦 **Installer Node.js** : https://nodejs.org/ (REQUIS)
3. 🦊 **Installer Firefox** : https://www.mozilla.org/firefox/ (Recommandé)
4. 🌐 **Vérifier internet** : Connexion stable requise
5. 🔄 **Redémarrer** : Redémarrez votre ordinateur
6. ✅ **Tester** : Relancer l'application

**Le système multi-stratégies devrait résoudre la plupart des problèmes automatiquement !**

---

**Note :** Si toutes les stratégies échouent, l'application affichera des suggestions détaillées dans les logs. Consultez-les pour plus d'informations.
