import Sortie_class
import Tkinter
class Log(Sortie_class.Sortie):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert(Tkinter.END,str)
	#self.terminal.write(str)
