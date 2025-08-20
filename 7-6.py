promt = "\nПожалуйста, введите добавку, которую вы хотите видеть в своей пицце: "
promt += "\n(Напишите 'стоп', если вы не хотите ничего добавлять)."

activ = True
while activ:
    nochinka = input(promt)

    if nochinka == 'стоп':
        activ = False
        break
    else:
        print("Вы добавили начинку: " + nochinka.title() + " в свой заказ!")