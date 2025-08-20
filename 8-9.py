def show_magicians(names):
    """Вывод имени каждого волшебника """
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

magic = ['devid', 'josh', 'pol']
show_magicians(magic)
