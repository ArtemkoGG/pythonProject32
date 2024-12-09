my_str = "Привіт давай пограємо на вулиці"
tyta_split = my_str.split()
print("Ось ми розділили речення:", tyta_split)
ostanni_radok = list(map(lambda x: len(x), tyta_split))
print(ostanni_radok)