"""
1. LLD Scope (What we’re designing)
    In scope (LLD):
        - Play / Pause / Next / Previous
        - User, Playlist, Song
        - Queue management
        - Multiple playback modes (Shuffle, Repeat)
        - Observers (UI updates, notifications)
        - Search & recommendation NOT required at LLD

    Out of scope (HLD):
        - Streaming infra
        - CDN
        - Licensing
        - ML recommendations

2. Core Design Principles
    - SOLID
    - Open-Closed Principle (easy to add new playback modes)
    - Loose coupling
    - Composition over inheritance

    
3. High-Level Class Diagram (Mental Model)
User
 └── MusicPlayer
       ├── PlaybackController
       ├── QueueManager
       ├── PlaybackStrategy
       └── List<Observer>

Playlist
 └── List<Song>

Song
"""

# Song Entity (Basic Model)
class Song:
    """
    Represents a song in the system
    """
    def __init__(self, song_id: str, title: str, artist: str, duration: int):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds

    def __str__(self):
        return f"{self.title} - {self.artist}"


# Strategy Pattern — Audio Source
from abc import ABC, abstractmethod

class AudioSource(ABC):
    """
    Strategy interface for different audio sources
    """

    @abstractmethod
    def play(self, song: Song):
        pass

# Local Audio Source
class LocalAudioSource(AudioSource):
    """
    Plays music stored locally
    """
    def play(self, song: Song):
        print(f"🎧 Playing locally: {song}")


# Streaming Audio Source
class StreamingAudioSource(AudioSource):
    """
    Plays music via streaming
    """
    def play(self, song: Song):
        print(f"📡 Streaming: {song}")


# State Pattern — Player State
class PlayerState(ABC):
    """
    State interface defining player actions
    """

    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass


# Playing State
class PlayingState(PlayerState):
    """
    Represents the Playing state
    """

    def play(self, player):
        print("▶️ Already playing")

    def pause(self, player):
        print("⏸️ Music paused")
        player.set_state(PausedState())


# Paused State
class PausedState(PlayerState):
    """
    Represents the Paused state
    """

    def play(self, player):
        print("▶️ Resuming music")
        player.set_state(PlayingState())

    def pause(self, player):
        print("⏸️ Already paused")


# Iterator Pattern — Playlist
class Playlist:
    """
    Represents a playlist of songs
    """

    def __init__(self, name: str):
        self.name = name
        self.songs = []
        self.current_index = 0

    def add_song(self, song: Song):
        self.songs.append(song)

    def next_song(self):
        """
        Returns the next song in the playlist
        """
        if self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            return song
        return None

    def reset(self):
        """
        Resets playlist to the beginning
        """
        self.current_index = 0



# Singleton + Facade — Music Player
class MusicPlayer:
    """
    Main music player class
    Implements:
    - Singleton Pattern
    - Facade Pattern
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MusicPlayer, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initial state is paused
        self.state = PausedState()

        # Default audio source
        self.audio_source = StreamingAudioSource()

        self.current_song = None
        self.playlist = None

    # ---------- State Handling ----------
    def set_state(self, state: PlayerState):
        self.state = state

    # ---------- Strategy Handling ----------
    def set_audio_source(self, source: AudioSource):
        self.audio_source = source

    # ---------- Playlist Handling ----------
    def load_playlist(self, playlist: Playlist):
        self.playlist = playlist
        self.playlist.reset()

    # ---------- Player Controls ----------
    def play(self):
        if not self.current_song and self.playlist:
            self.current_song = self.playlist.next_song()

        if self.current_song:
            self.audio_source.play(self.current_song)
            self.state.play(self)
        else:
            print("❌ No song to play")

    def pause(self):
        self.state.pause(self)

    def next(self):
        if self.playlist:
            self.current_song = self.playlist.next_song()
            if self.current_song:
                self.audio_source.play(self.current_song)
            else:
                print("📭 End of playlist")


# Client Code (Execution Flow)
if __name__ == "__main__":

    # Create songs
    song1 = Song("1", "Believer", "Imagine Dragons", 210)
    song2 = Song("2", "Shape of You", "Ed Sheeran", 240)
    song3 = Song("3", "Blinding Lights", "The Weeknd", 200)

    # Create playlist
    playlist = Playlist("My Favorites")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    # Get singleton music player
    player = MusicPlayer()

    # Load playlist
    player.load_playlist(playlist)

    # Play controls
    player.play()
    player.pause()
    player.play()
    player.next()
    player.next()
    player.next()
