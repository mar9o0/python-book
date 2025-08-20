peoples = input("На сколько человек вам нужен стол? ")
peoples = int(peoples)
if peoples > 8:
    print("\n" + "К сожалению сейчас все места заняты(")
else:
    print("\n" + "Ваш стол будет готов через 30 минут)")