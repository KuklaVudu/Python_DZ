def prime_number(): 
    if number < 0 or number > 100000:
        return 'Ошибка. Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'
    
    if number == 1 or number == 0:
        return 'Это не простое и не составное число'  
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'Число является составным'
    return 'Число является простым'
              

number = -1
print(prime_number())