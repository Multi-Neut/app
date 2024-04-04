sped = int(input("Введите скорость авто "))
povtor = int()
while (sped != -1):
    povtor += 1
    if (sped > 200):
        print("Вы ввели не риальную цифру!")
    elif (sped == 0):
        print("Машина стоит на месте.")
    elif (sped < 0):
        print("Ввод знака (-) запрещен!")
    elif (sped <= 60):
        print("Скорость нормальная!")
    else:
        print("Привышение скорости вы нарушаете ПДД!")
    sped = int(input("Введите скорость авто "))

print(f'конец прграммы! Вы проверели {povtor} авто.')