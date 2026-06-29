gecerli_sifreler = []

print("Şifre Belirleme Sistemine Hoş Geldiniz!")
print("Çıkış yapmak için 'q' tuşuna basabilirsiniz.\n")

while True:
    sifre = input("Lütfen bir şifre giriniz: ")
# 7. satırdan sonra Ai yardımı alındı
    if sifre.lower() == 'q':
        print("\nProgramdan çıkılıyor...")
        break

    if len(sifre) < 6:
        print("Hata: Şifre en az 6 karakter uzunluğunda olmalıdır!\n")
        continue

    if "123" in sifre:
        print("Hata: Şifre ardışık '123' sayılarını içeremez!\n")
        continue

    gecerli_sifreler.append(sifre)
    print("Şifre başarıyla kabul edildi.")

    print(f"-> Güncel Şifre Listesi: {gecerli_sifreler}\n")

print("\n--- İŞLEM TAMAMLANDI ---")
print(f"Sistemde kayıtlı tüm şifreleriniz: {gecerli_sifreler}")