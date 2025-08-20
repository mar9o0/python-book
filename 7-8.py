sandwich_orders = ['с рыбой', 'с мясом', 'овощной', 'с соусом']
finished_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("Готовые сэндвичи: " + sandwich.title())
    finished_orders.append(sandwich)

print("\nВсе готовые бутерброды:")
for finished_order in finished_orders:
    print(finished_order.title())