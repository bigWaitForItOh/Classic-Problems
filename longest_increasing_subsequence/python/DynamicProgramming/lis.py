######################################################################################################################
#Dynamic Programming Solution of Longest Increasing Subsequence
#Time Complexity: O (N^2)
#Space Complexity: O (N)
######################################################################################################################

def max_len (array, aux_array, upper):
	result = 0;
	for i in range (upper):
		if (array [upper] > array [i]):
			if (aux_array [i] > result):
				result = aux_array [i];
	return (result);

def lis (array):
	aux_array = [None for i in range (len (array))];
	result = 0;

	aux_array [0] = 1;
	for i in range (1, len (array)):
		aux_array [i] = 1 + max_len (array, aux_array, i);
		if (aux_array [i] > result):
			result = aux_array [i];

	return (result);

if (__name__ == '__main__'):
	array = [int (i) for i in input ().split ()];
	print ('Length of the longest increasing subsequence is: %d' % (lis (array)));
