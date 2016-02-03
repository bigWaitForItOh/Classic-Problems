###############################################################################################################
#Implementation of the Sliding Window Algorithm using heapq
#Worst Case Time Complexity: O (NK)
#N = number of items in array out of which, K smallest items are required
#NOTE: If duplicates exist in the given array and are amongst the smallest, they are counted as separate
#eg- Array = [5, 7, 2, 1, 2] K = 3
#Result = [1, 2, 2]
###############################################################################################################

from heapq import heapify, heappush, heappop;

def k_smallest (buffer, k):
	if (len (buffer) < k):
		return (None);

	heap = [-i for i in buffer [ : k]];
	position = k;

	heapify (heap);
	while (position < len (buffer)):
		current = buffer [position];
		if (-current > heap [0]):
			heappop (heap);
			heappush (heap, -current);
		position += 1;

	return ([-i for i in heap]);

if (__name__ == '__main__'):
	buffer = [int (i) for i in input ().split ()];
	k = int (input ());
	print (k_smallest (buffer, k));