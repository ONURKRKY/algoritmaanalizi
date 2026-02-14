import random

def tek_veri_seti_olustur(eleman_sayisi, maksimum_agirlik=50, maksimum_deger=100):
    """
    Belirtilen sayıda rastgele ağırlık ve değer çifti oluşturur.
    
    Argümanlar:
        eleman_sayisi (int): Oluşturulacak eşya sayısı (N).
        maksimum_agirlik (int): Bir eşyanın alabileceği maksimum ağırlık.
        maksimum_deger (int): Bir eşyanın alabileceği maksimum değer.
        
    Döndürür:
        agirliklar (list): Eşyaların ağırlık listesi.
        degerler (list): Eşyaların değer listesi.
        kapasite (int): Çantanın toplam kapasitesi (toplam ağırlığın %50'si olarak ayarlandı).
    """
    agirliklar = [random.randint(1, maksimum_agirlik) for _ in range(eleman_sayisi)]
    degerler = [random.randint(1, maksimum_deger) for _ in range(eleman_sayisi)]
    
    # Kapasite genellikle toplam ağırlığın yarısı kadar seçilir ki zor bir problem olsun.
    toplam_agirlik = sum(agirliklar)
    kapasite = int(toplam_agirlik * 0.5)
    
    return agirliklar, degerler, kapasite
