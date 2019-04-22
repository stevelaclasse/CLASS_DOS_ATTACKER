# -*- coding: utf-8 -*-
import Tkinter
import os
from tkMessageBox import *
import subprocess
import shlex
import sys
	

class test_fenetre(Tkinter.Tk):
	
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
		if os.getuid() != 0: 
    			showerror("ERREUR DROITS D'ACCES"," vous devez exécuter ce programme en administrateur")
    			sys.exit(1)
		
		


	def initialize(self):
		self["bg"]="green"
	
		self.frame1=Tkinter.Frame(self,borderwidth=2,width=100,height=100,relief=Tkinter.GROOVE)
		#self.frame1.pack()
		self.frame1.grid(column=0,row=0,sticky="EW",pady=10,padx=30)
		
		##variable de colonnes et lignes
		x=0
		y=0
		self.frame1.rowconfigure(0, weight=1)
		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.columnconfigure(0, weight=1)

		## CREATION DES BOUTONS


		self.f1b1 = Tkinter.Button(self.frame1,text="ICMP FLOOD",bg="#40E0D0",activebackground="#00FFFF",cursor="spider",height=5,width=25,command=self.icmp,relief=Tkinter.RAISED)
		self.f1b1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)
		x=(x+2)%3  
		
		

		self.f1b2 = Tkinter.Button(self.frame1,text="TCP SYN FLOOD",bg="#40E0D0",activebackground="#00FFFF",cursor="spider",height=5,width=25,command=self.tcp,relief=Tkinter.RAISED)
		self.f1b2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+2)%3
		y=(y+1)

		self.f1b3 = Tkinter.Button(self.frame1,text="ARP CACHE POISONING",bg="#40E0D0",activebackground="#00FFFF",cursor="spider",height=5,width=25,command=self.arp,relief=Tkinter.RAISED)
		self.f1b3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+2)%3
		y=(y+1)
		self.f1b4 = Tkinter.Button(self.frame1,text="DHCP STARVATION",bg="#40E0D0",activebackground="#00FFFF",cursor="spider",height=5,width=25,command=self.dhcp,relief=Tkinter.RAISED)
		self.f1b4.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)


		x=(x+2)%3
		self.f1b5 = Tkinter.Button(self.frame1,text="WIFI DEAUTHENTIFICATION",bg="#40E0D0",activebackground="#00FFFF",cursor="spider",height=5,width=25,command=self.kick,relief=Tkinter.RAISED)
		self.f1b5.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		#GESTION DU REZIZE DE LA FENETRE

		#for row_index in range(0,2):
    		#	self.frame1.rowconfigure(row_index, weight=1)
		#	self.frame1.master.rowconfigure(row_index, weight=1)
		
		#for column_index in range(0,3):
    		#	self.frame1.columnconfigure(column_index, weight=1)
		#	self.frame1.master.columnconfigure(column_index, weight=1)

		
		## CREATION DE LA BARRE DE MENU
		self.Barre_Menu=Tkinter.Menu(self)
		self.col1=Tkinter.Menu(self.Barre_Menu,tearoff=0)
		'''col1.add_command(label="Nouveau",command=self.info_box)'''
		self.col1.add_command(label="Enregister Parametres",command=self.info_box)
		self.col1.add_separator()
		self.col1.add_command(label="Fermer",command=self.quit)
		self.Barre_Menu.add_cascade(label="Fichier",menu=self.col1)
	
		self.col2=Tkinter.Menu(self.Barre_Menu)
		self.col2.add_command(label="Charger Parametres par defaut",command=self.charger_default)
		self.col2.add_command(label="Charger Parametres depuis un fichier",command=self.info_box)
		self.Barre_Menu.add_cascade(label="Edition",menu=self.col2)

		self.col3=Tkinter.Menu(self.Barre_Menu)
		self.col3.add_command(label="Aide",command=self.info_box)
		self.col3.add_command(label="A Propos",command=self.info_box)
		self.Barre_Menu.add_cascade(label="?",menu=self.col3)
		
		self.config(menu=self.Barre_Menu)
		
	def icmp(self):
		
		script_path="ICMP_FLOOD/launch_icmp_flood_graphique.py"
		#the_icmp=['python ']
		subprocess.Popen(['python',script_path])
		#print(os.path.join(os.getcwd(),script_path))

	def tcp(self):
		script_path="TCP_SYN/launch_tcp_syn_graphique_2.py"
		#the_icmp=['python ']
		subprocess.Popen(['python',script_path])
		#print(os.path.join(os.getcwd(),script_path))

	def arp(self):
		script_path="ARP_CACHE_POISONING/launch_arp_spoof_graphique.py"
		#the_icmp=['python ']
		subprocess.Popen(['python',script_path])
		#print(os.path.join(os.getcwd(),script_path))

	def dhcp(self):
		script_path="DHCP_STARVATION/launch_dhcp_starvation_graphique.py"
		#the_icmp=['python ']
		subprocess.Popen(['python',script_path])
		#print(os.path.join(os.getcwd(),script_path))

	def kick(self):
		script_path="WIFI_DEAUTHENTIFICATION/launch_kick_deauth_graphique.py"
		#the_icmp=['python ']
		subprocess.Popen(['python',script_path])
		#print(os.path.join(os.getcwd(),script_path))


	def charger_default(self):
		showinfo("Erreur", "Aucun Paramètre à charger")	
			

	def message_box(self):
		#print("VERIFICATION VOUS VOUS VRAIMENT FAIRE CELA")
		showinfo("MESSAGE","ACTION PRISE EN COMPTE")	

	def info_box(self):
		print("INFORMATIONS DE MESSAGE")

	

	
