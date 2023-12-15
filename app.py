import streamlit as st

# Titre de l'application
st.title("Simulateur d'épidémie en temps réel")

image_logo = st.image("imgs/le_logo.png", caption=None, use_column_width=True)

# Description du projet
st.write(
    """Epydemie c'est un simulateur en temps réel de la contagion d'un virus 
    par rapport aux populations. Ce projet vise à fournir une compréhension visuelle 
    de la propagation des maladies infectieuses et de l'impact de différentes 
    mesures préventives."""
)

image_demo = st.image("imgs/epy_capture.png", caption=None, use_column_width=True)

# Boutons interactifs
if st.button("En savoir plus sur Epydemie"):
    st.write(
        """Epydemie est un projet innovant qui utilise des modèles de simulation pour 
        prédire la propagation d'une maladie dans différentes populations. La plateforme 
        permet aux utilisateurs de tester différents scénarios en ajustant des paramètres 
        tels que le taux d'infectiosité, le taux d'asymptomatiques, etc."""
    )
    
    # Image à gauche
    col1, col2 = st.columns(2)
    col1.image("imgs/julien.jpg", caption="Julien Vincent, 17 ans", width=150)
    col2.write(
        """Expert en correction de bugs : Julien incarne la précision et l'efficacité au sein de notre équipe. 
        En tant que résolveur de bugs, il excelle dans l'art de traquer et d'éliminer les imperfections du code. 
        Sa détermination et sa perspicacité font de lui un pilier essentiel pour assurer la robustesse de notre projet. 
        Sa capacité à identifier et à résoudre rapidement les problèmes est un atout précieux qui renforce la solidité de notre code."""
    )
    
    col2.image("imgs/helios.jpg", caption="Helios Bringuet, 17 ans", width=150)
    col1.write(
        """Architecte des idées fondamentales : Helios est le cerveau créatif derrière notre projet. 
        Son rôle en tant que source d'idées fondamentales est crucial pour la direction globale de notre travail. 
        En plus d'être le pilier conceptuel de l'équipe, Helios partage son savoir en conseillant et en orientant l'équipe. 
        Sa vision novatrice et son approche unique du code inspirent l'ensemble du groupe à atteindre des sommets inégalés."""
    )
    
    col1.image("imgs/omar.jpg", caption="Omar, 17 ans", width=150)
    col2.write(
        """Logisticien et coordinateur hors pair : Omar apporte une dimension organisationnelle indispensable à notre équipe. 
        En tant que coordonnateur, il excelle dans la planification et la gestion des tâches, garantissant une collaboration fluide 
        entre les membres. Sa vision claire et sa capacité à aborder les tâches complexes avec assurance font de lui le chef d'orchestre 
        qui maintient notre projet sur la bonne voie. Omar est le garant de l'efficacité opérationnelle de notre équipe."""
    )
    
    col2.image("imgs/arthur.jpg", caption="Arthur Renault-Cléquin, 17 ans", width=150)
    col1.write(
        """Designer graphique : Arthur est le génie créatif derrière l'esthétique visuelle de notre projet. 
        En tant que designer, il donne vie à nos idées en créant des interfaces visuellement captivantes et fonctionnelles. 
        Son talent inné pour le design graphique ajoute une dimension esthétique à notre travail, créant une expérience utilisateur exceptionnelle. 
        Arthur transforme les concepts en images, et son expertise garantit que notre projet ait une présence visuelle remarquable."""
    )
    
# Pied de page
st.write(
    """Contactez-nous pour plus d'informations sur Epydemie. 
    © 2023 Epydemie. Tous droits réservés."""
)
