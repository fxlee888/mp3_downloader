#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube to MP3 Downloader
Application graphique pour télécharger des vidéos YouTube en format MP3
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import threading
import os
from pathlib import Path


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube MP3 Downloader")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # Variables
        self.url_var = tk.StringVar()
        self.destination_var = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.quality_var = tk.StringVar(value="0")
        self.is_downloading = False

        self.setup_ui()

    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configuration du grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # URL Source
        ttk.Label(main_frame, text="URL YouTube:", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        url_entry = ttk.Entry(main_frame, textvariable=self.url_var, width=50)
        url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)

        # Destination
        ttk.Label(main_frame, text="Destination:", font=('Arial', 10, 'bold')).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        dest_entry = ttk.Entry(main_frame, textvariable=self.destination_var, width=40)
        dest_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

        browse_btn = ttk.Button(main_frame, text="Parcourir...", command=self.browse_destination)
        browse_btn.grid(row=1, column=2, sticky=tk.W, pady=5, padx=5)

        # Qualité Audio
        ttk.Label(main_frame, text="Qualité Audio:", font=('Arial', 10, 'bold')).grid(
            row=2, column=0, sticky=tk.W, pady=5
        )

        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5, padx=5)

        quality_combo = ttk.Combobox(
            quality_frame,
            textvariable=self.quality_var,
            values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            state='readonly',
            width=10
        )
        quality_combo.grid(row=0, column=0, sticky=tk.W)

        ttk.Label(quality_frame, text="(0 = Meilleure qualité, 9 = Qualité la plus faible)").grid(
            row=0, column=1, sticky=tk.W, padx=10
        )

        # Bouton de téléchargement
        self.download_btn = ttk.Button(
            main_frame,
            text="Télécharger",
            command=self.start_download,
            style='Accent.TButton'
        )
        self.download_btn.grid(row=3, column=0, columnspan=3, pady=15)

        # Zone de logs
        ttk.Label(main_frame, text="Logs:", font=('Arial', 10, 'bold')).grid(
            row=4, column=0, sticky=tk.W, pady=5
        )

        self.log_text = scrolledtext.ScrolledText(
            main_frame,
            height=15,
            width=70,
            wrap=tk.WORD,
            font=('Consolas', 9)
        )
        self.log_text.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        main_frame.rowconfigure(5, weight=1)

        # Barre de statut
        self.status_label = ttk.Label(
            self.root,
            text="Prêt",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_label.grid(row=1, column=0, sticky=(tk.W, tk.E))

    def browse_destination(self):
        """Ouvre un dialogue pour sélectionner le dossier de destination"""
        folder = filedialog.askdirectory(
            initialdir=self.destination_var.get(),
            title="Sélectionner le dossier de destination"
        )
        if folder:
            self.destination_var.set(folder)
            self.log(f"Dossier de destination: {folder}")

    def log(self, message):
        """Ajoute un message dans la zone de logs"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def update_status(self, message):
        """Met à jour la barre de statut"""
        self.status_label.config(text=message)
        self.root.update_idletasks()

    def validate_inputs(self):
        """Valide les entrées utilisateur"""
        url = self.url_var.get().strip()
        destination = self.destination_var.get().strip()

        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube")
            return False

        if not destination:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier de destination")
            return False

        if not os.path.isdir(destination):
            messagebox.showerror("Erreur", "Le dossier de destination n'existe pas")
            return False

        return True

    def start_download(self):
        """Lance le téléchargement dans un thread séparé"""
        if not self.validate_inputs():
            return

        if self.is_downloading:
            messagebox.showwarning("Attention", "Un téléchargement est déjà en cours")
            return

        # Lance le téléchargement dans un thread pour ne pas bloquer l'interface
        thread = threading.Thread(target=self.download, daemon=True)
        thread.start()

    def download(self):
        """Télécharge la vidéo YouTube en MP3"""
        self.is_downloading = True
        self.download_btn.config(state='disabled')

        url = self.url_var.get().strip()
        destination = self.destination_var.get().strip()
        quality = self.quality_var.get()

        self.log("=" * 70)
        self.log(f"Démarrage du téléchargement...")
        self.log(f"URL: {url}")
        self.log(f"Destination: {destination}")
        self.log(f"Qualité audio: {quality} (0 = meilleure)")
        self.log("=" * 70)
        self.update_status("Téléchargement en cours...")

        # Stratégies de téléchargement à essayer dans l'ordre
        strategies = [
            {
                'name': 'Cookies Firefox + Client Android',
                'args': [
                    '--remote-components', 'ejs:github',
                    '--cookies-from-browser', 'firefox',
                    '--extractor-args', 'youtube:player_client=android',
                    '--no-check-certificates',
                ]
            },
            {
                'name': 'Cookies Firefox + Client Web',
                'args': [
                    '--remote-components', 'ejs:github',
                    '--cookies-from-browser', 'firefox',
                    '--no-check-certificates',
                ]
            },
            {
                'name': 'Sans cookies + Client iOS',
                'args': [
                    '--remote-components', 'ejs:github',
                    '--extractor-args', 'youtube:player_client=ios',
                    '--no-check-certificates',
                    '--user-agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15',
                ]
            },
            {
                'name': 'Mode basique avec composants distants',
                'args': [
                    '--remote-components', 'ejs:github',
                    '--no-check-certificates',
                ]
            }
        ]

        success = False
        for i, strategy in enumerate(strategies, 1):
            if i > 1:
                self.log("\n" + "=" * 70)
                self.log(f"Tentative {i}/{len(strategies)}: {strategy['name']}")
                self.log("=" * 70)
            else:
                self.log(f"Stratégie: {strategy['name']}")
                self.log("=" * 70)

            # Commande yt-dlp de base
            command = [
                'yt-dlp',
                '-x',  # Extract audio
                '--audio-format', 'mp3',
                '--audio-quality', quality,
                '-o', os.path.join(destination, '%(title)s.%(ext)s'),  # Output template
                '--extractor-retries', '3',  # Nombre de tentatives
            ]

            # Ajoute les arguments spécifiques à la stratégie
            command.extend(strategy['args'])
            command.append(url)

            try:
                # Exécute la commande
                process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )

                # Affiche la sortie en temps réel
                for line in process.stdout:
                    self.log(line.strip())

                process.wait()

                if process.returncode == 0:
                    self.log("=" * 70)
                    self.log(f"✓ Téléchargement réussi avec: {strategy['name']}")
                    self.log("=" * 70)
                    self.update_status("Téléchargement réussi")
                    messagebox.showinfo("Succès", f"Le téléchargement est terminé!\n\nStratégie utilisée: {strategy['name']}")
                    success = True
                    break
                else:
                    self.log(f"✗ Échec avec cette stratégie (code: {process.returncode})")

            except FileNotFoundError:
                error_msg = "yt-dlp n'est pas trouvé. Assurez-vous qu'il est installé et dans le PATH."
                self.log(error_msg)
                self.update_status("Erreur: yt-dlp non trouvé")
                messagebox.showerror("Erreur", error_msg)
                break

            except Exception as e:
                self.log(f"✗ Erreur avec cette stratégie: {str(e)}")

        if not success:
            self.log("\n" + "=" * 70)
            self.log("✗ ÉCHEC: Toutes les stratégies ont échoué")
            self.log("=" * 70)
            self.log("\nSuggestions:")
            self.log("1. Vérifiez que yt-dlp est à jour: pip install --upgrade yt-dlp")
            self.log("2. Vérifiez que Node.js est installé")
            self.log("3. Vérifiez votre connexion internet")
            self.log("4. Essayez avec une autre vidéo YouTube")
            self.log("5. La vidéo est peut-être restreinte géographiquement")
            self.update_status("Échec du téléchargement")
            messagebox.showerror("Erreur", "Toutes les stratégies ont échoué.\nConsultez les logs pour plus de détails.")

        self.is_downloading = False
        self.download_btn.config(state='normal')


def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
