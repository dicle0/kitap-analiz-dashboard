# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sqlite3  # 1. SQLite kütüphanesini koda dahil ettik

kitap_sepeti = []

# 1'den 50. sayfaya kadar tüm sayfalarý geziyoruz
for sayfa_no in range(1, 51):
    print(f"Sayfa {sayfa_no}/50 kaziniyor...")
    
    url = f"http://books.toscrape.com/catalogue/page-{sayfa_no}.html"
    cevap = requests.get(url)
    soup = BeautifulSoup(cevap.text, "html.parser")

    kitap_kutulari = soup.find_all("article", class_="product_pod")

    for kutu in kitap_kutulari:
        kitap_adi = kutu.find("h3").text.strip()
        
        # Fiyat temizleme
        ham_fiyat = kutu.find("p", class_="price_color").text.strip()
        sadece_sayilar = "".join([karakter for karakter in ham_fiyat if karakter.isdigit() or karakter == '.'])
        sayisal_fiyat = float(sadece_sayilar)
        
        # Stok temizleme
        ham_stok = kutu.find("p", class_="availability").text.strip()
        if "In stock" in ham_stok:
            temiz_stok = "Stokta Var"
        else:
            temiz_stok = "Stokta Yok"
        
        kitap_sepeti.append({
            "Kitap Adi": kitap_adi,
            "Fiyat Sterlin": sayisal_fiyat,
            "Stok Durumu": temiz_stok
        })
    
    time.sleep(1)

# Pandas Tablosu Oluþturma
tablo = pd.DataFrame(kitap_sepeti)

# 1. Yöntem: CSV Dosyasýna Kaydetme
tablo.to_csv("kitaplar.csv", index=False, encoding="utf-8-sig")

# 2. Yöntem: SQL Veritabanýna Kaydetme
baglanti = sqlite3.connect("kitaplar.db")
tablo.to_sql("kitaplar_tablosu", baglanti, if_exists="replace", index=False)
baglanti.close()

print(f"\nISLEM TAMAMLANDI!")
print(f"1000 kitap hem 'kitaplar.csv' hem de 'kitaplar.db' (SQL) dosyasina kaydedildi.")