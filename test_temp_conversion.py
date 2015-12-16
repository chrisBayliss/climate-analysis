from temp_conversion import fahr_to_kelvin
from temp_conversion import fahr_to_celsius
def test_non_negative_kelvin():
	assert fahr_to_kelvin(0)>=0, "kelvin must be non-negative"
	
def test_fahro():
	#print(fahr_to_celsius(0)+","+(160/9))
	assert fahr_to_celsius(0)==(-160/9),"fahr 0 test"