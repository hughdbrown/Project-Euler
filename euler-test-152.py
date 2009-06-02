import decimal
x = [2,3,4,5,7,12,15,20,28,35]
y = [1/(decimal.Decimal(str(xx)) * decimal.Decimal(str(xx))) for xx in x]
half = decimal.Decimal("0.5")
print sum(y), half
print sum(y) == half
