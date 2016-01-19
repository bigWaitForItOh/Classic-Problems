#################################################################################################################
#Telephone Words Problem (Pg. 100, Programming Interviews Exposed)
#Displays all 3**7 = 2187 possible strings formed from the 7 digit telephone number
#Time Complexity: O(3^N)
#	where N = number of digits in telephone number. Since in this problem, N = 7 always, complexity = 3**7 = 2187 = O(1)
#Space Complexity: O(3^N)
#	where N = number of digits in telephone number. Since in this problem, N = 7 always, complexity = 3**7 = 2187 = O(1)
#################################################################################################################

def get_char_key (digit, pos):
	chars = {
		1 : '',
		2 : 'ABC',
		3 : 'DEF',
		4 : 'GHI',
		5 : 'JKL',
		6 : 'MNO',
		7 : 'PQR',
		8 : 'STU',
		9 : 'VWX',
		0 : 'YZ'
	}
	return (chars [digit] [pos-1]);

def strings (number, digit_pos, string):
	global results;
	if (digit_pos < 0):
		print (string);
		return;

	current_digit = (number // 10**digit_pos) % 10;
	for i in range (1, 4):
		string [6-digit_pos] = get_char_key (current_digit, i);
		strings (number, digit_pos-1, string);
		string [6-digit_pos] = None;


def get_strings (number):
	strings (number, 6, [None for i in range (7)]);

if (__name__ == '__main__'):
	get_strings (int (input ()));