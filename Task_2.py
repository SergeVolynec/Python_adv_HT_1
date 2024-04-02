a = int(input("Введите число: "))
if a > 1:
    for i in range(2, int(a**0.5)+1):
        if(a % i) == 0:
            print(a, " не является простым числом")
            break
    else:
        print(a, " это простое число")
else:
    print(a, " не является простым числом")
