import os.path as path
import sys
import logging
import logging.handlers as handlers
import atexit

formatter = logging.Formatter("[%(asctime)s]\t[%(levelname)s]\t[%(message)s]")

log_handler = handlers.TimedRotatingFileHandler(path.join(
    path.expanduser("~"),
    "Documents",
    "basicMusicPlayer",
    "log.txt"
),
    when = 'D',
    backupCount = 5
)
log_handler.setFormatter(formatter)

logger = logging.getLogger("basic_music_player")
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

logging.info("Starting application")
logging.info("Loading additional libraries")

try:
    import kivy
    kivy.require('2.1.0')

    from kivy.app import App
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.image import Image

    logging.info("Successfully imported required packages")

    
except ImportError:
    logger.critical("Could not import all packages. Stacktrace:", exc_info = True)
    sys.exit(1)

except Exception:
    logger.error("Older version of Kivy detected. Exitting", exc_info = True)
    sys.exit(1)


@atexit.register
def exit_script():
    logger.info("Exitting application")
    logging.shutdown()


class PlayerLayout(GridLayout):
    pass


class MusicPlayerApp(App):
    def build(self) -> PlayerLayout:
        return PlayerLayout()