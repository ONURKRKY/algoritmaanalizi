import time
from utils import tek_veri_seti_olustur
from knapsack_dp import knapsack_dp
from knapsack_ga import GenetikAlgoritma
import sys

# Rekürsif limitini artırıyoruz (DP için gerekebilir)
sys.setrecursionlimit(20000)

def main():
    print("---------------------------------------------------------------------------")
    print("SONUÇLAR VE KARŞILAŞTIRMA RAPORU")
    print("---------------------------------------------------------------------------")
    
    test_senaryolari = [100, 1000, 10000] # Proje isterleri

    for n in test_senaryolari:
        print(f"\n>> SENARYO: N = {n} Eleman")
        print("-" * 30)
        
        # Veri seti oluşturma
        agirliklar, degerler, kapasite = tek_veri_seti_olustur(n)
        
        # --- Dinamik Programlama (DP) ---
        dp_baslangic = time.time()
        dp_sonuc = 0
        dp_sure = 0
        
        # Çok büyük veri setlerinde DP çok bellek harcar, bu yüzden N=10000 için atlıyoruz
        if n > 2000: 
            dp_sonuc = -1 # Çalıştırılmadı
            print(f"1. Yöntem: Dinamik Programlama (DP)")
            print(f"   Durum: ATLANDI (Bellek/Zaman kısıtı nedeniyle)")
            print(f"   Sonuç: -")
            print(f"   Süre:  -")
        else:
            dp_sonuc = knapsack_dp(kapasite, agirliklar, degerler, n)
            dp_bitis = time.time()
            dp_sure = dp_bitis - dp_baslangic
            print(f"1. Yöntem: Dinamik Programlama (DP)")
            print(f"   Sonuç: {dp_sonuc}")
            print(f"   Süre:  {dp_sure:.5f} saniye")
            
        # --- Genetik Algoritma (GA) ---
        ga_baslangic = time.time()
        # N=10000 gibi devasa durumlarda popülasyonu veya jenerasyonu küçük tutabiliriz hızlı sonuç için
        ga = GenetikAlgoritma(kapasite, agirliklar, degerler, n, populasyon_buyuklugu=50, jenerasyon_sayisi=100)
        ga_sonuc = ga.calistir()
        
        ga_bitis = time.time()
        ga_sure = ga_bitis - ga_baslangic
        
        print(f"2. Yöntem: Genetik Algoritma (GA)")
        print(f"   Sonuç: {ga_sonuc}")
        print(f"   Süre:  {ga_sure:.5f} saniye")
        
        # Karşılaştırma yorumu
        print("-" * 30)
        if dp_sonuc != -1:
            hata_payi = ((dp_sonuc - ga_sonuc) / dp_sonuc) * 100
            print(f"ANALİZ: GA sonucu, Optimum (DP) sonuca göre %{hata_payi:.2f} farkla bulundu.")
        else:
            print(f"ANALİZ: DP çalıştırılamadığı için karşılaştırma yapılamadı.")
        print("---------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
