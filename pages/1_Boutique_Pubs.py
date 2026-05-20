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
# PAGE
# -------------------------

st.title("🛍️ Générateur de Boutique IA — Version Test")
st.subheader("Remplissez les informations ci-dessous pour générer votre boutique.")

st.write("")

# Champs utilisateur
nom = st.text_input("Nom du produit")
description = st.text_area("Description du produit")
style = st.selectbox("Style de la boutique", ["Moderne", "Luxe", "Minimaliste", "Coloré"])

prix = st.text_input("Prix (optionnel)")
image_url = st.text_input("Image du produit (optionnel)")

st.write("")

# Bouton de génération
if st.button("✨ Générer la boutique"):
    if not nom or not description:
        st.error("Veuillez remplir au moins le nom et la description.")
    else:
        # Création de la boutique
        boutique = {
            "nom": nom,
            "description": description,
            "style": style,
            "prix": prix,
            "image": image_url
        }

        # Charger anciennes boutiques
        if os.path.exists("boutiques.json"):
            with open("boutiques.json", "r") as f:
                data = json.load(f)
        else:
            data = []

        # Ajouter la nouvelle boutique
        data.append(boutique)

        # Sauvegarder
        with open("boutiques.json", "w") as f:
            json.dump(data, f)

        st.success("🎉 Boutique générée avec succès !")
        st.write("Votre boutique a été ajoutée à votre liste.")
