# Read the playlist.txt file you created and display each song name in uppercase letters using Python.


file = open("playlist.txt", "r")

for song in file:
    print(song.strip().upper())

file.close()