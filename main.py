import os.path as path

from kivy.config import Config
Config.read(path.join(
    path.abspath(path.dirname(__file__)),
    "config.ini"
))

from music_player.musicplayer import MusicPlayerApp

if __name__ == "__main__":
    MusicPlayerApp().run()