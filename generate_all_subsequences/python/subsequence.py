#################################################################################################
#Recursive implementation for generating all possible subsequences of a list of numbers
#Time Complexity: O (2^N)
#################################################################################################

ssList = [];
def subsequences (array, currentPos, currentSeq):
	if (currentPos >= len (array)):
		#print (currentSeq);
		ssList.append (currentSeq);
		return;

	subsequences (array, currentPos + 1, currentSeq + [array [currentPos]]);
	subsequences (array, currentPos + 1, currentSeq);

if (__name__ == '__main__'):
	arr = [int (i) for i in input ().split ()];
	subsequences (arr, 0, []);
	for seq in ssList: print (seq);