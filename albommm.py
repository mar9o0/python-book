import make_album

while True:
    print("Пожалуйста введите свое имя: ")

    n_artist = input("Имя: ")
    if n_artist == 'стоп':
        break

    a_artist = input("Альбом: ")
    if a_artist == 'стоп':
            break
    
    album = make_album.make_album(n_artist, a_artist)
    print(album)