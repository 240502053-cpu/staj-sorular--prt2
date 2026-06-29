while True:
    sifre = input("Şifre giriniz: ")

    if len(sifre) < 8:
        print("En az 8 karakter olmalı.")
        continue

    if "123" in sifre:
        print("'123' içeremez.")
        continue

    buyuk = False
    kucuk = False
#13. satırdan sonra Ai yardım alındı
    for harf in sifre:
        if harf.isupper():
            buyuk = True
        if harf.islower():
            kucuk = True

    if buyuk and kucuk:
        print("Geçerli şifre.")
        break
    else:
        print("Büyük ve küçük harf içermeli.")