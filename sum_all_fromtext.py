import re
hand = open('regex_sum_294912.txt')
it = list()
sum = 0
for line in hand:
	line = line.rstrip()
	x = re.findall('[0-9]+',line)
	if len(x) > 0 :
		print x
		for i in x :
			sum = sum + int(i)
print sum
