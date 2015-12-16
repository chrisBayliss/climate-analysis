"""A library to perform temperature conversions"""

def test_non_negative_kelvin():
	assert fahr_to_kelvin(0)>=0, "kelvin must be non-negative"
	
#def test_kelvin

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard Fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius

def fahr_to_kelvin(fahr):
    """Convert Fahrenheight to Kelvin.

    Uses standard Fahrenheit to Kelvin formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
	
    return kelvin
