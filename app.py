import streamlit as st
import os
import json

# -------------------------
# SUPPRIMER LA SIDEBAR
# -------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stSidebarNav"] {display: none;}
[data-testid="stSidebarUserContent"] {display: none;}
</style>
""", unsafe_allow_html=True)

# -------------------------
# POLICE PRO (Poppins)
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

st.write("")

# Bouton IA (toujours débloqué)
st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")

st.write("---")

st.header("💳 Abonnement PRO (désactivé pour les tests)")
st.write("### **50 $ / mois**")

st.write("""
Dans la version finale, l'abonnement débloquera :

- Générateur de boutique complet  
- Générateur de publicités IA  
- Analyse IA avancée  
- Export facile  
- Support prioritaire  
""")

st.info("🎉 Vous utilisez actuellement la version gratuite pour tester le générateur.")

st.write("---")

st.caption("© 2026 – IA Business Suite • Version Test")
