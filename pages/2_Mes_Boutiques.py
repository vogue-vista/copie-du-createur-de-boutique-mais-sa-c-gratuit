import streamlit as st
import json
import os

st.page_link("app.py", label="🏠 Retour à l'accueil", icon="🏠")

st.markdown("<style>[data-testid='stSidebar'], [data-testid='stSidebarNav'] {display: none !important;}</style>", unsafe_allow_html=True)

st.title("📦 Mes Boutiques")
st.subheader("Gérez vos boutiques générées.")

# Synchroniser la mémoire avec le fichier JSON au chargement
if "boutiques_memoire" not in st.session_state:
    st.session_state.boutiques_memoire = []
    if os.path.exists("boutiques.json") and os.path.getsize("boutiques.json") > 0:
        try:
            with open("boutiques.json", "r", encoding="utf-8") as f:
                st.session_state.boutiques_memoire = json.load(f)
        except:
            pass

data = st.session_state.boutiques_memoire

if len(data) == 0:
    st.info("Vous n'avez encore généré aucune boutique. Allez dans le Générateur IA !")
else:
    for boutique in data:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"### {boutique['nom']}")
                st.caption(f"Style: {boutique['style']} | Prix: {boutique.get('prix', 'N/A')} 💵")
            with col2:
                # Utilisation d'un bouton classique combiné à st.session_state
                if st.button("👁️ Voir", key=f"btn_{boutique['id']}"):
                    st.session_state["boutique_id_selectionnee"] = boutique["id"]
                    st.switch_page("page/3_Boutique_Public.py")
