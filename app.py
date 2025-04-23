import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="DiagnosaAI - Asisten Dokter")
st.title("🩺 DiagnosaAI")
st.write("Masukkan data anamnesis dan pemeriksaan fisik untuk mendapatkan saran klinis.")

anamnesis = st.text_area("📝 Anamnesis", placeholder="Keluhan utama, riwayat penyakit dahulu, dll.")
pemeriksaan_fisik = st.text_area("🔍 Pemeriksaan Fisik", placeholder="Tekanan darah, suhu, auskultasi, dll.")

if st.button("Dapatkan Saran Klinis"):
    with st.spinner("Menganalisis..."):
        prompt = open("prompt_template.txt", "r").read().format(
            anamnesis=anamnesis,
            pemeriksaan=pemeriksaan_fisik
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten medis profesional."},
                {"role": "user", "content": prompt}
            ]
        )
        hasil = response.choices[0].message.content
        st.subheader("📋 Hasil Analisis")
        st.markdown(hasil)
