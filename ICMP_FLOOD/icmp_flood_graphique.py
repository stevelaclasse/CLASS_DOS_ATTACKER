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
import ma_thread_icmp_flood
import Log_class
import infoBulle_class
from scapy.all import *
	

class test_fenetre(Tkinter.Tk):
	
	monlog_content=0
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
		global verrou
		verrou=threading.Lock()
		#self.attack=ma_thread_icmp_flood.icmp_flood(self.f1t1.get(),self.f1t1_1.get(),self.f1t2.get(),self.f1t3.get(),self.f3t2.get(),self.f3t3.get(),self.f3t4.get())
		self.attack=ma_thread_icmp_flood.icmp_flood(self.f1t1.get(),self.f1t1_1.get(),self.f1t2.get(),self.f1t3.get(),"",self.f3t3.get(),self.ma_liste.get(),int(self.bande.get()))
		if os.getuid() != 0: 
    			showerror("ERROR ACCESS RIGHTS"," you must run this program as an administrator")
    			sys.exit(1)
		
		


	def initialize(self):
		self["bg"]="green"
	
		self.frame1=Tkinter.Frame(self,borderwidth=2,width=100,height=100,relief=Tkinter.GROOVE)
		#self.frame1.pack()
		self.frame1.grid(column=0,row=0,sticky="EW",pady=10,padx=30)

		self.frame1.master.rowconfigure(0, weight=1)
		self.frame1.master.columnconfigure(0, weight=1)
		self.frame1.rowconfigure(0, weight=1)
		self.frame1.columnconfigure(0, weight=1)


		self.frame2=Tkinter.LabelFrame(self,text="LOGS DISPLAY",borderwidth=2,height=10,relief=Tkinter.GROOVE)
		#self.frame1.pack()
		self.frame2.grid(column=0,row=1,pady=10,padx=30)

		self.frame2.master.rowconfigure(0, weight=1)
		self.frame2.master.columnconfigure(0, weight=1)
		self.frame2.rowconfigure(0, weight=1)
		self.frame2.columnconfigure(0, weight=1)

		
		##variable de colonnes et lignes
		x=0
		y=0

		#REMPLISSAGE DU PANNEAU CONCERNANT L'ORDINATEUR ATTAQUANT
		f1t1=Tkinter.Label(self.frame1,text="ATTACK INFORMATIONS:",height=5,fg="blue",anchor="w")
		f1t1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
		

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		y=(y+1)
		self.f1l1=Tkinter.Label(self.frame1, text="IP ADDRESSES TO ATTACK:",height=2,width=25,anchor="e")
		self.f1l1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f1t1=Tkinter.StringVar()
		self.f1t1.set("")
		self.f1z1=Tkinter.Entry(self.frame1,textvariable=self.f1t1,width=30)
		self.f1z1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		self.f1z1.bind("<Enter>",self.ip_source_hover_in)
		self.f1z1.bind("<Leave>",self.ip_source_hover_out)
		x=(x+1)%2
		y=y+1

		y=(y+1)
		self.f1l1_1=Tkinter.Label(self.frame1, text="MAC ADDRESSES TO ATTACK:",height=2,width=25,anchor="e")
		self.f1l1_1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f1t1_1=Tkinter.StringVar()
		self.f1t1_1.set("")
		self.f1z1_1=Tkinter.Entry(self.frame1,textvariable=self.f1t1_1,width=30)
		self.f1z1_1.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		self.f1z1_1.bind("<Enter>",self.ip_source_hover_in)
		self.f1z1_1.bind("<Leave>",self.ip_source_hover_out)
		x=(x+1)%2
		y=y+1		
	
		self.f1l2=Tkinter.Label(self.frame1, text="USURPED IP ADDRESS:",height=2,anchor="e")
		self.f1l2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f1t2=Tkinter.StringVar()
		self.f1t2.set("")
		self.f1z2=Tkinter.Entry(self.frame1,textvariable=self.f1t2,width=30)
		self.f1z2.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)	

		self.f1l3=Tkinter.Label(self.frame1, text="USURPED MAC ADDRESS:",height=2,anchor="e")
		self.f1l3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		self.f1t3=Tkinter.StringVar()
		self.f1t3.set("")
		self.f1z3=Tkinter.Entry(self.frame1,textvariable=self.f1t3,width=30)
		self.f1z3.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		y=(y+1)	
		
		self.plt=Tkinter.Label(self.frame1, text="PAYLOAD DATA SIZE:",height=2,anchor="e")
		self.plt.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		x=(x+1)%2
		#self.f3t2=Tkinter.StringVar()
		#self.f3t2.set("")
		#self.f3z2=Tkinter.Entry(self.frame1,textvariable=self.f3t2,width=20)
		self.bande = Tkinter.Scale(self.frame1,orient='horizontal', showvalue=1,length=245, from_=0, to=65507)
		self.bande.grid(column=x,row=y,sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W,padx=5)

		self.frame1.master.rowconfigure(y, weight=1)
		self.frame1.master.columnconfigure(x, weight=1)
		self.frame1.rowconfigure(y, weight=1)
		self.frame1.columnconfigure(x, weight=1)

		#self.f3z2.grid(column=x,row=y,sticky="W",padx=5)
		x=(x+1)%2
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
		x=(x+1)%2
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
 
		#info_bulle=Tix.Balloon()
		#info_bulle.bind_widget(f1z1,msg="LAISSER VIDE POUR UTILISER VOTRE PROPRE ADRESSE IP")
		infoBulle_class.infoBulle(parent=self.f1z1,texte="SEPARATE IP ADDRESSES BY ';' OR USE THE '-' TO INDICATE AN IP RANGE \n SPECIFY A OR B OR C FOR CLASSES A, B OR C. EXAMPLE: 192.168.11.3-192.168.11.8 C \n ADDRESS OF THE MACHINE THAT WOULD NOT JOIN THE TARGET MACHINE \n IF YOU LEAVE THIS EMPTY FIELD, ALL NETWORK WILL BE TAKEN FOR TARGET")
		
		infoBulle_class.infoBulle(parent=self.f1z1_1,texte="MAC ADDRESS OF IP ADDRESS TO ATTACK \n YOU CAN LEAVE THIS MAC ADDRESS FIELD AND THE FOLLOWING EMPTY, \n BUT IN THIS CASE YOUR MAC ADDRESS WILL BE VISIBLE DURING THE NETWORK ANALYSIS \n HOWEVER IF YOU LET THIS FIELD EMPTY BUT COMPLETE THE FOLLOWING, \n IF THE MACHINE IS IN YOUR SUB-NETWORK, THEN THIS FIELD WILL INCLUDE ITS MAC ADDRESS, \n OTHERWISE THE BROADCAST MAC ADDRESS")		

		infoBulle_class.infoBulle(parent=self.f1z2,texte="SPECIFY THE IP ADDRESS THAT WOULD BE INCLUDED IN THE PACKETS SENT \n IF YOU LEAVE THIS FIELD EMPTY, YOUR IP ADDRESS WILL BE USED")
		infoBulle_class.infoBulle(parent=self.f1z3,texte="SPECIFY THE MAC ADDRESS THAT WOULD BE INCLUDED IN THE PACKETS SENT \n IF YOU LEAVE THIS FIELD EMPTY, YOUR MAC ADDRESS WILL BE USED")

		infoBulle_class.infoBulle(parent=self.f3z3,texte="LEAVE EMPTY TO SEND PACKAGES WITHOUT INTERRUPTION")

		infoBulle_class.infoBulle(parent=self.ma_liste,texte="CHOOSE THE INTERFACE TO SEND THE PACKETS \n LEAVE EMPTY TO USE ONE OF THE FREE INTERFACES OF YOUR MACHINE")
		
		infoBulle_class.infoBulle(parent=self.bande,texte="MOVE TO THE RIGHT TO ADD DATA (PAYLOAD) TO PACKET TO BE SENT \n (FOR MORE SATURATION OF THE NETWORK)")
		##CREATION DE LA ZONE DE TEXTE POUR LE LOG DE L'EXECUTION DU PROGRAMME

		self.f4b3 = Tkinter.Button(self.frame2,text="CLEAR",command=self.OnButtonClear,relief=Tkinter.RAISED)
		self.f4b3.pack(side=Tkinter.BOTTOM)

		self.monlog=Tkinter.Text(self.frame2,width=75,height=15)

		self.monlog.pack(side=Tkinter.LEFT)
		#self.monlog.insert(Tkinter.END,"BONJOUR LES TESTS")
		self.scroll_bar=Tkinter.Scrollbar(self.frame2)
		self.scroll_bar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
		self.scroll_bar.config(command=self.monlog.yview)
		self.monlog.config(yscrollcommand=self.scroll_bar.set)
		self.add_timestamp()

		

		#self.scroll_bar.grid(column=1,row=0)
		
		
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
		
		#if len(self.monlog.get("1.0","end"))%2 == 0:
		if len(self.monlog.get("1.0","end")) > self.monlog_content :
			#print(self.monlog_content)
			self.monlog.see("end")
      		  	#self.monlog.config(bg='red')
   		#else:
      		#  	self.monlog.config(bg='blue')
		#self.monlog.insert("end", time.ctime() + "\n")
		#self.monlog.see("end")
		self.monlog_content=len(self.monlog.get("1.0","end"))
		self.after(100, self.add_timestamp)

	def charger_default(self):
		
		self.f1t1.set("")
		#self.f3t1.set("1-1000000")
		#self.f2l1.config(fg="red")
		#self.f2l2.config(fg="red")
		

	def ip_source_hover_in(self):
		print("IN")
	def ip_source_hover_out(self):
		print("OUT")		
	def OnButtonLaunch(self):
		#self.f2l1.config(fg="black")
		#self.f2l2.config(fg="black")
		print("STARTING THE ATTACK")
		#self.labelVariable.set("Vous avez clique sur le button")
		#self.labelVariable.set(self.entryVariable.get()+"Vous avez cliquez sur le button")
		#attack=tcp_syn(self.f1t1.get(),self.f1t2.get(),self.f2t1.get(),self.f2t2.get(),self.f3t1.get(),self.f3t2.get(),self.f3t3.get(),self.f3t4.get())
		#attack.start()
		if(verrou.locked()):
			print("\n ERROR LAUNCHING THE ATTACK, ANOTHER ATTACK IN PROGRESS DETECTED")
		#print("Vous avez clique sur le button lancer")
		#self.labelVariable.set("Vous avez clique sur le button")
		#self.labelVariable.set(self.entryVariable.get()+"Vous avez cliquez sur le button")
			#self.attack=True
		else:
			#self.attack=ma_thread_icmp_flood.icmp_flood(self.f1t1.get(),self.f1t1_1.get(),self.f1t2.get(),self.f1t3.get(),self.f3t2.get(),self.f3t3.get(),self.f3t4.get())
			self.attack=ma_thread_icmp_flood.icmp_flood(self.f1t1.get(),self.f1t1_1.get(),self.f1t2.get(),self.f1t3.get(),"",self.f3t3.get(),self.ma_liste.get(),int(self.bande.get()))
			#self.attack.stop()
			self.attack.start()
			#print("thread_alive="+str(self.thread_alive))
		#self.f4b1.config(state=Tkinter.DISABLED)
		self.f4b2.config(state=Tkinter.NORMAL)
		

	def OnButtonStop(self):
		
		#print("Tentative d'arret d'envoi des paquet")
		self.attack.stop()
		self.f4b2.config(state=Tkinter.DISABLED)
		#while(self.attack.isAlive()):
		#	time.sleep(0,2)
		#print("Vous avez clique sur le button arreter")
		print("TRYING TO STOP A POSSIBLE PREVIOUS ATTACK")
		#self.labelVariable.set("Vous avez clique sur le button")
		#self.labelVariable.set(self.entryVariable.get()+"Vous avez cliquez sur le button")	

	def OnButtonClear(self):
		
		self.monlog.delete(0.0,Tkinter.END)
		self.monlog_content=0

	def message_box(self):
		#print("VERIFICATION VOUS VOUS VRAIMENT FAIRE CELA")
		showinfo("MESSAGE","NOT AVAILABLE")	

	def info_box(self):
		print("NOT AVAILABLE")

	

	
