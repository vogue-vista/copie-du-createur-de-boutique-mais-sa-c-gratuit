import streamlit as st
import json
import os

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
# LIRE L'ID DE L'URL
# -------------------------

params = st.query_params

if "id" not in params:
    st.write("👋 Sélectionnez une boutique depuis *Mes Boutiques*.")
    st.stop()

try:
    boutique_id = int(params["id"])
except:
    st.error("ID invalide.")
    st.stop()

# -------------------------
# CHARGER LES BOUTIQUES (Dans le Module 3)
# -------------------------
if "boutiques_memoire" in st.session_state:
    data = st.session_state.boutiques_memoire
elif os.path.exists("boutiques.json"):
    with open("boutiques.json", "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.error("Aucune boutique trouvée.")
    st.stop()


# -------------------------
# AFFICHAGE
# -------------------------

st.title(f"🛍️ {boutique['nom']}")

if boutique.get("image"):
    st.image(boutique["image"], use_column_width=True)

st.write("### Description")
st.write(boutique["description"])

st.write("### Style")
st.write(boutique["style"])

if boutique.get("prix"):
    st.write("### Prix")
    st.write(f"💵 {boutique['prix']}")

st.write("### Acheter")
st.button("🛒 Acheter maintenant (bientôt disponible)")
