import Tkinter
from tkMessageBox import *
import sys
import Tix
import os
import commands
import ttk
import time
import random
import threading
import ma_thread_tcp_syn
import Log_class
import infoBulle_class



class test_fenetre(Tkinter.Tk):
	
	monlog_content=0
	
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		
		self.parent=parent
		self.initialize()
		self.thread_alive=False
		global verrou
		verrou=threading.Lock()
		self.mon_verrou=False
		self.attack=ma_thread_tcp_syn.tcp_syn(self.f1t1.get(),"",self.f2t1.get(),self.f2t2.get(),"","",self.f3t3.get(),self.ma_liste.get())
		if os.getuid() != 0: 
    			showerror("ERROR ACCESS RIGHTS"," you must run this program as an administrator")
    			sys.exit(1)
		
	def check_verrou(self):
		return self.mon_verrou	
	
	def edit_verrou(self,data):
		self.mon_verrou=data

	def initialize(self):
		
		
		self["bg"]="green"
	
		self.frame1=Tkinter.Frame(self,borderwidth=2,width=100,height=100,relief=Tkinter.GROOVE)
		self.frame1.grid(column=0,row=0,sticky="EW",pady=10,padx=30)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(0, weight=1)
		self.frame1.columnconfigure(0, weight=1)


		self.frame2=Tkinter.LabelFrame(self,text="LOGS DISPLAY",borderwidth=2,height=10,relief=Tkinter.GROOVE)
		self.frame2.grid(column=0,row=1,pady=10,padx=30)

		self.frame2.master.rowconfigure(0, weight=1)
		self.frame2.master.columnconfigure(0, weight=1)
		self.frame2.rowconfigure(0, weight=1)
		self.frame2.columnconfigure(0, weight=1)


		##variable de colonnes et lignes
		x=0
		y=0

		#REMPLISSAGE DU PANNEAU CONCERNANT L'ORDINATEUR ATTAQUANT
		f1t1=Tkinter.Label(self.frame1,text="INFORMATION ON THE ATTACKING COMPUTER",height=5,fg="blue",anchor="w")
		f1t1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		
		y=(y+1)
		self.f1l1=Tkinter.Label(self.frame1, text="IP SOURCE:",height=2,width=20,anchor="e")
		self.f1l1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f1t1=Tkinter.StringVar()
		self.f1t1.set("")
		self.f1z1=Tkinter.Entry(self.frame1,textvariable=self.f1t1,width=15)
		self.f1z1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		self.f1z1.bind("<Enter>",self.ip_source_hover_in)
		self.f1z1.bind("<Leave>",self.ip_source_hover_out)
		x=(x+1)%2
		y=y+1

		## REMPLISSAGE DU PANNEAU CONCERNANT L'ORDINATEUR CIBLE
		f1t2=Tkinter.Label(self.frame1,text="NFORMATION ON THE TARGET COMPUTER",height=5,fg="blue",anchor="w")
		f1t2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		y=(y+1)
		self.f2l1=Tkinter.Label(self.frame1, text="IP DESTINATION:",height=2,anchor="e")
		self.f2l1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f2t1=Tkinter.StringVar()
		self.f2t1.set("")
		self.f2z1=Tkinter.Entry(self.frame1,textvariable=self.f2t1,width=15)
		self.f2z1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)
		self.f2l2=Tkinter.Label(self.frame1, text="DESTINATION PORT:",height=2,anchor="e")
		self.f2l2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f2t2=Tkinter.StringVar()
		self.f2t2.set("")
		self.f2z2=Tkinter.Entry(self.frame1,textvariable=self.f2t2,width=10)
		self.f2z2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)


		## REMPLISSAGE DU PANNEAU CONCERNANT LES INFOMATIONS COMPLEMENTAIRES SUR L'ATTAQUE
		f1t3=Tkinter.Label(self.frame1,text="ADDITIONAL INFORMATION ON THE ATTACK",height=5,fg="blue",anchor="w")
		f1t3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		y=(y+1)


		f3l3=Tkinter.Label(self.frame1, text="TIME INTERVAL BETWEEN TWO PACKETS:",height=2,anchor="e")
		f3l3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f3t3=Tkinter.StringVar()
		self.f3t3.set("")
		self.f3z3=Tkinter.Entry(self.frame1,textvariable=self.f3t3,width=10)
		self.f3z3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)




		f3l4=Tkinter.Label(self.frame1, text="INTERFACE:",height=2,anchor="e")
		f3l4.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.commande="netstat -i | cut -d' ' -f1 |grep [0-9]$"
		self.t=int(commands.getoutput(self.commande+"|grep [0-9]$ -c"))
		self.init=0
		self.mes_interfaces=[]
		self.mes_interfaces.append("")
		for self.init in range (1,self.t+1):

			self.item=commands.getoutput(self.commande+"|sed -n "+str(self.init)+"p")
			self.mes_interfaces.append(self.item)
		
		
		self.mes_interfaces=tuple(self.mes_interfaces)
		self.inter_sel=Tkinter.StringVar()
		self.inter_sel.set("")
		self.ma_liste=ttk.Combobox(self.frame1, textvariable = self.inter_sel,values = self.mes_interfaces, state = 'readonly')
		self.inter_sel.set(self.mes_interfaces[0])
		self.ma_liste.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx="5")

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)

		x=(x+1)%2
		x=(x+1)%2
		y=(y+1)
		

		## CREATION DES BOUTONS LANCER ET STOPPER
		self.f4b1 = Tkinter.Button(self.frame1,text="START",command=self.OnButtonLaunch,relief=Tkinter.RAISED)
		self.f4b1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)


		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f4b2 = Tkinter.Button(self.frame1,text="STOP",command=self.OnButtonStop,relief=Tkinter.RAISED)
		self.f4b2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		self.f4b2.config(state=Tkinter.DISABLED)

		

		##LES INFO BULLES POUR GUIDER L'UTILISATEUR   (pierjean sur le forum Developpez.net)
 
		infoBulle_class.infoBulle(parent=self.f1z1,texte="LEAVE BLANK TO USE YOUR OWN IP ADDRESS")
		infoBulle_class.infoBulle(parent=self.f2z1,texte="THE DESTINATION IP ADDRESS IS MANDATORY")
		infoBulle_class.infoBulle(parent=self.f2z2,texte="THE PORT OF DESTINATION IS MANDATORY")
		infoBulle_class.infoBulle(parent=self.f3z3,texte="LEAVE EMPTY TO SEND PACKETS WITHOUT INTERRUPTION")
		infoBulle_class.infoBulle(parent=self.ma_liste,texte="CHOOSE THE INTERFACE TO SEND THE PACKETS \n LEAVE EMPTY TO USE ONE OF THE FREE INTERFACES OF YOUR MACHINE")

		##CREATION DE LA ZONE DE TEXTE POUR LE LOG DE L'EXECUTION DU PROGRAMME

		self.f4b3 = Tkinter.Button(self.frame2,text="CLEAR",command=self.OnButtonClear,relief=Tkinter.RAISED)
		self.f4b3.pack(side=Tkinter.BOTTOM)

		self.monlog=Tkinter.Text(self.frame2,width=65,height=15)
		self.monlog.pack(side=Tkinter.LEFT)
		self.scroll_bar=Tkinter.Scrollbar(self.frame2)
		self.scroll_bar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
		self.scroll_bar.config(command=self.monlog.yview)
		self.monlog.config(yscrollcommand=self.scroll_bar.set)
		self.add_timestamp()
		
		
		## CREATION DE LA BARRE DE MENU
		self.Barre_Menu=Tkinter.Menu(self)
		self.col1=Tkinter.Menu(self.Barre_Menu,tearoff=0)
		self.col1.add_command(label="Save Settings",command=self.info_box)
		self.col1.add_separator()
		self.col1.add_command(label="Quit",command=self.quit)
		self.Barre_Menu.add_cascade(label="File",menu=self.col1)
	
		self.col2=Tkinter.Menu(self.Barre_Menu)
		self.col2.add_command(label="Load Default Settings",command=self.charger_default)
		self.col2.add_command(label="Load Settings from a file",command=self.info_box)
		self.Barre_Menu.add_cascade(label="Edition",menu=self.col2)

		self.col3=Tkinter.Menu(self.Barre_Menu)
		self.col3.add_command(label="Help",command=self.info_box)
		self.col3.add_command(label="ABout",command=self.info_box)
		self.Barre_Menu.add_cascade(label="?",menu=self.col3)
		
		self.config(menu=self.Barre_Menu)
		sys.stdout=Log_class.Log(self.monlog)
		sys.stderr=Log_class.Log(self.monlog)

		monlog_content=len(self.monlog.get("1.0","end"))

	def scroll_text(self,event):
		self.monlog.see("end")
		print ("Modification")

	def add_timestamp(self):
		
		
		if len(self.monlog.get("1.0","end")) > self.monlog_content :
			self.monlog.see("end")
		self.monlog_content=len(self.monlog.get("1.0","end"))
		self.after(100, self.add_timestamp)

	def charger_default(self):
		
		self.f1t1.set("")
		

	def ip_source_hover_in(self):
		print("IN")
	def ip_source_hover_out(self):
		print("OUT")		
	def OnButtonLaunch(self):
		print("STARTING THE ATTACK")
		if(verrou.locked()):
			print("\n ERROR LAUNCHING THE ATTACK, ANOTHER ATTACK IN PROGRESS DETECTED")
		else:
			self.attack=ma_thread_tcp_syn.tcp_syn(self.f1t1.get(),"",self.f2t1.get(),self.f2t2.get(),"","",self.f3t3.get(),self.ma_liste.get())
			self.attack.start()
		self.f4b2.config(state=Tkinter.NORMAL)
		

	def OnButtonStop(self):
		
		
		self.attack.stop()
		self.f4b2.config(state=Tkinter.DISABLED)
		print("TRYING TO STOP A POSSIBLE PREVIOUS ATTACK") 	

	def thread_check(self):
		self.attack.stop()
		while (1==1):
			if(self.attack.isAlive()):
				self.f4b1.config(state=Tkinter.DISABLED)
			else:
				self.f4b2.config(state=Tkinter.NORMAL)
			time.sleep(0.5)

	def OnButtonClear(self):
		
		self.monlog.delete(0.0,Tkinter.END)
		self.monlog_content=0

	def message_box(self):
		#self.attack.stop()
		#print("VERIFICATION VOUS VOUS VRAIMENT FAIRE CELA")
		showinfo("MESSAGE","NOT AVAILABLE")	

	def info_box(self):
		print("NOT AVAILABLE")

	

	
