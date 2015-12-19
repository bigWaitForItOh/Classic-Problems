##############################################################################################################################
#Recursive implementation of Edit Distance Algorithm
#Time Complexity: O (3^m)
##############################################################################################################################

def edit_dist (x, y):
	if (not x):
		return (len (y));
	if (not y):
		return (len (x));

	if (x [-1] == y [-1]):
		return (edit_dist (x [ : -1], y [ : -1]));

	insert = edit_dist (x, y [ : -1]);
	remove = edit_dist (x [ : -1], y);
	replace = edit_dist (x [ : -1], y [ : -1]);

	return (1 + min (insert, remove, replace));

print (edit_dist (input (), input ()));
