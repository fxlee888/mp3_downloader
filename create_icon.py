#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour créer une icône simple pour l'application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Crée une icône avec un symbole de note de musique"""

    # Tailles standard pour les icônes Windows
    sizes = [256, 128, 64, 48, 32, 16]
    images = []

    for size in sizes:
        # Créer une image avec fond dégradé
        img = Image.new('RGB', (size, size), color='#1DB954')  # Vert Spotify-like
        draw = ImageDraw.Draw(img)

        # Dessiner un cercle de fond
        margin = size // 10
        draw.ellipse([margin, margin, size-margin, size-margin],
                     fill='#1DB954', outline='#FFFFFF', width=max(2, size//64))

        # Dessiner une note de musique simplifiée
        center_x = size // 2
        center_y = size // 2

        # Taille de la note proportionnelle
        note_size = size // 4

        # Cercle de la note (bas)
        note_circle_y = center_y + note_size // 2
        draw.ellipse([center_x - note_size//3, note_circle_y - note_size//3,
                     center_x + note_size//3, note_circle_y + note_size//3],
                     fill='#FFFFFF')

        # Tige de la note
        stem_width = max(2, size // 32)
        stem_height = note_size * 2
        draw.rectangle([center_x + note_size//4, note_circle_y - stem_height,
                       center_x + note_size//4 + stem_width, note_circle_y],
                      fill='#FFFFFF')

        # Petit trait en haut de la tige
        draw.rectangle([center_x + note_size//4, note_circle_y - stem_height,
                       center_x + note_size//4 + note_size//2,
                       note_circle_y - stem_height + stem_width],
                      fill='#FFFFFF')

        images.append(img)

    # Sauvegarder comme fichier .ico
    output_path = 'app_icon.ico'
    images[0].save(output_path, format='ICO', sizes=[(img.width, img.height) for img in images])

    print(f"Icône créée : {output_path}")
    print(f"Tailles incluses : {sizes}")

    return output_path

if __name__ == "__main__":
    try:
        icon_path = create_icon()
        print(f"\nSuccès ! L'icône a été créée : {icon_path}")
        print("\nVous pouvez maintenant reconstruire l'executable avec la nouvelle icône.")
    except ImportError:
        print("ERREUR : Le module 'Pillow' n'est pas installé.")
        print("\nPour l'installer, exécutez :")
        print("    pip install Pillow")
        print("\nOu téléchargez une icône .ico depuis internet et placez-la dans le dossier du projet.")
    except Exception as e:
        print(f"Erreur : {e}")
