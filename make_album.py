def make_album(name_artist, album_artist, kolvo=''):
    person = {'name': name_artist, 'album': album_artist}
    if kolvo:
        person['kolvo'] = kolvo
    return person
    
print("Напишите 'стоп' если хотите выйти.")