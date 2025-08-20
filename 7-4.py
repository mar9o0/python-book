promt = "\nПожалуйста, введите добавку, которую вы хотите видеть в своей пицце: "
promt += "\n(Напишите 'стоп', если вы не хотите ничего добавлять)."

while True:
    nochinka = input(promt)

    if nochinka == 'стоп':
        break
    else:
        print("Вы добавили начинку: " + nochinka.title() + " в свой заказ!")