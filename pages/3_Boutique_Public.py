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
# LIRE L'ID DEPUIS LA MÉMOIRE (Début du Module 3)
# -------------------------
if "boutique_id_selectionnee" not in st.session_state:
    st.write("👋 Sélectionnez une boutique depuis *Mes Boutiques*.")
    st.stop()

boutique_id = st.session_state["boutique_id_selectionnee"]
st.switch_page("3_Boutique_Public.py")
# -------------------------
# CHARGER LES BOUTIQUES
# -------------------------
if "boutiques_memoire" in st.session_state:
    data = st.session_state.boutiques_memoire
elif os.path.exists("boutiques.json"):
    with open("boutiques.json", "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.error("Aucune boutique trouvée.")
    st.stop()

boutique = next((b for b in data if b["id"] == boutique_id), None)

if boutique is None:
    st.error("Boutique introuvable.")
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
