# *******************************************************
# Nom ......... : exercice_4_3 (bonus)
# Rôle ........ : 1. Rechercher une date de naissance saisie 
#               par l'utilisateur au sein des décimales de PI
#                 2. Trouver à quel jour de la semaine correspond
#               une date 
#                 3. Calculer la somme des 20 premières décimales de Pi
#               et la somme des 12^2 premières décimales
#                 4. Insertion d'une vidéo qui explique que la somme
#               des entiers naturels est égale à -1/12
# Auteur ...... : Avrile FLORO 
# Version ..... : V0.1 du 06/01/2023
# Licence ..... : réalisé dans le cadre du cours de OIC (TP4)
#********************************************************/

import datetime
import streamlit as st
from mpmath import mp

st.title(":blue[Exercice 4.3. Bonus]", anchor=None)

#*************************PARTIE 1*******************************/

st.header(":blue[Question 1. Chercher une date de naissance dans les décimales de Pi]")

# je veux un million de décimales
mp.dps = 1000000
pi = mp.pi
# je transforme en str 
pi = str(pi)

date = st.date_input("Quelle est votre date de naissance?", min_value=datetime.date(1900,1,1))
st.write('Votre anniversaire est le:', date)
# je convertis en str
date_naissance = str(date)
# je change pour obtenir JJ/MM/AAAA (format long)
date_longue = str(date_naissance[8])+str(date_naissance[9])+str(date_naissance[5])+str(date_naissance[6])+str(date_naissance[0])+str(date_naissance[1])+str(date_naissance[2])+str(date_naissance[3])
# je change pour obtenir JJ/MM/AA (format court)
date_courte =  str(date_naissance[8])+str(date_naissance[9])+str(date_naissance[5])+str(date_naissance[6])+str(date_naissance[2])+str(date_naissance[3])

if date_longue in pi: 
    st.write("La date de naissance '",date_longue,"' se trouve parmi le premier million de décimales de Pi.")
elif date_courte in pi: 
    st.write("La date de naissance '",date_courte,"' se trouve parmi le premier million de décimales de Pi.")
else:
    st.write("Ni la date de naissance '",date_longue,"', ni la date de naissance '",date_courte,"' ne se trouve parmi le premier million de décimales de Pi.")

#*************************PARTIE 2*******************************/
from datetime import datetime

# pour présenter au format JJ/MM/AAAA
jour_date = str(date_naissance[8])+str(date_naissance[9])+"/"+str(date_naissance[5])+str(date_naissance[6])+"/"+str(date_naissance[0])+str(date_naissance[1])+str(date_naissance[2])+str(date_naissance[3])

st.header(":blue[Question 2. À quel jour correspond la date de naissance entrée?]")

# date.strftime('%A')affiche le jour de la semaine en anglais
day = date.strftime('%A')
day_str = str(day)
if day_str == "Monday":
    st.write("Le",jour_date,"était un lundi.")
if day_str == "Tuesday":
    st.write("Le",jour_date,"était un mardi.")
if day_str == "Wednesday":
    st.write("Le",jour_date,"était un mercredi.")
if day_str == "Thursday":
    st.write("Le",jour_date,"était un jeudi.")
if day_str == "Friday":
    st.write("Le",jour_date,"était un vendredi.")
if day_str == "Saturday":
    st.write("Le",jour_date,"était un samedi.")
if day_str == "Sunday":
    st.write("Le",jour_date,"était un dimanche.")

#*************************PARTIE 3*******************************/

st.header(":blue[Question 3. Additionner les décimales de Pi.]")

# calculer la somme des 20 premières décimales 
pi_20 = (float("0"+str(pi[1:22])))
# je commence à partir du "." en [1]
st.write("La somme des 20 premières décimales de Pi est égale à", pi_20)

# calculer les 12 puissance 2 premières décimales
pi_144 = (float("0"+str(pi[1:146])))
st.write("La somme des 144 premières décimales de Pi est égale à", pi_144)

#*************************PARTIE 4*******************************/
st.header(":blue[Question 4. La somme des entiers naturels est égale à -1/12.]")
url= "https://www.youtube.com/watch?v=GnZQOb9YNV4"
st.video(url)
st.write("Source: https://www.youtube.com/watch?v=GnZQOb9YNV4")
