from datetime import datetime, timedelta

dogum = input("Doğum tarihi (GG/AA/YYYY): ")
#3. satırdan sonra Ai yardım alındı
dogum_tarihi = datetime.strptime(dogum, "%d/%m/%Y")   
bugun = datetime.now()

yasanan_gun = (bugun - dogum_tarihi).days
print("Yaşadığı gün sayısı:", yasanan_gun)

yuz_yas = dogum_tarihi + timedelta(days=36525)
print("100. yaş günü:", yuz_yas.strftime("%d/%m/%Y"))