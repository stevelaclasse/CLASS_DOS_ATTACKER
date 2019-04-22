import re
address = raw_input( "MAC Address:" )

def is_valid_mac_address(address):
	if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", address.lower()):
		return True
	else:
		return False
	
print is_valid_mac_address(address)