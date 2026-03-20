import random
kelime = "sinopdeneyap"  
tahmin_edilen = ["_"] * len(kelime)

alfabe = list("abcçdefgğhıijklmnoöprsştuüvyz")
denenen_harfler = []
hak = 50

print("Bilgisayar kelimeyi bulmaya çalışıyor...")

while hak > 0 and "_" in tahmin_edilen:
    harf = random.choice(alfabe)
    alfabe.remove(harf)
    denenen_harfler.append(harf)

    print(f"\nBilgisayar harfi deniyor: {harf}")

    if harf in kelime:
        for i in range(len(kelime)):
            if kelime[i] == harf:
                tahmin_edilen[i] = harf
        print("Doğru harf!")
    else:
        hak -= 1
        print("Yanlış harf!")

    print("Kelime durumu:", " ".join(tahmin_edilen))
    print("Kalan hak:", hak)

if "_" not in tahmin_edilen:
    print("\nBilgisayar kelimeyi buldu:", kelime)
else:
    print("\nBilgisayar bulamadı. Kelime:", kelime)
