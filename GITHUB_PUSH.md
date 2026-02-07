# Instructions pour pousser vers GitHub

Le repository Git local est prêt avec tous les fichiers commités.

## Option 1 : Avec GitHub CLI (Recommandé)

### Installer GitHub CLI

**Windows** :
```bash
# Avec winget
winget install --id GitHub.cli

# Ou avec chocolatey
choco install gh

# Ou téléchargez depuis
# https://cli.github.com/
```

### Utiliser GitHub CLI

```bash
# Se connecter à GitHub
gh auth login

# Créer le repo et pousser
cd "D:\Documents\FX\PROJECTS\mp3_downloader"
gh repo create mp3_downloader --public --source=. --remote=origin --push
```

## Option 2 : Manuellement (sans installer gh)

### Étape 1 : Créer le repo sur GitHub

1. Allez sur https://github.com/new
2. **Repository name** : `mp3_downloader`
3. **Description** : `YouTube MP3 Downloader - Application Python avec interface graphique`
4. **Visibilité** : Public ou Private (votre choix)
5. **NE COCHEZ PAS** "Initialize with README" (on a déjà un README)
6. Cliquez sur **Create repository**

### Étape 2 : Pousser le code

Après avoir créé le repo, GitHub vous montrera des instructions. Utilisez celles pour "push an existing repository" :

```bash
cd "D:\Documents\FX\PROJECTS\mp3_downloader"
git remote add origin https://github.com/fxlee888/mp3_downloader.git
git branch -M main
git push -u origin main
```

**OU avec SSH** (si vous avez configuré une clé SSH) :

```bash
cd "D:\Documents\FX\PROJECTS\mp3_downloader"
git remote add origin git@github.com:fxlee888/mp3_downloader.git
git branch -M main
git push -u origin main
```

## Vérification

Après le push, visitez :
```
https://github.com/fxlee888/mp3_downloader
```

Vous devriez voir tous vos fichiers, y compris le README qui s'affiche automatiquement.

## Prochaines fois

Pour les futurs commits :

```bash
git add .
git commit -m "Votre message de commit"
git push
```

## Troubleshooting

### Authentification requise

Si Git demande vos identifiants :
- **Username** : fxlee888
- **Password** : Utilisez un Personal Access Token (pas votre mot de passe)

Pour créer un token :
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → Cochez "repo"
3. Copiez le token et utilisez-le comme mot de passe

### Erreur "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/fxlee888/mp3_downloader.git
```

## État actuel du repository local

✓ Repository Git initialisé
✓ Tous les fichiers ajoutés
✓ 2 commits créés
✓ Branch : master
✓ Prêt à pousser vers GitHub

## Fichiers dans le repo

- youtube_downloader.py (application principale)
- create_icon.py (générateur d'icône)
- app_icon.ico (icône)
- build_exe.bat (script de build)
- requirements.txt
- README.md
- claude.md (documentation complète)
- BUILD_INSTRUCTIONS.md
- CUSTOM_ICON.md
- .gitignore

**Note** : Les dossiers `build/`, `dist/` et les fichiers `.spec` sont ignorés (.gitignore)
