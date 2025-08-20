def make_album(name_artist, album_artist, kolvo=''):
    person = {'name': name_artist, 'album': album_artist}
    if kolvo:
        person['kolvo'] = kolvo
    return person

artist = make_album('rfikrj', 'vmkrvmkjrv', kolvo=17)
print(artist)