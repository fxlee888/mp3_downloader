#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube to MP3 Batch Downloader (CLI)
Telecharge une liste d'URLs YouTube en MP3 vers un dossier de destination.
Reutilise le systeme multi-strategies de youtube_downloader.py.
"""

import argparse
import os
import subprocess
import sys

from download_strategies import STRATEGIES


def download_one(url, destination, quality):
    print("=" * 70)
    print(f"URL: {url}")
    print("=" * 70)

    for i, strategy in enumerate(STRATEGIES, 1):
        print(f"\nTentative {i}/{len(STRATEGIES)}: {strategy['name']}")
        print("-" * 70)

        command = [
            'yt-dlp',
            '-x',
            '--no-playlist',
            '--audio-format', 'mp3',
            '--audio-quality', quality,
            '-o', os.path.join(destination, '%(title)s.%(ext)s'),
            '--extractor-retries', '3',
        ]
        command.extend(strategy['args'])
        command.append(url)

        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
            )
            for line in process.stdout:
                print(line.rstrip())
            process.wait()

            if process.returncode == 0:
                print(f"\n[OK] Reussi avec: {strategy['name']}")
                return True
            else:
                print(f"\n[ECHEC] code retour: {process.returncode}")

        except FileNotFoundError:
            print("[ERREUR] yt-dlp n'est pas trouve. Verifiez qu'il est installe et dans le PATH.")
            return False

    print(f"\n[ECHEC TOTAL] Toutes les strategies ont echoue pour: {url}")
    return False


def main():
    parser = argparse.ArgumentParser(description="Telecharge une liste d'URLs YouTube en MP3")
    parser.add_argument('urls', nargs='*', help="URLs YouTube a telecharger")
    parser.add_argument('-f', '--file', help="Fichier texte contenant une URL par ligne")
    parser.add_argument('-d', '--destination', required=True, help="Dossier de destination")
    parser.add_argument('-q', '--quality', default='0', choices=[str(n) for n in range(10)],
                         help="Qualite audio 0 (meilleure) a 9 (pire), defaut: 0")
    args = parser.parse_args()

    urls = list(args.urls)
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            urls.extend(line.strip() for line in f if line.strip() and not line.strip().startswith('#'))

    if not urls:
        print("Erreur: aucune URL fournie (via arguments ou --file)")
        sys.exit(1)

    destination = os.path.abspath(args.destination)
    os.makedirs(destination, exist_ok=True)

    print(f"Destination: {destination}")
    print(f"Qualite audio: {args.quality}")
    print(f"Nombre d'URLs: {len(urls)}")

    results = []
    for url in urls:
        ok = download_one(url, destination, args.quality)
        results.append((url, ok))
        print()

    print("=" * 70)
    print("RESUME")
    print("=" * 70)
    success_count = sum(1 for _, ok in results if ok)
    for url, ok in results:
        status = "OK" if ok else "ECHEC"
        print(f"[{status}] {url}")
    print(f"\n{success_count}/{len(results)} telechargements reussis")

    sys.exit(0 if success_count == len(results) else 1)


if __name__ == "__main__":
    main()
