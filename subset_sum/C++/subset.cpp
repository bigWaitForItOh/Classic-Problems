/*
	Subset Sum Problem - Determines whether a possible subset of the given set exists such that the sum of elements of the subset = target
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool subset_sum (int target, vector< int > numbers, int vector_size) {
	if (!target) {
		return (true);
	}
	if (!vector_size && target) {
		return (false);
	}
	return (subset_sum (target, numbers, vector_size - 1) || subset_sum (target - numbers [vector_size - 1], numbers, vector_size - 1));
}

int main () {
	vector< int > numbers;
	int target (0), size (0);

	cout << "Size: "; cin >> size;
	cout << "Numbers (space separated): ";
	for (int i = 0; i < size; i++) {
		int buf (0);
		cin >> buf;
		numbers.push_back (buf);
	}
	cout << "Target: "; cin >> target;

	cout << (subset_sum (target, numbers, numbers.size ()) ? "YES!" : "NO..") << endl;
	return (0);
}
