import streamlit as st
import os
import json

st.page_link("app.py", label="🏠 Retour à l'accueil", icon="🏠")

# -------------------------
# SUPPRIMER LA SIDEBAR & POLICE
# -------------------------
st.markdown("<style>[data-testid='stSidebar'], [data-testid='stSidebarNav'] {display: none !important;}</style>", unsafe_allow_html=True)

st.title("🛍️ Générateur de Boutique IA")

nom = st.text_input("Nom du produit")
description = st.text_area("Description du produit")
style = st.selectbox("Style de la boutique", ["Moderne", "Luxe", "Minimaliste", "Coloré"])
prix = st.text_input("Prix (optionnel)")
image_url = st.text_input("Image du produit (optionnel)")

if st.button("✨ Générer la boutique"):
    if not nom or not description:
        st.error("Veuillez remplir au moins le nom et la description.")
    else:
        # Initialiser la session si elle n'existe pas
        if "boutiques_memoire" not in st.session_state:
            st.session_state.boutiques_memoire = []
            if os.path.exists("boutiques.json") and os.path.getsize("boutiques.json") > 0:
                try:
                    with open("boutiques.json", "r", encoding="utf-8") as f:
                        st.session_state.boutiques_memoire = json.load(f)
                except:
                    pass

        boutique = {
            "id": len(st.session_state.boutiques_memoire) + 1,
            "nom": nom,
            "description": description,
            "style": style,
            "prix": prix,
            "image": image_url,
            "publie": False,
            "revenus": 0
        }

        # Ajouter à la mémoire et au fichier
        st.session_state.boutiques_memoire.append(boutique)
        
        with open("boutiques.json", "w", encoding="utf-8") as f:
            json.dump(st.session_state.boutiques_memoire, f, ensure_ascii=False, indent=4)

        st.success("🎉 Boutique générée avec succès ! Rendez-vous dans 'Mes Boutiques'.")
