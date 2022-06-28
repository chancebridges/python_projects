def make_album(artist_name, album_title, tracks = ''):
    """Return a dictionary with the album information."""
    album = {'name' : artist_name, 'album' : album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("Please enter below an album's artist and title.")
    print("Enter 'q' at any time to quit.")
    artist = input('artist: ')
    if artist == 'q':
        break
    album = input('album: ')
    if album == 'q':
        break

    user_album = make_album(artist, album)
    print(user_album)