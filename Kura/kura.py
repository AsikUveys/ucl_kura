import random
import time

# Takımlar ve isimler listeleri
takimlar = ["arsenal", "liverpool", "mancity", "manu", "toothnam", "chelse"]
isimler = ["asik", "sahin", "ibo", "bekir", "kaan", "x"]

# Listeleri karıştır
random.shuffle(takimlar)
random.shuffle(isimler)

# Eşleşmeleri oluştur
eslesmeler = list(zip(takimlar, isimler))

# Kura sonuçlarını teker teker açıkla
print("Kura Basliyor...\n")
for takim, isim in eslesmeler:
    print(f"{isim} icin kura cekiliyor...")
    time.sleep(10)  # x saniye bekle
    print(f"{isim} -> {takim}\n")
    time.sleep(1)  # Sonraki kura için kısa bir bekleme
