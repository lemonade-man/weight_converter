units = {
    "g": 1,
    "kg": 1000,
    "lbs": 453.6
}

def convert(num, cFrom, cTo):
	num = int(num)
	return f"{(num*units[cFrom])/units[cTo]}{cTo}"
