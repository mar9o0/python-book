# Функция для получения минимального числа
def find_min_number(n):
    digits = list(str(n))
    
    digits.sort()
    
    for i in range(len(digits)):
        if digits[i] != '0':
            digits[0], digits[i] = digits[i], digits[0]
            break
    
    return int(''.join(digits))

print(find_min_number(7331))  
print(find_min_number(2017))  