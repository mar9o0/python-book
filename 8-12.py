def make_sandw(size, *toppings):
    """Выводит описание пиццы"""
    print("Сделаем пицццу " + str(size) + " размера " + "и со следующими ночинками: ")
    for topping in toppings:
        print("- " + topping.title())

make_sandw('12', 'mashrooms', 'bobo', 'rukala')