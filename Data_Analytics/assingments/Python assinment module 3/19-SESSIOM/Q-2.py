# Add a method play_preview(self) to the Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method using the object you created.


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)


song1 = Song("Believer", "Imagine Dragons", 204)

print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

song1.play_preview()