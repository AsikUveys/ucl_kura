import tkinter as tk
import random
import time

# Takımlar ve isimler listeleri
takimlar = ["arsenal", "liverpool", "mancity", "manu", "chelse", "toothnam"]
isimler = ["aşık", "şahin", "ibo", "bekir", "kaan", "bedo"]

# Pencereyi oluştur
root = tk.Tk()
root.title("Kura Çekimi")
root.geometry("400x300")  # Pencere boyutunu ayarla
root.config(bg="#f0f0f0")

# Başlık etiketini ekle
title_label = tk.Label(root, text="Kura Çekimi", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Kura sonuçlarının gösterileceği metin kutusunu oluştur
result_text = tk.Text(root, width=40, height=8, font=("Helvetica", 12), wrap="word", bg="#f9f9f9", fg="#333")
result_text.pack(pady=10)

# Geri sayım etiketi
countdown_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
countdown_label.pack(pady=10)

# Kura çekme fonksiyonu
def kura_cek():
    # Kura Başlat butonunu gizle
    draw_button.pack_forget()
    
    # Listeleri karıştır
    random.shuffle(takimlar)
    random.shuffle(isimler)

    # Kura sonuçlarını metin kutusuna yazdır
    result_text.delete(1.0, tk.END)  # Önceki sonuçları sil
    result_text.insert(tk.END, "Kura Başlıyor...\n\n")
    
    # Sonuçları saklayacak liste
    final_results = []

    # Her kişiyi ve takımını tek tek yazdır
    for isim, takim in zip(isimler, takimlar):
        result_text.insert(tk.END, f"{isim} -> Takımını Öğreniyor...\n")
        result_text.update()  # Ekranı güncelle
        time.sleep(1)  # 1 saniye bekle
        
        # Geri sayım yap
        for i in range(10, 0, -1):
            countdown_label.config(text=f"{i}...")
            countdown_label.update()
            time.sleep(1)  # 1 saniye bekle
        
        # Sonuçları göster
        result_text.insert(tk.END, f"{isim} -> {takim}\n")
        result_text.update()  # Ekranı güncelle
        time.sleep(1)  # 1 saniye bekle

        countdown_label.config(text="")  # Geri sayımı temizle
        result_text.yview(tk.END)  # Sonraya kaydır

        # Sonuçları listeye ekle
        final_results.append(f"{isim} -> {takim}")
        
    # Kura tamamlandıktan sonra butonu tekrar göster
    draw_button.pack(pady=20)

    # En son sonuçları ekrana yazdır
    result_text.insert(tk.END, "\n\nKura Sonuçları:\n")
    for result in final_results:
        result_text.insert(tk.END, f"{result}\n")

# Başlat butonunu oluştur
draw_button = tk.Button(root, text="Kura Çek", font=("Helvetica", 14), command=kura_cek, bg="#4CAF50", fg="white", relief="raised", bd=3)
draw_button.pack(pady=20)

# Pencereyi başlat
root.mainloop()
