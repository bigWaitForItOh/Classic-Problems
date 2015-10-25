###############################################################################################
#A number is given in the form of a string and we are supposed to find the sum of all its substrings (which are also numbers)
#example: 16 = 16 + 1 + 6 = 23
#example: 123 = 123 + 1 + 2 + 3 + 12 + 23 = 164
###############################################################################################

def grand_total (string):
	total, mult = 0, 1;
	for i in range (len (string), 0, -1):
		total += int (string [i - 1]) * mult * i;
		mult = (mult * 10) + 1;

	return (total);		

print (grand_total (input ()));
