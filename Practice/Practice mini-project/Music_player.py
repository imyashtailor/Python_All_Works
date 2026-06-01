import os
import random
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

import pygame
from mutagen import File as MutagenFile
from mutagen.id3 import ID3
from PIL import Image, ImageTk

# ----------------------------
# Initialize pygame mixer
# ----------------------------
pygame.mixer.init()


class MusicPlayer:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Music Player")
        self.root.geometry("950x650")
        self.root.configure(bg="#1e1e1e")

        self.playlist = []
        self.current_index = -1

        self.paused = False
        self.repeat = False
        self.shuffle = False

        self.song_length = 0
        self.dragging_slider = False

        self.setup_style()
        self.build_ui()

        self.update_progress()

    # ----------------------------
    # Dark Theme
    # ----------------------------
    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Horizontal.TScale",
            background="#252526"
        )

    # ----------------------------
    # UI
    # ----------------------------
    def build_ui(self):

        title = tk.Label(
            self.root,
            text="🎵 Advanced Music Player",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=10)

        main = tk.Frame(
            self.root,
            bg="#1e1e1e"
        )
        main.pack(fill="both", expand=True)

        # LEFT PANEL
        left = tk.Frame(
            main,
            bg="#252526"
        )
        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # RIGHT PANEL
        right = tk.Frame(
            main,
            bg="#252526",
            width=280
        )
        right.pack(
            side="right",
            fill="y",
            padx=10,
            pady=10
        )

        # Playlist
        self.playlist_box = tk.Listbox(
            left,
            bg="#2d2d30",
            fg="white",
            selectbackground="#007acc",
            font=("Segoe UI", 11)
        )

        self.playlist_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.playlist_box.bind(
            "<Double-Button-1>",
            self.play_selected_song
        )

        # Song Label
        self.song_label = tk.Label(
            left,
            text="No song selected",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12)
        )

        self.song_label.pack(pady=5)

        # Progress Bar
        self.progress_var = tk.DoubleVar()

        self.progress_scale = ttk.Scale(
            left,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.progress_var
        )

        self.progress_scale.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.progress_scale.bind(
            "<ButtonRelease-1>",
            self.seek_song
        )

        # Time
        self.time_label = tk.Label(
            left,
            text="00:00 / 00:00",
            bg="#252526",
            fg="lightgray"
        )

        self.time_label.pack()

        # Controls
        controls = tk.Frame(
            left,
            bg="#252526"
        )
        controls.pack(pady=15)

        button_style = {
            "bg": "#3c3c3c",
            "fg": "white",
            "font": ("Segoe UI", 10),
            "width": 10
        }

        tk.Button(
            controls,
            text="Add Songs",
            command=self.add_songs,
            **button_style
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            controls,
            text="Play",
            command=self.play_song,
            **button_style
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            controls,
            text="Pause",
            command=self.pause_song,
            **button_style
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            controls,
            text="Stop",
            command=self.stop_song,
            **button_style
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            controls,
            text="Previous",
            command=self.previous_song,
            **button_style
        ).grid(row=1, column=0, pady=10)

        tk.Button(
            controls,
            text="Next",
            command=self.next_song,
            **button_style
        ).grid(row=1, column=1, pady=10)

        self.shuffle_btn = tk.Button(
            controls,
            text="Shuffle OFF",
            command=self.toggle_shuffle,
            **button_style
        )
        self.shuffle_btn.grid(row=1, column=2)

        self.repeat_btn = tk.Button(
            controls,
            text="Repeat OFF",
            command=self.toggle_repeat,
            **button_style
        )
        self.repeat_btn.grid(row=1, column=3)

        # Volume
        volume_frame = tk.Frame(
            left,
            bg="#252526"
        )

        volume_frame.pack(pady=10)

        tk.Label(
            volume_frame,
            text="Volume",
            bg="#252526",
            fg="white"
        ).pack()

        self.volume_slider = ttk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient="horizontal",
            command=self.change_volume
        )

        self.volume_slider.set(70)
        self.volume_slider.pack()

        pygame.mixer.music.set_volume(0.7)

        # Album Art
        self.album_art_label = tk.Label(
            right,
            bg="#252526"
        )

        self.album_art_label.pack(
            pady=20
        )

        self.default_album_art()

        self.info_label = tk.Label(
            right,
            text="Album Art",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12)
        )

        self.info_label.pack()

    # ----------------------------
    # Playlist
    # ----------------------------
    def add_songs(self):

        files = filedialog.askopenfilenames(
            filetypes=[
                (
                    "Audio Files",
                    "*.mp3 *.wav *.ogg *.flac *.m4a"
                )
            ]
        )

        for file in files:
            self.playlist.append(file)

            self.playlist_box.insert(
                tk.END,
                os.path.basename(file)
            )

    def play_selected_song(self, event=None):

        selection = self.playlist_box.curselection()

        if selection:
            self.current_index = selection[0]
            self.load_song()

    # ----------------------------
    # Playback
    # ----------------------------
    def play_song(self):

        if not self.playlist:
            messagebox.showwarning(
                "Warning",
                "No songs added."
            )
            return

        if self.current_index == -1:
            self.current_index = 0

        self.load_song()

    def load_song(self):

        song = self.playlist[self.current_index]

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        self.song_label.config(
            text=os.path.basename(song)
        )

        self.paused = False

        self.load_song_info(song)
        self.load_album_art(song)

        self.playlist_box.selection_clear(
            0,
            tk.END
        )

        self.playlist_box.selection_set(
            self.current_index
        )

    def pause_song(self):

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):

        if not self.playlist:
            return

        if self.shuffle:
            self.current_index = random.randint(
                0,
                len(self.playlist) - 1
            )
        else:
            self.current_index += 1

            if self.current_index >= len(self.playlist):
                self.current_index = 0

        self.load_song()

    def previous_song(self):

        if not self.playlist:
            return

        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1

        self.load_song()

    # ----------------------------
    # Modes
    # ----------------------------
    def toggle_shuffle(self):

        self.shuffle = not self.shuffle

        self.shuffle_btn.config(
            text=f"Shuffle {'ON' if self.shuffle else 'OFF'}"
        )

    def toggle_repeat(self):

        self.repeat = not self.repeat

        self.repeat_btn.config(
            text=f"Repeat {'ON' if self.repeat else 'OFF'}"
        )

    # ----------------------------
    # Volume
    # ----------------------------
    def change_volume(self, value):
        pygame.mixer.music.set_volume(
            float(value) / 100
        )

    # ----------------------------
    # Song Info
    # ----------------------------
    def load_song_info(self, path):

        try:
            audio = MutagenFile(path)

            if audio and hasattr(audio, "info"):
                self.song_length = audio.info.length
            else:
                self.song_length = 0

        except Exception:
            self.song_length = 0

    # ----------------------------
    # Album Art
    # ----------------------------
    def default_album_art(self):

        img = Image.new(
            "RGB",
            (250, 250),
            (70, 70, 70)
        )

        self.album_image = ImageTk.PhotoImage(img)

        self.album_art_label.config(
            image=self.album_image
        )

    def load_album_art(self, path):

        try:

            if not path.lower().endswith(".mp3"):
                self.default_album_art()
                return

            tags = ID3(path)

            for tag in tags.values():

                if tag.FrameID == "APIC":

                    from io import BytesIO

                    image_data = tag.data

                    image = Image.open(
                        BytesIO(image_data)
                    )

                    image = image.resize(
                        (250, 250)
                    )

                    self.album_image = (
                        ImageTk.PhotoImage(image)
                    )

                    self.album_art_label.config(
                        image=self.album_image
                    )

                    return

            self.default_album_art()

        except Exception:
            self.default_album_art()

    # ----------------------------
    # Progress
    # ----------------------------
    def update_progress(self):

        try:

            if pygame.mixer.music.get_busy():

                current_pos = (
                    pygame.mixer.music.get_pos()
                    / 1000
                )

                if self.song_length > 0:

                    percentage = (
                        current_pos
                        / self.song_length
                    ) * 100

                    self.progress_var.set(
                        percentage
                    )

                    current = self.format_time(
                        current_pos
                    )

                    total = self.format_time(
                        self.song_length
                    )

                    self.time_label.config(
                        text=f"{current} / {total}"
                    )

            else:

                if (
                    not self.paused
                    and self.current_index != -1
                ):

                    if self.repeat:
                        self.load_song()
                    else:
                        self.next_song()

        except Exception:
            pass

        self.root.after(
            1000,
            self.update_progress
        )

    def seek_song(self, event):

        if self.song_length <= 0:
            return

        position = (
            self.progress_var.get()
            / 100
        ) * self.song_length

        try:
            song = self.playlist[
                self.current_index
            ]

            pygame.mixer.music.load(song)
            pygame.mixer.music.play(
                start=position
            )

        except Exception:
            pass

    # ----------------------------
    # Utils
    # ----------------------------
    def format_time(self, seconds):

        mins = int(seconds // 60)
        secs = int(seconds % 60)

        return f"{mins:02}:{secs:02}"


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":

    root = tk.Tk()

    app = MusicPlayer(root)

    root.mainloop()