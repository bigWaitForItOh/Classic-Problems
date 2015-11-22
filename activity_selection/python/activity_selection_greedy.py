######################################################################################################################
#Greedy Algorithm for Activity Selection Problem
######################################################################################################################

from heapq import heapify, heappush, heappop;
def activity_selection (activities):
	p_queue = [ (activities [i] [1], activities [i] [0], i) for i in activities ];
	heapify (p_queue);
	result = [heappop (p_queue) [2]];

	while (p_queue):
		datum = heappop (p_queue);
		if (datum [1] >= activities [result [-1]] [1]):
			result.append (datum [2]);

	return (result);

#Sample Argument to be passed to the function: A Dictionary with key => Name of the Activity, Value => A 2-Tuple (start time, end time)
activities = {
	'A' : (1, 2),
	'B' : (3, 4),
	'C' : (0, 6),
	'D' : (5, 7),
	'E' : (8, 9),
	'F' : (5, 9)
};

#sample call to activity_selection ()
#returns a list of the Maximum Activities (Names) you can do
max_act = activity_selection (activities);
print (max_act);
