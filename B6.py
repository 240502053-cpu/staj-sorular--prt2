import random

hedef = random.randint(1, 50)
deneme = 0

while True:
    tahmin = int(input("Tahmininiz: "))
    deneme += 1

    if tahmin < hedef:
        print("Daha büyük")
    elif tahmin > hedef:
        print("Daha küçük")
    else:
        print(f"Tebrikler! {deneme} denemede bildiniz.")
        break