###################################################################################################################
#Recursive Implementation of the Subset Sum problem
###################################################################################################################

def subset_sum (target, elements, size):
	if (target == 0):
		return (True);
	if (size == 0 and target):
		return (False);

	return (subset_sum (target - elements [size - 1], elements, size - 1) or subset_sum (target, elements, size - 1));

if (__name__ == '__main__'):
	s_sum, elements = int (input ()), [int (i) for i in input ().split ()];
	s_sum_possible = subset_sum (s_sum, elements, len (elements));
	print (s_sum_possible);
