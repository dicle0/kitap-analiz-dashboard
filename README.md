# 📚 Kitap Analiz ve Veri Görselleştirme Dashboard'u

Bu proje, web üzerindeki kitap verilerini otomatik olarak kazıyan, bir **SQLite** veritabanında depolayan ve **Streamlit** kullanarak etkileşimli bir veri analizi panosu (dashboard) sunan bir Python uygulamasıdır.

---

## 🚀 Özellikler

* **Veri Kazıma (Web Scraping):** Kitap adı, fiyatı, stok durumu ve değerlendirme puanı gibi verilerin çekilmesi.
* **Veritabanı Yönetimi:** Çekilen verilerin `SQLite` veritabanında (`kitaplar.db`) düzenli şekilde saklanması.
* **SQL Sorguları:** Veritabanı üzerinde dinamik sorgulamalar yapılması (`sql_sorgulari.py`).
* **Etkileşimli Arayüz:** `Streamlit` ile veri filtreleme, grafiksel analiz ve görsel dashboard sunumu.

---

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Veri Kazıma & İşleme:** `BeautifulSoup`, `requests`, `pandas`
* **Veritabanı:** `SQLite3`
* **Web & Dashboard Framework:** `Streamlit`
* **Versiyon Kontrolü:** Git & GitHub

---

## 📁 Proje Yapısı

```text
staj projem/
├── app.py              # Streamlit arayüz ve dashboard kodları
├── veri_kazici.py      # Web scraping (veri kazıma) betiği
├── sql_sorgulari.py    # SQL sorguları ve veritabanı bağlantıları
├── kitaplar.db         # Kazılan verilerin saklandığı SQLite veritabanı
├── kitaplar.csv        # Dışa aktarılan veri seti
├── .gitignore          # Git tarafından takip edilmeyecek dosyalar
└── README.md           # Proje tanıtım ve kullanım kılavuzu

## 🔧 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu bilgisayarınıza klonlayın:
   git clone https://github.com/dicle0/kitap-analiz-dashboard.git
   cd kitap-analiz-dashboard

2. Gerekli kütüphaneleri yükleyin:
   pip install pandas streamlit beautifulsoup4 requests

3. Streamlit uygulamasını başlatın:
   streamlit run app.py