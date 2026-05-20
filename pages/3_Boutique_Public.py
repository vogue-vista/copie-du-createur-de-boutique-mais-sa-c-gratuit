import streamlit as st
import json
import os

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
# PAGE PUBLIQUE
# -------------------------

# Récupérer l'ID depuis l'URL
params = st.query_params
if "id" not in params:
    st.error("Aucune boutique sélectionnée.")
    st.stop()

boutique_id = int(params["id"])

# Charger les boutiques
if os.path.exists("boutiques.json"):
    with open("boutiques.json", "r") as f:
        data = json.load(f)
else:
    st.error("Aucune boutique trouvée.")
    st.stop()

# Trouver la boutique
boutique = None
for b in data:
    if b["id"] == boutique_id:
        boutique = b
        break

if boutique is None:
    st.error("Boutique introuvable.")
    st.stop()

# -------------------------
# AFFICHAGE DE LA BOUTIQUE
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

# Bouton d'achat (factice pour l'instant)
st.write("### Acheter")
st.button("🛒 Acheter maintenant (bientôt disponible)")
