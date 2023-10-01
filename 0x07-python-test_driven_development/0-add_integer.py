
""" Integer Addition funtion
	a and b are two real values
"""

def add_integers(a, b = 98):
	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))
