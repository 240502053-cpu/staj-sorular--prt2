class Ogrenci:
    def __init__(self, isim, vize, final):
        self.isim = isim
        self.vize = vize
        self.final = final

    def durum_hesapla(self):
        ortalama = self.vize * 0.4 + self.final * 0.6

        if ortalama >= 50:
            return "Geçti"
        else:
            return "Kaldı"


ogr = Ogrenci("Sude", 54, 100)
print(ogr.durum_hesapla())