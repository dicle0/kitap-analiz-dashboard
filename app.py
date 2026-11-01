# -*- coding: utf-8 -*-
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Sayfa Başlığı
st.title("📚 Kitap Analiz Dashboard")
st.write("Veritabanındaki 1000 kitabın canlı verisi aşağıda listelenmektedir.")

# 1. Veritabanına bağlanıp veriyi çekiyoruz
baglanti = sqlite3.connect("kitaplar.db")
sorgu = 'SELECT * FROM kitaplar_tablosu'
df = pd.read_sql_query(sorgu, baglanti)
baglanti.close()

# 2. Sol Yan Menüye (Sidebar) Fiyat Filtresi Ekliyoruz
st.sidebar.header("🔍 Filtreleme Seçenekleri")

min_fiyat = float(df["Fiyat Sterlin"].min())
max_fiyat = float(df["Fiyat Sterlin"].max())

secilen_fiyat = st.sidebar.slider(
    "Fiyat Aralığı (£)",
    min_value=min_fiyat,
    max_value=max_fiyat,
    value=(min_fiyat, max_fiyat)
)

# 3. Veriyi Filtreliyoruz
filtrelenmis_df = df[
    (df["Fiyat Sterlin"] >= secilen_fiyat[0]) & 
    (df["Fiyat Sterlin"] <= secilen_fiyat[1])
]

# 4. Özet Metrikler
toplam_kitap = len(filtrelenmis_df)
ortalama_fiyat = filtrelenmis_df["Fiyat Sterlin"].mean() if toplam_kitap > 0 else 0

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Seçilen Kitap Sayısı", value=toplam_kitap)
with col2:
    st.metric(label="Ortalama Fiyat", value=f"£{ortalama_fiyat:.2f}")

st.divider()

# 5. GRAFİKLER BÖLÜMÜ
if not filtrelenmis_df.empty:
    # Grafik 1: Fiyat Dağılımı
    st.subheader("📊 Fiyat Dağılım Grafiği")
    fig_fiyat = px.histogram(
        filtrelenmis_df, 
        x="Fiyat Sterlin", 
        nbins=25, 
        title="Kitapların Fiyat Aralığına Göre Dağılımı",
        labels={"Fiyat Sterlin": "Fiyat (£)", "count": "Kitap Sayısı"},
        template="plotly_white"
    )
    fig_fiyat.update_traces(marker_color="#4F46E5", marker_line_color="white", marker_line_width=1.5)
    fig_fiyat.update_layout(yaxis_title="Kitap Sayısı", bargap=0.15)
    st.plotly_chart(fig_fiyat, use_container_width=True)

    st.divider()

    # Grafik 2: Stok Durumu Grafiği (Donut Chart)
    st.subheader("📦 Stok Durumu Dağılımı")
    
    stok_ozet = filtrelenmis_df["Stok Durumu"].value_counts().reset_index()
    stok_ozet.columns = ["Stok Durumu", "Kitap Sayısı"]

    fig_stok = px.pie(
        stok_ozet,
        names="Stok Durumu",
        values="Kitap Sayısı",
        title="Seçilen Kitapların Stok Durumu Oranı",
        hole=0.4,
        color_discrete_sequence=["#10B981", "#EF4444"]
    )
    fig_stok.update_traces(textinfo="percent+label")
    
    st.plotly_chart(fig_stok, use_container_width=True)

else:
    st.warning("Seçilen fiyat aralığında kitap bulunamadı.")

st.divider()

# 6. Tablo ve İndirme Butonu Bölümü
st.subheader("📋 Filtrelenmiş Kitap Listesi")

# CSV İndirme Hazırlığı
if not filtrelenmis_df.empty:
    csv_veri = filtrelenmis_df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Filtrelenmiş Listeyi CSV Olarak İndir",
        data=csv_veri,
        file_name="filtrelenmis_kitaplar.csv",
        mime="text/csv"
    )

st.dataframe(filtrelenmis_df)