# Define a Python class called Song with attributes title, artist, and duration (in seconds). Create an object for your favorite song and print its details.



class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song("Believer", "Imagine Dragons", 204)

print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")