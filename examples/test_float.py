nb=raw_input("Entrez un Decimal: ")
def is_valid_float(nb):    
	try:
		float(nb)
		return True
	except ValueError:
		return False

print is_valid_float(nb)