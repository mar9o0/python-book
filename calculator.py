#Калькулятор для простых чисел
opinion = input("Вы хотите что-то хотите посчитать? (да/нет): ")

if opinion == "нет":
    print("Всего хорошего!")
else:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

print("Ваше первое число: " + str(num1))
print("Ваше второе число: " + str(num2))

operation = input("Какую операцию вы выберете? (+,-,*,/): ")

if operation == '+':
    print("В результате сложения получилось: " + str(num1 + num2))
elif operation == '-':
    print("В результате вычитания получилось: " + str(num1 - num2))
elif operation == '/':
    print("В результате деления получилось: " + str(num1 / num2))
elif operation == '*':
    print("В результате умножения получилось: " + str(num1 * num2))
else:
    print("Такой операции нет")