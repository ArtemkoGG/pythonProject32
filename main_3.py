names = ["Bolodya", "Alice", "Bob", "Alice", "John", "Artem"]
set_names = set(names)
new_names = list(map(lambda a: (f"{a} Smith"), set_names))
print(f"Ось унікальні імена з фамілією Smith: {new_names}")