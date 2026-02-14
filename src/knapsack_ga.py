import random

class GenetikAlgoritma:
    def __init__(self, kapasite, agirliklar, degerler, n, populasyon_buyuklugu=50, jenerasyon_sayisi=100, mutasyon_orani=0.1):
        self.kapasite = kapasite
        self.agirliklar = agirliklar
        self.degerler = degerler
        self.n = n
        self.populasyon_buyuklugu = populasyon_buyuklugu
        self.jenerasyon_sayisi = jenerasyon_sayisi
        self.mutasyon_orani = mutasyon_orani
        self.populasyon = []

    def baslangic_populasyonu_olustur(self):
        """Rastgele bireylerden oluşan başlangıç popülasyonunu oluşturur."""
        self.populasyon = []
        for _ in range(self.populasyon_buyuklugu):
            # Her birey 0 ve 1'lerden oluşan n uzunluğunda bir listedir.
            # 1: Eşyayı al, 0: Alma
            birey = [random.randint(0, 1) for _ in range(self.n)]
            self.populasyon.append(birey)

    def uygunluk_hesapla(self, birey):
        """Bir bireyin (çözümün) uygunluk değerini (fitness) hesaplar."""
        toplam_agirlik = 0
        toplam_deger = 0
        for i in range(self.n):
            if birey[i] == 1:
                toplam_agirlik += self.agirliklar[i]
                toplam_deger += self.degerler[i]
        
        # Eğer kapasite aşılırsa, bu çözüm geçersizdir (fitness = 0 yapılır).
        if toplam_agirlik > self.kapasite:
            return 0
        else:
            return toplam_deger

    def secim(self):
        """Turnuva seçimi yöntemi ile ebeveyn seçer."""
        turnuva_boyutu = 3
        secilenler = random.sample(self.populasyon, turnuva_boyutu)
        secilenler.sort(key=lambda x: self.uygunluk_hesapla(x), reverse=True)
        return secilenler[0] # En iyi bireyi döndür

    def caprazlama(self, ebeveyn1, ebeveyn2):
        """Tek noktalı çaprazlama (Single Point Crossover)."""
        if random.random() < 0.8: # %80 çaprazlama ihtimali
            nokta = random.randint(1, self.n - 1)
            cocuk1 = ebeveyn1[:nokta] + ebeveyn2[nokta:]
            cocuk2 = ebeveyn2[:nokta] + ebeveyn1[nokta:]
            return cocuk1, cocuk2
        else:
            return ebeveyn1, ebeveyn2

    def mutasyon(self, birey):
        """Her gen için mutasyon uygular."""
        for i in range(self.n):
            if random.random() < self.mutasyon_orani:
                birey[i] = 1 - birey[i] # 0 ise 1, 1 ise 0 yap
        return birey

    def calistir(self):
        """Algoritmayı çalıştırır ve en iyi sonucu döndürür."""
        self.baslangic_populasyonu_olustur()
        
        en_iyi_cozum_degeri = 0
        
        for _ in range(self.jenerasyon_sayisi):
            yeni_populasyon = []
            
            # Elitizm: En iyiyi bir sonraki nesle doğrudan aktar
            mevcut_en_iyi = max(self.populasyon, key=self.uygunluk_hesapla)
            en_iyi_cozum_degeri = max(en_iyi_cozum_degeri, self.uygunluk_hesapla(mevcut_en_iyi))
            yeni_populasyon.append(mevcut_en_iyi)
            
            while len(yeni_populasyon) < self.populasyon_buyuklugu:
                e1 = self.secim()
                e2 = self.secim()
                
                c1, c2 = self.caprazlama(e1, e2)
                
                c1 = self.mutasyon(c1)
                c2 = self.mutasyon(c2)
                
                yeni_populasyon.append(c1)
                if len(yeni_populasyon) < self.populasyon_buyuklugu:
                    yeni_populasyon.append(c2)
            
            self.populasyon = yeni_populasyon
            
        return en_iyi_cozum_degeri
