import logging
import time

from mopidy.exceptions import MpdNotImplemented
from mopidy.models import Playlist

logger = logging.getLogger('backends.base')

class BaseBackend(object):
    current_playlist = None
    library = None
    playback = None
    stored_playlists = None
    uri_handlers = []

class BasePlaybackController(object):
    PAUSED = 'paused'
    PLAYING = 'playing'
    STOPPED = 'stopped'
    
    def __init__(self, backend):
        self.backend = backend
        self.state = self.STOPPED
        self.current_track = None
        self.playlist_position = None

    def play(self, id=None, position=None):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError
