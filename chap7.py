# Enter your answrs for chapter 7 here
# Name: Ethan Puzarne

from math import pi,factorial,sqrt
# Ex. 7.5

def estimate_pi():
	k = 0
	sum_total = 0.0
	current_item = 1.0
	pre_constant = 2 * sqrt(2)/9801

	while current_item > 1e-15:
		current_item = (float(factorial(4 * k) * (1103 + 26390*k)) / float((factorial(k)**4 * 396**(4*k))))
		#print(current_item)
		sum_total += current_item
		k+=1
		estimation = 1 / (pre_constant * sum_total)
		print(estimation)

	print pi


estimate_pi()



# How many iterations does it take to converge?
# Iterations:
# k=0 3.14159273001
# k=1 3.14159265359
# k=2 3.14159265359
# k=3 3.14159265359

# Pi:3.14159265359

# It takes 4 iterations for the next term in the sumation to be smaller than 1e-15
