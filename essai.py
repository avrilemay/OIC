# *******************************************************
# Nom ......... : exercice_4_2
# Rôle ........ : 1. Modifier les données GPS EXIF d'une image
#                 2. Modifier les coordonnées GPS 
#                 3. Montrer sur une carte les coordonnées GPS 
#                    d'une image 
#                 4. Montrer sur une carte tous les endroits 
#                    où je suis allée
# Auteur ...... : Avrile FLORO 
# Version ..... : V0.1 du 03/01/2023
# Licence ..... : réalisé dans le cadre du cours de OIC (TP4)
#********************************************************/

import streamlit as st
from PIL import Image
import os


# image utilisée
mon_image = "bernard_arnault.jpg"


# ouverture de l'image
image = Image.open(mon_image)

st.title(":blue[Exercice 4.2. Streamlit]", anchor=None)
# affichage de l'image sur streamlit
st.image(mon_image, caption='Une photo de Bernard Arnault, PDG de LVMH et homme le plus riche de France.')

# exploitation des données EXIF
from exif import Image
img_path = mon_image

with open(img_path, 'rb') as img_file:
    img = Image(img_file)
    
#*************************PARTIE 1*******************************/

st.header(":blue[Partie 1. Modifier les données EXIF d'une image]")
st.write("La photo contient des EXIF:", img.has_exif)

# début du formulaire 
with st.form("Formulaire"):
    st.write("Modifier les EXIF de la photo")

    #pixel_x_dimension
    pixel_x_dimension= st.text_input("'pixel_x_dimension' (int) : la mesure horizontale de l'image mesurée en pixels")
    # si une valeur est entrée
    if pixel_x_dimension !="":
        # on modifie la caractéristique EXIF "pixel_x_dimension"
        # on lui attribue la valeur entrée (transformée en INT)
        img.pixel_x_dimension = int(pixel_x_dimension)
        st.write("pixel_x_dimension=", {img.get("pixel_x_dimension")})

    #pixel_y_dimension
    pixel_y_dimension= st.text_input("'pixel_y_dimension' (int) : la mesure verticale de l'image mesurée en pixels")
    if pixel_y_dimension !="":
        img.pixel_y_dimension = int(pixel_y_dimension)
        st.write("pixel_y_dimension=", {img.get("pixel_y_dimension")})

    #datetime
    datetime= st.text_input("'datetime' (YYYY/MM/JJ HH:MM:SS) : moment où la photo a été prise")
    if datetime !="":
        img.datetime = datetime
        st.write("datetime=", {img.get("datetime")})

    #make
    make= st.text_input("'make' (str) : le constructeur de l'appareil photo")
    if make !="":
        img.make = make
        st.write("make=", {img.get("make")})

    #model
    model= st.text_input("'model' (str) : le modèle de l'appareil photo")
    if model !="":
        img.model = model
        st.write("model=", {img.get("model")})

    #lens_make
    lens_make= st.text_input("'lens_make' (str) : le constructeur de l'objectif")
    if lens_make !="":
        img.lens_make = lens_make
        st.write("lens_make=", {img.get("lens_make")})

    #lens_model
    lens_model= st.text_input("'lens_model' (str) : le modèle de l'objectif")
    if lens_model !="":
        img.lens_model = lens_model
        st.write("lens_model=", {img.get("lens_model")})

    #brightness_value
    brightness_value= st.text_input("'brightness_value' (int) : la valeur de la brillance")
    if brightness_value !="":
        img.brightness_value = brightness_value
        st.write("brightness_value=", {img.get("brightness_value")})

    #subject_distance
    subject_distance= st.text_input("'subject_distance' (float en mètres) : la distance en mètres du modèle de la photo")
    if subject_distance !="":
        img.subject_distance = float(subject_distance)
        st.write("subject_distance=", {img.get("subject_distance")})

    #software
    software= st.text_input("'software' (str) : le logiciel utilisé pour modifier la photo")
    if software !="":
        img.software = software
        st.write("software=", {img.get("software")})

    submitted = st.form_submit_button("Soumettre")
    if submitted:
        st.write("Les modifications ont été prises en compte")
        for EXIF in sorted(img.list_all()): 
            st.write(EXIF,'=',{img.get(EXIF)})

# j'enregistre les modifications
with open(mon_image, 'wb') as new_image_file:
    new_image_file.write(img.get_file())

#*************************PARTIE 2*******************************/

st.header(":blue[Partie 2. Modifier les coordonnées GPS d'une image]")
from GPSPhoto import gpsphoto
photo = gpsphoto.GPSPhoto(mon_image)

with st.form("GPS"):
    st.write("Modifier les données GPS de la photo")
    st.write("Les coordonnées GPS de l'endroit où je vis (La Paz, BCS au Mexique) sont: 24.140505, -110.326982, ce qui est égal à: 24 degrés 08 minutes 25 secondes Nord / 110 degrés 19 minutes 37 secondes Ouest. Nous allons mettre à jour les données EXIF de l'image pour refléter mes coordonnées géographiques.")

    # coordonnées GPS par défaut à l'IED Paris 8
    # cf carte partie 3
    lat_map = 48.945506
    lon_map = 2.362878

    taggeg_GPS = st.form_submit_button("Mettre à jour les coordonnées GPS (cliquer 2 fois pour actualiser)")
    if taggeg_GPS:
        # actualisation coordonnées GPS
        lat_map = 24.140505
        lon_map = -110.326982
        info = gpsphoto.GPSInfo((lat_map, lon_map), alt=10)
        # modification 
        photo.modGPSData(info, mon_image)
        st.write("Les coordonnées GPS ont été mis à jour.")
        for EXIF in sorted(img.list_all()): 
            st.write(EXIF,'=',{img.get(EXIF)})


    blank_GPS = st.form_submit_button("Supprimer les coordonnées GPS (cliquer 2 fois pour actualiser)")
    if blank_GPS:
        # modification 
        photo.stripData(mon_image)
        st.write("Les coordonnées GPS ont été supprimés.")
        for EXIF in sorted(img.list_all()): 
            st.write(EXIF,'=',{img.get(EXIF)})

#*************************PARTIE 3*******************************/

st.header(":blue[Partie 3. Montrer les coordonnées GPS sur une carte]")
import pandas as pd
import numpy as np

st.write("Par défaut, je me trouve à l'IED Paris 8. Si vous actualisez les coordonnées GPS de la photo, vous verrez où j'habite (: à La Paz en Basse Californie du Sud au Mexique) :")
data = pd.DataFrame({
    'Point' : ['La Paz'],
    'lat' : [lat_map],
    'lon' : [lon_map]
})
st.map(data)

#*************************PARTIE 4*******************************/

st.header(":blue[Partie 4. Ma carte du monde]")
st.write("Voici une carte présentant des endroits que j'ai visités dans le monde. Chaque endroit est identifié par son nom (ville + pays), sa longitude et sa latitude :")
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines+text",
    lon = [-21.923168, -0.130441, 4.873180,2.374710,2.222675,13.422402,
    14.418023,30.716368,96.176751,100.504699,104.922947,106.702240,120.969111,116.083243,
    145.905609,174.761406,-175.200522,-58.405505,-68.137654,-77.023360,-74.061977,-79.508529,
    -90.734078,-110.326971,-78.946289,-79.392704,-17.525911,-8.002824,-9.127454,2.179910,
    2.222675],
    lat = [64.139914, 51.500330,52.378108,48.868684,48.605059,52.516569, 50.088272,36.874834,
    16.819333,13.693209,11.565611,10.787207,14.593372,-8.358646,-41.049261,-36.848588,
    -21.134146,-34.600224,-16.498273,-12.147520,4.630366,8.977582,14.559226,24.140510,
    36.011074,43.654128,14.742567,31.641129,38.710599,41.377222,48.605059],
    text = ["Reykjavík, Islande","Londres, UK","Amsterdam, Pays-Bas","Paris, France","Ollainville, France","Berlin, Allemagne","Prague, République Tchèque","Antalya, Turquie","Yangon, Birmanie","Bangkok, Thaïlande","Phnom Phen, Cambodge","Ho Chi Minh City, Vietnam","Manille, Philippines","Gili Air, Indonésie","Burnie, Tas., Australie","Auckland, Nouvelle-Zélande","Nuku'alofa, Tonga","Buenos Aires, Argentine","La Paz, Bolivie","Lima, Pérou","Bogota, Colombie","Panama City, Panama", "Antigua, Guatemala","La Paz, Mexique","Durham, NC, USA","Toronto, Canada","Dakar, Sénégal","Marrakech, Maroc","Lisbonne, Portugal","Barcelone, Espagne","Ollainville, France"],
    marker = {'size': 15}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

st.plotly_chart(fig,theme=None)