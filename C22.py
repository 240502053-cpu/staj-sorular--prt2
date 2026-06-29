menu = {
    "cay": 25,
    "kahve": 60,
    "tost": 80,
    "pasta": 90,
    "su": 15
}

siparisler = []
toplam_tutar = 0
# 12. satırdan sonra Ai yardım alındı
print("--- Kafe Sipariş Sistemine Hoş Geldiniz ---")
print("Menü Ürünleri:", ", ".join([urun.capitalize() for urun in menu.keys()]))
print("Lütfen siparişinizi 'urun-adet' formatında giriniz (Örn: cay-2).")
print("Siparişi tamamlamak ve fiş kesmek için 'onay' yazınız.\n")

while True:
    girdi = input("Sipariş giriniz / onay: ").strip().lower()

    if girdi == 'onay':
        break

    if "-" not in girdi:
        print("Hata: Lütfen ürünü ve adedi aralarında '-' olacak şekilde giriniz (Örn: tost-1).\n")
        continue

    parcalar = girdi.split("-")
    urun = parcalar[0].strip()
    adet_str = parcalar[1].strip()

    if not adet_str.isdigit():
        print("Hata: Adet kısmına geçerli bir sayı girmelisiniz!\n")
        continue

    adet = int(adet_str)

    if urun in menu:
        fiyat = menu[urun]
        ara_toplam = fiyat * adet
        toplam_tutar += ara_toplam

        siparisler.append({
            "urun": urun,
            "adet": adet,
            "birim_fiyat": fiyat,
            "ara_toplam": ara_toplam
        })
        print(f"-> {adet} adet {urun.capitalize()} siparişe eklendi. (Ara Toplam: {ara_toplam} TL)\n")
    else:
        print(f"Hata: '{urun}' menümüzde bulunmamaktadır. Lütfen tekrar deneyin.\n")

print("\n" + "=" * 30)
print("            FİŞ")
print("=" * 30)

if not siparisler:
    print("Sipariş verilmedi.")
else:
    for s in siparisler:
        print(f"{s['urun'].capitalize():<10} x {s['adet']:<3} = {s['ara_toplam']:>5} TL")

    print("-" * 30)
    print(f"Brüt Toplam: {toplam_tutar:>14} TL")

    if toplam_tutar > 200:
        indirim = toplam_tutar * 0.10
        net_tutar = toplam_tutar - indirim
        print(f"200 TL Üstü %10 İndirim: -{indirim:>6.2f} TL")
        print("-" * 30)
        print(f"ÖDENECEK TUTAR: {net_tutar:>11.2f} TL")
    else:
        print(f"ÖDENECEK TUTAR: {toplam_tutar:>11}.00 TL")

print("=" * 30)
print("Afiyet Olsun! Yine Bekleriz.")