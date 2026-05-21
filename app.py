import streamlit as st
import os
import json

# -------------------------
# SUPPRIMER LA SIDEBAR
# -------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stSidebarNav"] {display: none !important;}
[data-testid="stSidebarUserContent"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

# -------------------------
# POLICE POPPINS
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
html, body, div, p, h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# PAGE D'ACCUEIL
# -------------------------

st.title("🚀 IA Business Suite — Version Test")
st.subheader("Testez le générateur de boutique gratuitement.")

st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")
st.page_link("pages/2_Mes_Boutiques.py", label="📦 Voir mes boutiques", icon="📁")
st.page_link("pages/3_Boutique_Public.py", label="🌐 Voir les boutiques publiques", icon="🌍")

st.write("---")
st.caption("© 2026 – IA Business Suite • Version Test")
