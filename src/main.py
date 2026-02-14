import time
from utils import tek_veri_seti_olustur
from knapsack_dp import knapsack_dp
from knapsack_ga import GenetikAlgoritma
import sys

# Rekürsif limitini artırıyoruz (DP için gerekebilir)
sys.setrecursionlimit(20000)

def main():
    print("-" * 75)
    print(f"{'N (Eleman)':<10} | {'Yöntem':<20} | {'Süre (sn)':<15} | {'Sonuç (Değer)':<15}")
    print("-" * 75)
    
    test_senaryolari = [100, 1000, 10000] # Proje isterleri

    for n in test_senaryolari:
        # Veri seti oluşturma
        agirliklar, degerler, kapasite = tek_veri_seti_olustur(n)
        
        # --- Dinamik Programlama (DP) ---
        dp_baslangic = time.time()
        dp_sonuc = 0
        dp_sure = 0
        
        # Çok büyük veri setlerinde DP çok bellek harcar, bu yüzden N=10000 için atlıyoruz
        # veya uyarı veriyoruz. 
        if n > 2000: 
            dp_sonuc = -1 # Çalıştırılmadı
            dp_yontem_adi = "DP (Atlandı-Bellek)"
        else:
            dp_sonuc = knapsack_dp(kapasite, agirliklar, degerler, n)
            dp_yontem_adi = "Dinamik Prog. (DP)"
            
        dp_bitis = time.time()
        dp_sure = dp_bitis - dp_baslangic
        
        if dp_sonuc != -1:
            print(f"{n:<10} | {dp_yontem_adi:<20} | {dp_sure:<15.5f} | {dp_sonuc:<15}")
        else:
             print(f"{n:<10} | {dp_yontem_adi:<20} | {'-':<15} | {'-':<15}")

        # --- Genetik Algoritma (GA) ---
        ga_baslangic = time.time()
        # N=10000 gibi devasa durumlarda popülasyonu veya jenerasyonu küçük tutabiliriz hızlı sonuç için
        ga = GenetikAlgoritma(kapasite, agirliklar, degerler, n, populasyon_buyuklugu=50, jenerasyon_sayisi=100)
        ga_sonuc = ga.calistir()
        
        ga_bitis = time.time()
        ga_sure = ga_bitis - ga_baslangic
        
        print(f"{n:<10} | {'Genetik Alg. (GA)':<20} | {ga_sure:<15.5f} | {ga_sonuc:<15}")
        print("-" * 75)
        
        # Karşılaştırma yorumu
        if dp_sonuc != -1:
            hata_payi = ((dp_sonuc - ga_sonuc) / dp_sonuc) * 100
            print(f"   >>> GA, Optimuma (DP) göre %{hata_payi:.2f} farkla çalıştı.")
            print("-" * 75)

if __name__ == "__main__":
    main()
