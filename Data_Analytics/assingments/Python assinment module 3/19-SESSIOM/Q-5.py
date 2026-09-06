# Refactor your Song class so that the duration attribute is optional in the constructor (default to 0 if not provided).<br><br><em><strong>Hint:</strong> Use a default argument for duration in the __init__() method.</em>



class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)


song1 = Song("Believer", "Imagine Dragons", 204)
song2 = Song("Perfect", "Ed Sheeran")

print(song1.title, song1.duration)
print(song2.title, song2.duration)