def knapsack_dp(kapasite, agirliklar, degerler, n):
    """
    Sırt Çantası Problemi için Dinamik Programlama (DP) Çözümü.
    
    Argümanlar:
        kapasite (int): Çantanın alabileceği maksimum ağırlık.
        agirliklar (list): Eşyaların ağırlıkları.
        degerler (list): Eşyaların değerleri.
        n (int): Eşya sayısı.
        
    Döndürür:
        int: Çantaya sığan maksimum toplam değer.
    """
    # DP tablosunu oluşturma (n+1 x kapasite+1 boyutunda)
    # K[i][w] -> ilk i eşya kullanılarak w kapasitesi ile elde edilen maksimum değer.
    
    # Not: Büyük kapasitelerde bu tablo çok yer kaplayabilir (Memory Error riski).
    # Ancak N=1000 ve kapasite makul olursa çalışır.
    
    K = [[0 for x in range(kapasite + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(kapasite + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif agirliklar[i-1] <= w:
                # Eşyayı alırsak vs almazsak durumlarının maksimumu
                # Eşyayı aldığımızda: degerler[i-1] + kalan kapasite (w - agirliklar[i-1]) için en iyi değer
                K[i][w] = max(degerler[i-1] + K[i-1][w-agirliklar[i-1]], K[i-1][w])
            else:
                # Eşya sığmıyorsa, almayız.
                K[i][w] = K[i-1][w]
                
    return K[n][kapasite]
