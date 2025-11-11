ad = input("Lütfen adınızı giriniz: ")
soyad = input("Lütfen soyadınızı giriniz: ")

while True:
    try:
        yas = int(input("Lütfen yaşınızı giriniz: "))
        if 0 < yas <= 100:
            break
        elif yas <= 0:
            print("Geçersiz yaş girdiniz.")
        elif yas >= 100:
            print("Geçersiz yaş girdiniz.")
    except ValueError:
        print("Geçersiz giriş.")


print("\nGiriş Bilgileriniz:")
print(f"Ad: {ad}")
print(f"Soyad: {soyad}")
print(f"Yaş: {yas}")

if yas < 18:
    print(f"Üzgünüz, yaşınız 18'den küçük olduğu için giriş yapamazsınız")
elif yas >= 100:
  print("Geçersiz yaş girdiniz")
else:
    print(f"Hoş geldiniz, {ad} {soyad}. Girişiniz başarıyla onaylanmıştır.")
