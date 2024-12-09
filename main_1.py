my_list = [12, 34, 23, 98, 67, 33]
tilki_parni = list(filter(lambda x: x % 2 == 0, my_list))
print("Це всі пані числа:", tilki_parni)
kvadryat = list(map(lambda y: y**2, tilki_parni))
print("Це їхній квадрат:",kvadryat)