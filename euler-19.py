normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]

years = [ normal_year ] * 100
for i in range(3, len(years), 4) :
	years[i] = leap_year

current_day = (0+365) % 7
sundays = 0
for y in years :
	for m in y :
		if current_day % 7 == 6:
			sundays += 1
		current_day += m%7
print sundays

