from temp_conversion import fahr_to_kelvin
def test_non_negative_kelvin():
	assert fahr_to_kelvin(0)>=0, "kelvin must be non-negative"