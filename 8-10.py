def show_magicians(names):
    """Вывод имени каждого волшебника """
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)
magic = ['devid', 'josh', 'pol']

def make_great(magicians):
    for i in range(len(magicians)):     # range(len(magicians)) - создает последовательность индексов
        magicians[i] = 'Great ' + magicians[i]

make_great(magic)
show_magicians(magic)