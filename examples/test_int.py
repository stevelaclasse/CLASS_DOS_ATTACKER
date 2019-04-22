nb=raw_input("Entrez un Entier: ")
def is_valid_int(nb):    
	try:
		int(nb)
		return True
	except ValueError:
		return False

print is_valid_int(nb)
