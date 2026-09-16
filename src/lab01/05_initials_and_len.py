a = input("ФИО: ").split()
b = [i for i in a if len(i)>1]
print(f"Инициалы: {b[0][0]}{b[1][0]}{b[2][0]}.")
print(f"Длина (символов): {len(b[0])+len(b[1])+len(b[2])+2}")