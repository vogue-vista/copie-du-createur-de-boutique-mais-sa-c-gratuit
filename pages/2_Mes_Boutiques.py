import streamlit as st
import json
import os

st.page_link("app.py", label="🏠 Retour à l'accueil", icon="🏠")

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
# PAGE
# -------------------------

st.title("📦 Mes Boutiques")
st.subheader("Gérez vos boutiques générées.")

# Charger les boutiques
if os.path.exists("boutiques.json"):
    with open("boutiques.json", "r") as f:
        data = json.load(f)
else:
    data = []

# Si aucune boutique
if len(data) == 0:
    st.info("Vous n'avez encore généré aucune boutique
