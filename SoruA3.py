import random

sayac = 0
atis = 0

while sayac < 3:
    sonuc = random.choice(["TURA", "YAZI"])
    atis += 1
    print(f"{atis}. atış: {sonuc}")

    if sonuc == "TURA":
        sayac += 1
    else:
        sayac = 0

print(f"\nArka arkaya 3 TURA {atis} atışta geldi.")