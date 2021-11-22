# coding=utf-8
print("Добро пожаловать")
print("Доступные комманды:")
print("1 - добавить новое наименование")
print("2 - просмотреть список товаров")
print("3 - выйти")
print("4 - Считать из файла")
print("5 - Статистика")
print("6 - удалить позицию")

items = []


def readfile():
    f = open("filename.txt", "r")
    lines = f.readlines()

    for line in lines:
        splitline = line.split(" ")
        item = {
            "name": splitline[0],
            "count": splitline[1],
            "manufacture": splitline[2],
            "price": splitline[3],
            "size": splitline[4]
        }

        items.append(
            item
        )


def stat():
    manufacturesStats = []
    sizeStats = []

    statsItem={
        "name": name,
        "count": count
    }

    for item in items:
        manufacturesStats[item["name"]] = manufacturesStats[item["name"]] + 1
        sizeStats[item["size"]] = sizeStats[item["size"]] + 1
    print(manufacturesStats)
    print(sizeStats)


def delete(str):
    for item in items:
        if item["name"] == str:
            items.remove(item)


while True:
    command = int(input("> "))

    if command == 3:
        break
    elif command == 2:
        print(items)
    elif command == 4:
        readfile()
    elif command == 5:
        stat()
    elif command == 6:
        name = str(input("Название: "))
        delete(name)
    elif command == 1:
        name = str(input("Название: "))
        count = int(input("Количество: "))
        manufacture = str(input("Производитель: "))
        price = int(input("Цена: "))
        size = int(input("Размер: "))

        item = {
            "name": name,
            "count": count,
            "manufacture": manufacture,
            "price": price,
            "size": size
        }

        items.append(item)
