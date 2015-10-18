#An Infix to Postfix Expression converter using the Stack Data Structure
#the function needs to be supplied with 1 argument: the string which is your expression
#format of the expression:
#	The expression must begin with an opening bracket (the main bracket) and end with a closing bracket (the main one)
#	Number of open brackets = Number of Closing brackets
#	Use the circular brackets
#examples:
#	a = '(a+(b*c))';
#	b = '((a+b)*(z+x))';
#	c = '((a+t)*((b+(a+c))^(c+d)))';

def infix_to_postfix (expression):
	current = '(';
	stack, expression = [current], expression [1 : ];

	while (expression):
		current, expression = expression [0], expression [1 : ];
		if (current == ')'):
			right, operator, left, opening_bracket = stack.pop (), stack.pop (), stack.pop (), stack.pop ();
			current = left + right + operator;
		stack.append (current);
	return (stack [0]);

#SAMPLE CALL TO FUNCTION
print (infix_to_postfix ('((a+t)*((b+(a+c))^(c+d)))'))
