#import Sortie_class
import Tkinter
#class Log(Sortie_class.Sortie):
class Log(object):
	def __init__(self,mon_log_fictif):
	
		self.mon_log_fictif=mon_log_fictif
		'''A class for redirecting stdout to this Text widget.'''

	def write(self,str):
        	#self.text_area.insert(Tkinter.END,str)
		self.mon_log_fictif.insert(Tkinter.END,str)
		##self.terminal.write(str)
