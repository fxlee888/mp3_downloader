#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube to MP3 Downloader - Version avec fichier cookies
Application graphique pour télécharger des vidéos YouTube en format MP3
Cette version utilise un fichier cookies.txt exporté du navigateur
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
        self.root.title("YouTube MP3 Downloader (avec fichier cookies)")
        self.root.geometry("700x550")
        self.root.resizable(True, True)

        # Variables
        self.url_var = tk.StringVar()
        self.destination_var = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.quality_var = tk.StringVar(value="0")
        self.cookies_file_var = tk.StringVar(value=str(Path(__file__).parent / "youtube_cookies.txt"))
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

        browse_dest_btn = ttk.Button(main_frame, text="Parcourir...", command=self.browse_destination)
        browse_dest_btn.grid(row=1, column=2, sticky=tk.W, pady=5, padx=5)

        # Fichier cookies
        ttk.Label(main_frame, text="Fichier Cookies:", font=('Arial', 10, 'bold')).grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        cookies_entry = ttk.Entry(main_frame, textvariable=self.cookies_file_var, width=40)
        cookies_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

        browse_cookies_btn = ttk.Button(main_frame, text="Parcourir...", command=self.browse_cookies)
        browse_cookies_btn.grid(row=2, column=2, sticky=tk.W, pady=5, padx=5)

        # Qualité Audio
        ttk.Label(main_frame, text="Qualité Audio:", font=('Arial', 10, 'bold')).grid(
            row=3, column=0, sticky=tk.W, pady=5
        )

        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=5, padx=5)

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
        self.download_btn.grid(row=4, column=0, columnspan=3, pady=15)

        # Info sur les cookies
        info_frame = ttk.Frame(main_frame)
        info_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        info_text = "💡 Pour exporter les cookies, consultez EXPORT_COOKIES_GUIDE.md"
        ttk.Label(info_frame, text=info_text, foreground="blue", font=('Arial', 9)).pack()

        # Zone de logs
        ttk.Label(main_frame, text="Logs:", font=('Arial', 10, 'bold')).grid(
            row=6, column=0, sticky=tk.W, pady=5
        )

        self.log_text = scrolledtext.ScrolledText(
            main_frame,
            height=12,
            width=70,
            wrap=tk.WORD,
            font=('Consolas', 9)
        )
        self.log_text.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        main_frame.rowconfigure(7, weight=1)

        # Barre de statut
        self.status_label = ttk.Label(
            self.root,
            text="Prêt - Utilise un fichier cookies exporté",
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

    def browse_cookies(self):
        """Ouvre un dialogue pour sélectionner le fichier cookies"""
        file = filedialog.askopenfilename(
            initialdir=Path(__file__).parent,
            title="Sélectionner le fichier cookies.txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file:
            self.cookies_file_var.set(file)
            self.log(f"Fichier cookies: {file}")

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
        cookies_file = self.cookies_file_var.get().strip()

        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube")
            return False

        if not destination:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier de destination")
            return False

        if not os.path.isdir(destination):
            messagebox.showerror("Erreur", "Le dossier de destination n'existe pas")
            return False

        if not cookies_file:
            result = messagebox.askyesno(
                "Attention",
                "Aucun fichier cookies spécifié.\n\n"
                "YouTube demande maintenant des cookies pour télécharger.\n"
                "Voulez-vous continuer sans cookies (peut échouer) ?"
            )
            if not result:
                return False
        elif not os.path.isfile(cookies_file):
            messagebox.showerror(
                "Erreur",
                f"Le fichier cookies n'existe pas:\n{cookies_file}\n\n"
                "Consultez EXPORT_COOKIES_GUIDE.md pour exporter vos cookies."
            )
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
        cookies_file = self.cookies_file_var.get().strip()

        self.log("=" * 70)
        self.log(f"Démarrage du téléchargement avec fichier cookies...")
        self.log(f"URL: {url}")
        self.log(f"Destination: {destination}")
        self.log(f"Qualité audio: {quality} (0 = meilleure)")
        self.log(f"Fichier cookies: {cookies_file if cookies_file else 'Aucun'}")
        self.log("=" * 70)
        self.update_status("Téléchargement en cours...")

        # Commande yt-dlp avec fichier cookies
        command = [
            'yt-dlp',
            '-f', 'bestaudio',  # Meilleur audio disponible
            '--extract-audio',  # Extrait l'audio
            '--audio-format', 'mp3',
            '--audio-quality', quality,
            '-o', os.path.join(destination, '%(title)s.%(ext)s'),  # Output template
        ]

        # Ajoute le fichier cookies s'il existe
        if cookies_file and os.path.isfile(cookies_file):
            command.extend(['--cookies', cookies_file])
            # N'utilise PAS player_client=ios avec les cookies (incompatible)
            command.extend(['--extractor-args', 'youtube:player_skip=webpage'])
        else:
            # Sans cookies, utilise le client iOS
            command.extend(['--extractor-args', 'youtube:player_client=ios'])
            command.extend(['--no-check-certificates'])

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
                self.log("Téléchargement terminé avec succès!")
                self.log("=" * 70)
                self.update_status("Téléchargement réussi")
                messagebox.showinfo("Succès", "Le téléchargement est terminé!")
            else:
                self.log("=" * 70)
                self.log(f"Erreur lors du téléchargement (code: {process.returncode})")
                self.log("=" * 70)

                if not cookies_file or not os.path.isfile(cookies_file):
                    self.log("\n💡 CONSEIL: Exportez vos cookies YouTube et réessayez.")
                    self.log("   Consultez EXPORT_COOKIES_GUIDE.md pour les instructions.")

                self.update_status("Erreur lors du téléchargement")
                messagebox.showerror("Erreur", "Le téléchargement a échoué. Vérifiez les logs.")

        except FileNotFoundError:
            error_msg = "yt-dlp n'est pas trouvé. Assurez-vous qu'il est installé et dans le PATH."
            self.log(error_msg)
            self.update_status("Erreur: yt-dlp non trouvé")
            messagebox.showerror("Erreur", error_msg)

        except Exception as e:
            error_msg = f"Erreur inattendue: {str(e)}"
            self.log(error_msg)
            self.update_status("Erreur")
            messagebox.showerror("Erreur", error_msg)

        finally:
            self.is_downloading = False
            self.download_btn.config(state='normal')


def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
