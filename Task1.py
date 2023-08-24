def triagle (a, b, c):
    if (a + b < c or a + c < b or b + c < a):
       return 'Треугольника c такими сторонами не существует!'   

    if (a == b and b == c and c == a):
        return 'Треугольник равносторонний.'
    elif a != b and b != c:
        return 'Треугольник разносторонний.'  
    else:
        return 'Треугольник равнобедренный.'  


print(triagle(4, 4, 4))
print(triagle(4, 5, 6))
print(triagle(4, 4, 8))
print(triagle(4, 4, 12))