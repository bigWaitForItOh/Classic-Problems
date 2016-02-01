####################################################################################################
#A Pseudo Polynomial dynamic Programming Implementation for generating the Nth Bell Number
#Time Complexity: O (N^2)
#Space Complexity: O (N^2)
#This implementation is effiecient in case there are multiple queries. If Bell number is already
#present for for given query N, then Time Complexity = (1). O (N^2) is in case the table has to be
#constructed from the start up to N
####################################################################################################

triangle = {0 : [1]};

def build (triangle, number):
	for i in range (max (triangle)+1, number+1):
		triangle [i] = [triangle [i-1] [-1]];
		for j in range (0, i-1):
			triangle [i].append (triangle [i] [j] + triangle [i-1] [j]);

def bell (number):
	if (number == 0):
		return (1);

	if (not number in triangle):
		build (triangle, number);
	return (triangle [number] [-1]);

n = int (raw_input ());
print (bell (n));