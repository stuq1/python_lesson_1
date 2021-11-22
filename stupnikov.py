# coding=utf-8
print("Добро пожаловать")
print("Доступные комманды:")
print("1 - добавить новое наименование")
print("2 - просмотреть список товаров")
print("3 - выйти")

items = []

while True:
    command = int(input("> "))

    if command == 3:
        break
    elif command == 2:
        print(items)
    elif command == 1:
        name = str(input("Название: "))
        count = int(input("Количество: "))

        item = {
            "name": name,
            "count": count
        }

        items.append(item)