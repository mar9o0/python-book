def make_album(name_artist, album_artist, kolvo=''):
    person = {'name': name_artist, 'album': album_artist}
    if kolvo:
        person['kolvo'] = kolvo
    return person
    
print("Напишите 'стоп' если хотите выйти.")

while True:
    print("Пожалуйста введите свое имя: ")

    n_artist = input("Имя: ")
    if n_artist == 'стоп':
        break

    a_artist = input("Альбом: ")
    if a_artist == 'стоп':
            break
    
    album = make_album(n_artist, a_artist)
    print(album)
