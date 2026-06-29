metin = input("Metin giriniz: ")

sesliler = "aeıioöuüAEIİOÖUÜ"

yeni = ""

for harf in metin:
    if harf not in sesliler:
        yeni += harf

print("Yeni metin:", yeni)