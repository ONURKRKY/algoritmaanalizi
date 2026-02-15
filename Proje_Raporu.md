# Algoritma Analizi ve Tasarımı - Proje Raporu

Bu rapor, "0/1 Sırt Çantası Problemi" (0/1 Knapsack Problem) projesinin amacını, çalışma mantığını ve teknik detaylarını içermektedir. Word gibi bir programda açmak için bu dosyayı .md (Markdown) olarak kullanabilir veya metni kopyalayabilirsiniz.

## 1. Projenin Amacı ve Öğretilmek İstenen Konular

Bu proje ile öğretilmek istenen temel kavramlar şunlardır:

### a) NP-Zor Problemler ve Çözüm Yaklaşımları
Sırt Çantası Problemi, **NP-Zor (NP-Hard)** sınıfına giren klasik bir optimizasyon problemidir. Yani eleman sayısı (N) arttıkça, tüm olasılıkları denemek imkansız hale gelir (2^N olasılık). Bu proje, bu tür zor problemlere yaklaşım farklarını göstermeyi amaçlar.

### b) Kesin Çözüm (Exact) vs. Yaklaşık Çözüm (Heuristic)
- **Dinamik Programlama (DP):** Problemi daha küçük alt problemlere bölerek **kesin ve en iyi sonucu** (optimum) bulur. Ancak çok fazla bellek ve işlem gücü gerektirir.
- **Genetik Algoritma (GA):** Doğal seçimden esinlenen bir **sezgisel (heuristic)** yöntemdir. En iyi sonucu garanti etmez ancak çok kısa sürede "yeterince iyi" bir sonuç bulur.

### c) Zaman ve Bellek Karmaşıklığı (Time & Space Complexity)
Proje, N sayısı büyüdükçe (örn: 10,000 eleman) Dinamik Programlama yönteminin neden yetersiz kaldığını (hafıza hatası veya çok uzun sürmesi) ve Genetik Algoritma'nın bu durumlarda nasıl avantaj sağladığını deneysel olarak göstermektedir.

---

## 2. Projeyi Nasıl Çalıştıracaksınız?

Projeniz Python programlama dili ile yazılmıştır. Çalıştırmak için bilgisayarınızda Python yüklü olmalıdır.

### Adım Adım Çalıştırma:

1.  **Terminali Açın:** Proje klasörünün bulunduğu dizinde (`AlgoritmaAnaliziveTasarımı`) bir terminal veya komut satırı penceresi açın.
2.  **Komutu Girin:** Aşağıdaki komutu yazıp Enter tuşuna basın:
    ```bash
    python src/main.py
    ```
    *(Eğer `python` komutu çalışmazsa `python3` veya `py` deneyebilirsiniz.)*

3.  **Çıktıyı İnceleyin:** Program sırasıyla N=100, N=1000 ve N=10000 için algoritmaları çalıştıracak ve sonuçları ekrana tablo halinde yazacaktır.

---

## 3. Dosya Yapısı ve İşleyiş Detayları

Projedeki her dosyanın belirli bir görevi vardır. `main.py` dosyası patron (yönetici) konumundadır ve diğer işçi dosyaları çağırır.

### Dosya İlişki Şeması

Bu şema, hangi dosyanın hangisini çağırdığını gösterir:

- `main.py` --> `utils.py` (Veri ister)
- `main.py` --> `knapsack_dp.py` (Hesaplama yaptırır)
- `main.py` --> `knapsack_ga.py` (Hesaplama yaptırır)

### Dosya Detayları

#### 1. `src/main.py` (Ana Yönetici Dosya)
- **Görevi:** Projenin giriş kapısıdır.
- **Ne Yapar?**
  - `test_senaryolari = [100, 1000, 10000]` listesini döner.
  - Her senaryo için `utils.py`'dan veri ister.
  - Önce `knapsack_dp` fonksiyonunu çağırır ve süresini ölçer.
  - Ardından `GenetikAlgoritma` sınıfını çağırır ve süresini ölçer.
  - İki sonucu karşılaştırıp ekrana yazdırır.
  - **Önemli Detay:** N=10000 gibi büyük durumlarda DP'nin bilgisayarı kilitlememesi için DP adımını atlar (`if n > 2000`).

#### 2. `src/utils.py` (Yardımcı Araçlar)
- **Görevi:** Test verisi üretmektir.
- **Ne Yapar?**
  - `tek_veri_seti_olustur(n)` fonksiyonu ile rastgele ağırlık ve değerlere sahip eşyalar oluşturur.
  - Çanta kapasitesini, toplam ağırlığın yarısı olarak belirler (bu standart bir zorluk testidir).

#### 3. `src/knapsack_dp.py` (Dinamik Programlama - Kesin Çözüm)
- **Görevi:** Matematiksel olarak en mükemmel sonucu bulmaktır.
- **Ne Yapar?**
  - Bir tablo oluşturur (satırlar: eşyalar, sütunlar: ağırlık kapasitesi).
  - Her hücreye "şu ana kadarki eşyalarla bu kapasitede en fazla kaç değer toplanabilir?" sorusunun cevabını yazar.
  - Tablonun sağ alt köşesindeki değer, problemin kesin cevabıdır.

#### 4. `src/knapsack_ga.py` (Genetik Algoritma - Yaklaşık Çözüm)
- **Görevi:** Evrim teorisini taklit ederek iyi bir sonucu hızlıca bulmaktır.
- **Ne Yapar?**
  - **Kromozom:** 0 ve 1'lerden oluşan diziler (1: eşyayı al, 0: alma).
  - **Popülasyon:** Rastgele oluşturulmuş çözümler topluluğu.
  - **Fitness (Uygunluk):** Çantadaki toplam değer (kapasite aşılmışsa 0 puan).
  - **Seçim (Selection):** İyi çözümlerin "çiftleşmek" üzere seçilmesi.
  - **Çaprazlama (Crossover):** İki çözümün özelliklerinin birleştirilip yeni çözüm üretilmesi.
  - **Mutasyon:** Rastgele değişikliklerle çeşitlilik sağlanması.
  - Bu işlemler belirlenen nesil sayısı (jenerasyon) boyunca tekrar edilir ve en iyi sonuç döndürülür.

---

## 4. Örnek Çıktı ve Karşılaştırma Analizi

Program çalıştırıldığında üreteceği çıktı artık tablo yerine detaylı metin raporu şeklindedir:

```
---------------------------------------------------------------------------
SONUÇLAR VE KARŞILAŞTIRMA RAPORU
---------------------------------------------------------------------------

>> SENARYO: N = 100 Eleman
------------------------------
1. Yöntem: Dinamik Programlama (DP)
   Sonuç: 3450
   Süre:  0.01500 saniye
2. Yöntem: Genetik Algoritma (GA)
   Sonuç: 3450
   Süre:  0.08200 saniye
------------------------------
ANALİZ: GA sonucu, Optimum (DP) sonuca göre %0.00 farkla bulundu.
---------------------------------------------------------------------------

>> SENARYO: N = 1000 Eleman
------------------------------
1. Yöntem: Dinamik Programlama (DP)
   Sonuç: 28900
   Süre:  0.95000 saniye
2. Yöntem: Genetik Algoritma (GA)
   Sonuç: 27455
   Süre:  0.15000 saniye
------------------------------
ANALİZ: GA sonucu, Optimum (DP) sonuca göre %5.00 farkla bulundu.
---------------------------------------------------------------------------

>> SENARYO: N = 10000 Eleman
------------------------------
1. Yöntem: Dinamik Programlama (DP)
   Durum: ATLANDI (Bellek/Zaman kısıtı nedeniyle)
   Sonuç: -
   Süre:  -
2. Yöntem: Genetik Algoritma (GA)
   Sonuç: 250400
   Süre:  1.20000 saniye
------------------------------
ANALİZ: DP çalıştırılamadığı için karşılaştırma yapılamadı.
---------------------------------------------------------------------------
```

### Karşılaştırma Mantığı (Analyzing Results)

Program, her (DP, GA) çifti için sonuçları şu formül ile karşılaştırır:

```python
hata_payi = ((dp_sonuc - ga_sonuc) / dp_sonuc) * 100
```

1.  **N=100 Durumu:** Eleman sayısı az olduğu için DP çok hızlı çalışır. GA da çok yüksek ihtimalle optimum (en iyi) sonucu bulur. Hata payı genellikle %0 olur.
2.  **N=1000 Durumu:**
    *   **DP:** Süresi artmaya başlar (yaklaşık 1 saniye). Kesin sonucu bulur.
    *   **GA:** Çok daha hızlı çalışır (0.1 - 0.2 saniye). Ancak sonucu DP'den biraz daha düşük olabilir (örneğin %1 ile %5 arası bir hata payı).
    *   **Yorum:** GA, DP'ye göre **çok daha hızlı** olmasına rağmen, mükemmel sonuca **çok yakın** bir değer bulmayı başarmıştır.
3.  **N=10000 Durumu:**
    *   **DP Analizi:** Bu boyutta DP'nin oluşturması gereken tablo `Eşya Sayısı (N) x Kapasite (W)` boyutundadır. 
        *   Tahmini Kapasite: ~250.000
        *   Hücre Sayısı: 10.000 x 250.000 = 2.500.000.000 (2.5 Milyar)
        *   Bellek Gereksinimi: ~10 GB - 70 GB RAM (Python int boyutu nedeniyle)
        *   **Sonuç:** Bu işlem standart bir bilgisayarın belleğini (RAM) aşacağı için işletim sistemi işlemi sonlandırır (`MemoryError`) veya bilgisayar donar. Bu sebeple kodumuzda bir koruma mekanizması (`if n > 2000`) ile bu adım **bilerek** atlanmıştır. Bu durum, proje isterlerinde belirtilen *"DP hangi N değerinden sonra patlıyor?"* sorusunun cevabıdır.
    *   **GA Analizi:** Genetik Algoritma bellekten bağımsız olduğu için 1-2 saniyede çalışır ve optimuma yakın bir sonuç üretir.
    *   **Yorum:** Bu senaryo, GA gibi sezgisel algoritmaların neden gerekli olduğunu kanıtlar. DP'nin tamamen çöktüğü yerde GA çalışmaya devam eder.
