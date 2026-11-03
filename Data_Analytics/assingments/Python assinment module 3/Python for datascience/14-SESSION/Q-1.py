# Create a text file named playlist.txt and write the names of 5 songs you listened to this week, each on a new line using Python's open() function in write mode.



songs = [
    "Believer",
    "Shape of You",
    "Perfect",
    "Blinding Lights",
    "Heat Waves"
]

file = open("playlist.txt", "w")

for song in songs:
    file.write(song + "\n")

file.close()

print("Songs saved successfully!")