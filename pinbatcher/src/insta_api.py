# import subprocess
import os
import tkinter as tk
from PIL import Image, ImageTk
from rich.console import Console
from time import sleep
from rich.progress import track


def download_profile(username):
    print(f"Downloading {username}...")
    args = ["--no-videos",
            "--no-video-thumbnails",
            "--no-captions",
            "--no-metadata-json",
            "--no-compress-json",
            "--post-filter=\"not is_video\"",
            "--fast-update",
            # "--login \"scrapyyybt\"",
            # "--password \"Test458\""
            ]
    command = "instaloader"
    for arg in args:
        command += " " + arg
    command += f" profile {username}"
    os.system(command)

    for file in os.listdir(f"./{username}"):
        if not file.endswith(('jpg', 'jpeg')):
            os.remove(f"./{username}/{file}")
            # print(f"Deleted {file}")


def action(fenetre, fichier, decision):
    if decision == 'supprimer':
        os.remove(fichier)
        print(f"Fichier {fichier} supprimé.")
    fenetre.destroy()


def sort_pictures(username):
    dossier = f"./{username}"

    for fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, fichier)
        img = Image.open(chemin_complet)
        img.thumbnail((1000, 1000))

        fenetre = tk.Tk()
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(fenetre, image=photo)
        label.pack()

        # Boutons pour garder ou supprimer l'image
        btn_garder = tk.Button(fenetre, text="Garder", command=lambda: action(
            fenetre, chemin_complet, 'garder'))
        btn_garder.pack(side=tk.LEFT)

        btn_supprimer = tk.Button(fenetre, text="Supprimer", command=lambda: action(
            fenetre, chemin_complet, 'supprimer'))
        btn_supprimer.pack(side=tk.RIGHT)

        fenetre.mainloop()

    print("Done")


def rename_files(usernames):
    for username in usernames:
        path = f"./influs/{username}"
        for file in track(os.listdir(path), description=f"Renaming {username}..."):
            if os.path.isfile(os.path.join(path, file)):
                if "." in username:
                    username = username.replace(".", "_p_")
                new_name = f"{username}__at__{file}"
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, new_name)
                os.rename(old_path, new_path)


usernames = [
    # "spikeloveyoko",
    #  "cjay1k",
    #  "alessoyoko",
    #  "luke.akoto",
    #  "onemullz",
    #  "verenamtza",
    #  "javelberlin",
    #  "shai",
    #  "joshiiks",
    #  "iziboy224",
    #  "rymndla",
    #  "khristianity_",
    #  "stezinbelize",
    #  "ny_ocho",
    # "romerosego",
    # "iconikki",
    # "kshitij.bhatia",
    # "marianthe.z",
    # "__clayv",
]
console = Console()

# for username in usernames:
#     download_profile(username)
#     sleep(1)
#     console.log(f"{username} completed")
