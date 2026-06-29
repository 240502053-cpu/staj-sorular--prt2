import random

sayilar = [random.randint(0, 100) for i in range(15)] 

secilen = [x for x in sayilar if 40 <= x <= 60]

secilen.sort(reverse=True)

print("Üretilen Sayılar:", sayilar)
print("Sonuç:", " - ".join(map(str, secilen)))