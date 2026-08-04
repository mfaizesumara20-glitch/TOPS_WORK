# def get_unique_artists(spotify_playlist1, spotify_playlist2):

#     unique_artists = spotify_playlist1.union(spotify_playlist2)

#     return unique_artists


# playlist1 = {'Taylor Swift', 'Ed Sheeran', 'Adele', 'Drake'}
# playlist2 = {'Adele', 'Beyoncé', 'Drake', 'Bruno Mars'}
# print('unique artists in both playlists : ', get_unique_artists(playlist1, playlist2))



a=int(input("Enter a Numbers : "))
b=int(input("Enter b Numbers : "))
if a>b:
  if a!=0 and b!=0:
    print("a is greater than b and both are positive numbers")
else: 
  print('a is less than b')