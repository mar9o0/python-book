promt = ("\nВведите возраст посетителя и узнайте цену билета: ")
promt += ("\nИли введите 'стоп' для выхода.")

while True:
    age = input(promt)
    
    if age == 'стоп':
        break
    elif int(age) <= 3:
        print("Вход бесплатный!")
    elif 3<= int(age) <=12:
        print("Цена составит 10$!")
    else:
        print("Стоимость билета для взрослых: 15$!")