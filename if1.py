def age(a):
    if 3 <= a <= 6:
        return ("Вам нужно ходить в д.сад")
    elif 7 <= a <= 16:
        return ("Вам нужно ходить школу")
    elif 17 <= a <= 23:
        return ("Вам нужно ходить университет")
    elif a < 3:
        return ("Сидите дома")
    if a >= 23:
        return ("Вам нужно работать")   

a = int(input("Введите ваш возраст"))
b = age(a)

print(b)