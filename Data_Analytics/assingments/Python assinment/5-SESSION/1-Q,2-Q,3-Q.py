# Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.


playlist_ids = ['Blinding Lights','Believer','Lose Yourself','Counting Stars','A Sky Full of Stars']
print (playlist_ids)

# Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.Use append() for a single ID and extend() for adding multiple IDs at once.


res = playlist_ids.append('Unstoppable')
print(playlist_ids)

ras = playlist_ids.extend(['high','alan tuff'])
print(playlist_ids)

ris = playlist_ids.pop(7)
print(playlist_ids)