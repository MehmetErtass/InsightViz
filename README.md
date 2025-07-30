# InsightViz - Profesyonel Veri Analizi ve Görselleştirme Aracı

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-v1.0-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---

## Proje Hakkında

**InsightViz**, veri bilimi ve iş zekası süreçlerini hızlandırmak amacıyla geliştirilmiş, kullanıcı dostu ve güçlü bir web tabanlı uygulamadır. Kod yazmadan, sürükle bırak ve tıklamalarla veri setlerinizi yükleyip ön işleyebilir, kapsamlı analizler yapabilir, zengin görselleştirmeler oluşturabilir ve AI destekli içgörülerle karar destek süreçlerinizi optimize edebilirsiniz.

Bu proje, veri analizi sürecini otomatikleştirmeyi, zamandan tasarruf sağlamayı ve teknik bilgi seviyesi farklı kullanıcıların veriden değer üretmesini amaçlar.

---

https://github.com/user-attachments/assets/7a8ca507-780c-47ed-b78a-28d16c8808e5

---

## Temel Özellikler

- **Esnek Veri Yükleme:** CSV ve Excel dosya formatlarını destekler.
- **Kapsamlı Veri Ön İşleme:**
  - Eksik veri doldurma (Mean, Median, Mode seçenekleri)
  - Sütun ekleme, silme, yeniden adlandırma
  - Kategorik veriler için One-Hot Encoding
- **Zengin Veri Görselleştirme Araçları:**
  - Histogram, Boxplot, Scatter Plot
  - Korelasyon Heatmap, Pairplot
  - Barplot ve Lineplot
- **AI Destekli Otomatik Veri Analizi:**
  - Eksik veri ve aykırı değer tespiti (IQR yöntemi)
  - İstatistiksel özetler ve anomali analizi
  - Güçlü korelasyonların otomatik belirlenmesi
  - Analiz sonuçları için otomatik yorum ve öneriler
- **Veri İhracı:** Ön işlenmiş ve analiz edilmiş veriyi CSV olarak indirilebilir hale getirme

---

## Teknik Detaylar

| Teknoloji       | Versiyon     | Açıklama                                  |
|-----------------|--------------|-------------------------------------------|
| Python          | 3.8+         | Ana programlama dili                      |
| Streamlit       | 1.0+         | Web arayüzü ve interaktif uygulama       |
| Pandas          | 1.3+         | Veri işleme ve manipülasyon               |
| Matplotlib      | 3.4+         | Grafik çizim kütüphanesi                   |
| Seaborn         | 0.11+        | İstatistiksel veri görselleştirme         |
| Scikit-learn    | 0.24+        | Makine öğrenmesi ve veri analizi          |

---

## Kurulum ve Çalıştırma

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/mehmetertass/InsightViz.git
   cd InsightViz

2. **Sanal ortam oluşturun (tercihen):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows için: venv\Scripts\activate

3. **Gerekli bağımlılıkları yükleyin:**
    ```bash
   pip install -r requirements.txt

4. **Uygulamayı başlatın:**
    ```bash
   streamlit run app.py

---

Kullanım Rehberi

1.**Veri Yükleme:** Uygulama arayüzünde "Dosya Yükle" bölümünden CSV veya Excel dosyanızı seçin.

2.**Veri Ön İşleme:** Eksik verileri doldurun, sütunları yönetin, kategorik değişkenleri dönüştürün.

3.**Veri Görselleştirme:** İhtiyacınıza uygun grafik tipini seçerek verinizin görsel analizini yapın.

4.**AI Destekli Analiz:** Otomatik analiz butonuyla verinizdeki kritik noktalar, eksiklikler ve anormallikler hakkında öneriler alın.

5.**Sonuçları Kaydetme:** İşlem sonrası ön işlenmiş veri setinizi CSV formatında indirin.

