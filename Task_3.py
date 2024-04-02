from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count:
    a = int(input("Угадайте число: "))
    count -= 1
    if a == num:
        print("Угадали!")
    elif a > num:
        print(f"Меньше! Осталось {count} попыток")
    else:
        print(f"Больше! Осталось {count} попыток")
print("Загаданное число: ", num)