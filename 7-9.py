input("В нашем меню больше нет сэндвичей с рыбой( Приносим свои извинения!")

sandwich_orders = ['с рыбой', 'с мясом', 'с рыбой', 'овощной', 'с соусом', 'с рыбой',]
finished_orders = []

while 'с рыбой' in sandwich_orders:
    sandwich_orders.remove('с рыбой')

    print(sandwich_orders)