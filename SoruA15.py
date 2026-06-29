with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("merhaba\n")

with open("notlar.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Sakarya\n")
    dosya.write("İstanbul\n")

with open("notlar.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())