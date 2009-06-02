
import decimal

exact = decimal.Decimal(3) / decimal.Decimal(7)
diff = decimal.Decimal(1)
for i in range(999*1000,1000*1000) :
	x = int((i * 3) / 7)
	if (3 * i) == (7 * x) :
		x -= 1
	y = decimal.Decimal(x) / decimal.Decimal(i)
	new_diff = exact - y
	if new_diff < diff : 
		diff, num, denom = new_diff, x, i
		print diff, num, denom
print diff, num, denom

