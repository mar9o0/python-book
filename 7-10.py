responses = {}

polling_activ = True

while polling_activ:
    name = input("\nКак тебя зовут?")
    response = input("\nГде бы ты хотел провести отпуск?")

    responses[name] = response

    repeat = input("\nТы хотел бы записать еще мнение? (да/нет)")
    if repeat == 'нет':
        polling_activ = False

print("\n\tРезультаты опроса:")
for name, response in responses.items():
    print(name + " предпочитает " + response + ".")
