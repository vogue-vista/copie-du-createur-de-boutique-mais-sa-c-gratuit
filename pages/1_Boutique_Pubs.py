import streamlit as st
import os
import json
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

st.title("🛍️ Générateur de Boutique IA — Version Test")

nom = st.text_input("Nom du produit")
description = st.text_area("Description du produit")
style = st.selectbox("Style de la boutique", ["Moderne", "Luxe", "Minimaliste", "Coloré"])
prix = st.text_input("Prix (optionnel)")
image_url = st.text_input("Image du produit (optionnel)")

if st.button("✨ Générer la boutique"):
    if not nom or not description:
        st.error("Veuillez remplir au moins le nom et la description.")
    else:
        if os.path.exists("boutiques.json"):
            with open("boutiques.json", "r") as f:
                data = json.load(f)
        else:
            data = []

        boutique = {
            "id": len(data) + 1,
            "nom": nom,
            "description": description,
            "style": style,
            "prix": prix,
            "image": image_url,
            "publie": False,
            "revenus": 0
        }

        data.append(boutique)

        with open("boutiques.json", "w") as f:
            json.dump(data, f)

        st.success("🎉 Boutique générée avec succès !")
