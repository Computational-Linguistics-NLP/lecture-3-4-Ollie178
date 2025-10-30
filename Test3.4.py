# Первый способ
year = int(input("Введите год: "))
if year % 400 == 0:
    print("да")
elif year % 100 == 0:
    print("нет")
elif year % 4 == 0:
    print("да")
else:
    print("нет")



# Второй способ
year = int(input("Введите год: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("да")
else:
    print("нет")



# Третий способ
year = int(input("Введите год: "))
result = "да" if (year % 400 == 0) or \
         (year % 4 == 0 and year % 100 != 0) else "нет"
print(result)



