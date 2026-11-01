# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

# 1. Veritabanýna baðlanýyoruz
baglanti = sqlite3.connect("kitaplar.db")

# 2. SQL Sorgumuzu hazýrlýyoruz
sorgu = """
SELECT * FROM kitaplar_tablosu 
ORDER BY "Fiyat Sterlin" ASC 
LIMIT 5
"""

# 3. Sorguyu çalýþtýrýyoruz
en_pahali_kitaplar = pd.read_sql_query(sorgu, baglanti)

# 4. Ekrana yazdýrýyoruz (Türkçe karakter sorunu olmasýn diye sadeleþtirdik)
print("--- EN PAHALI 5 KITAP ---")
print(en_pahali_kitaplar)

# 5. Baðlantýyý kapatýyoruz
baglanti.close()