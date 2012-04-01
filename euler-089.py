dd = { 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 
	10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
	100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM", 1000:"M"}
a = ["M", "D", "C", "L", "X", "V", "I"]
a2 = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
def romanToDecimal(s) :
	result = 0
	prev_index = -1
	i = 0
	while i < len(s) :
		c = s[i]
		j = a.index(c)
		if i != len(s)-1 :
			next = s[i+1]
			if a.index(next) < j :
				result += a2[next] - a2[c]
				i += 2
			else :
				result += a2[c]
				i += 1
		else :
			result += a2[c]
			i += 1
	return result

def decimalToRoman(d) :
	result = ""
	while d > 1000 :
		result += "M"
		d -= 1000
	hundreds = d - d%100
	if hundreds :
		result += dd[hundreds]
		d = d % 100

	tens = d - d%10
	if tens :
		result += dd[tens]
		d = d % 10

	if d :
		result += dd[d]
	return result

def test() :
	f = open("roman-89.txt")
	v = [ line.strip() for line in f.readlines() ]
	savings = 0
	for a in v:
		d = romanToDecimal(a)
		r = decimalToRoman(d)
		savings += len(a) - len(r)
	print savings

test()