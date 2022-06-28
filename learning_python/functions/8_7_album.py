def make_album(artist_name, album_title, tracks = ''):
    """Return a dictionary with the album information."""
    album = {'name' : artist_name, 'album' : album_title}
    if tracks:
        album['tracks'] = tracks
    return album

nickelback = make_album('NIckelback', 'Feed the machine', '11')
dave_matthews = make_album('Dave Matthews', 'Crash')
blue_october = make_album(album_title='foiled', artist_name='Justin Furstenfield')

print(nickelback)
print(dave_matthews)
print(blue_october)