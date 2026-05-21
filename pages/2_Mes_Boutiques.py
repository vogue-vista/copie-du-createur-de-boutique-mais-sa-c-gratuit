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
    st.info("Vous n'avez encore généré aucune boutique.")
else:
    for i, b in enumerate(data):
        st.write("---")
        st.write(f"### 🛍️ {b['nom']}")
        st.write(f"**Description :** {b['description']}")
        st.write(f"**Style :** {b['style']}")

        if b.get("prix"):
            st.write(f"**Prix :** {b['prix']}")

        if b.get("image"):
            st.image(b["image"], caption=b["nom"], use_column_width=True)

        # État de publication
        if b.get("publie", False):
            st.success("Boutique publiée ✔")
        else:
            st.warning("Boutique non publiée")

        # Revenus
        st.write(f"💰 **Revenus générés :** {b.get('revenus', 0)} $")

        # Bouton publier
        if st.button(f"📤 Publier la boutique", key=f"pub{i}"):
            data[i]["publie"] = True
            with open("boutiques.json", "w") as f:
                json.dump(data, f)
            st.rerun()

        # Bouton simuler revenus
        if st.button(f"💵 Simuler 1 vente (+10$)", key=f"rev{i}"):
            data[i]["revenus"] = data[i].get("revenus", 0) + 10
            with open("boutiques.json", "w") as f:
                json.dump(data, f)
            st.rerun()

        # ⭐ Bouton voir la page publique (CORRECT + DANS LA BOUCLE)
      if st.button(f"🌐 Ouvrir la page publique", key=f"url{i}"):
    url = f"/pages/3_Boutique_Public?id={b['id']}"
    st.markdown(f"<script>window.location.href = '{url}';</script>", unsafe_allow_html=True)

