import random


class Oyuncu:
    def __init__(self, isim):
        self.isim = isim
        self.puanlar = []

    def puan_ekle(self, puan):
        self.puanlar.append(puan)
# 10.satırdan sonra Ai yardım alındı
    def kaydet(self):
        if len(self.puanlar) == 0:
            ortalama = 0
        else:
            ortalama = sum(self.puanlar) / len(self.puanlar)

        with open("skorlar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"Oyuncu: {self.isim} - Ortalama Skor: {ortalama:.2f}\n")
        print(f"{self.isim} adlı oyuncunun skor ortalaması kaydedildi.")

oyuncular = [Oyuncu("Ahmet"), Oyuncu("Mehmet"), Oyuncu("Zeynep")]

for oyuncu in oyuncular:
    print(f"\n{oyuncu.isim} için puanlar üretiliyor:")
    for _ in range(4):
        rastgele_puan = random.randint(0, 100)
        oyuncu.puan_ekle(rastgele_puan)
        print(f"Eklendi: {rastgele_puan}")

    oyuncu.kaydet()