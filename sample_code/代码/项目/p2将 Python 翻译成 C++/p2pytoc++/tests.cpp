#include <iostream>
#include <vector>
#include "simulate.h"
#include "debugging_helpers.h"
#include "helpers.h"
#include "localizer.h"
//#include "../maps/half_text.txt"
//#include "../maps/m1.txt"
//#include "../maps/m2.txt"

using namespace std;

bool test_normalize() {
	vector < vector <float> > unnormalized, normalized, result;
	unnormalized = zeros(2, 2);
	normalized = zeros(2, 2);

	int i, j;

	for (i = 0; i<2; i++) {
		for (j = 0; j<2; j++) {
			unnormalized[i][j] = 1.0;
			normalized[i][j] = 0.25;
		}
	}

	result = normalize(unnormalized);

	bool correct;
	correct = close_enough(normalized, result);

	if (correct) {
		cout << "! - normalize function worked correctly!\n";
	}
	else {
		cout << "X - normalize function did not work correctly.\n";
		cout << "For the following input:\n\n";
		show_grid(unnormalized);
		cout << "\nYour code returned the following:\n\n";
		show_grid(result);
		cout << "\nWhen it should have returned the following:\n";
		show_grid(normalized);
	}
	return correct;
}

bool test_blur() {
	vector < vector <float> > in, correct, out;
	in = zeros(3, 3);
	correct = zeros(3, 3);

	in[1][1] = 1.0;

	float corner = 0.01;
	float side = 0.02;
	float center = 0.88;

	correct[0][0] = corner;
	correct[0][1] = side;
	correct[0][2] = corner;

	correct[1][0] = side;
	correct[1][1] = center;
	correct[1][2] = side;

	correct[2][0] = corner;
	correct[2][1] = side;
	correct[2][2] = corner;

	out = blur(in, 0.12);

	bool right;
	right = close_enough(correct, out);

	if (right) {
		cout << "! - blur function worked correctly!\n";
	}
	else {
		cout << "X - blur function did not work correctly.\n";
		cout << "For the following input:\n\n";
		show_grid(in);
		cout << "\nYour code returned the following:\n\n";
		show_grid(out);
		cout << "\nWhen it should have returned the following:\n";
		show_grid(correct);
	}

	return right;
}

bool test_helpers() {
	bool correct = true;
	bool question_correct;

	question_correct = test_normalize();
	if (!question_correct) {
		correct = false;
	}

	cout << endl;

	question_correct = test_blur();
	if (!question_correct) {
		correct = false;
	}
	return correct;

}


bool test_initialize() {
	vector < vector <char> > map;
	map = read_map("maps/m1.txt");
	int h = map.size();

	if (h < 1) {
		cout << "failed to load map. Make sure there is a maps/ directory in the same directory as this file!\n";
		return false;
	}

	vector < vector <float> > beliefs, correct;
	beliefs = initialize_beliefs(map);

	int w, A;
	float belief;

	w = map[0].size();
	A = h * w;
	belief = 1.0 / A;

	int i, j;
	vector <float> row;
	for (i = 0; i<map.size(); i++) {
		row.clear();
		for (j = 0; j<map[0].size(); j++) {
			row.push_back(belief);
		}
		correct.push_back(row);
	}

	bool right = close_enough(correct, beliefs);

	if (right) {
		cout << "! - initialize_beliefs function worked correctly!\n";
	}
	else {
		cout << "X - initialize_beliefs function did not work correctly.\n";
		cout << "For the following input:\n\n";
		show_grid(map);
		cout << "\nYour code returned the following:\n\n";
		show_grid(beliefs);
		cout << "\nWhen it should have returned the following:\n";
		show_grid(correct);
	}

	return right;

}

bool test_move() {
	vector < vector <float> > in, out, correct;
	in = zeros(3, 3);
	in[2][2] = 1.0;

	int dx, dy;
	dx = 1;
	dy = 1;
	float blurring = 0.0;

	correct = zeros(3, 3);
	correct[0][0] = 1.0;

	out = move(dy, dx, in, blurring);

	bool right = close_enough(correct, out);

	if (right) {
		cout << "! - move function worked correctly with zero blurring\n";
	}
	else {
		cout << "X - move function did not work correctly.\n";
		cout << "When dx=1, dy=1, blurring=0.0 and with\nthe following beliefs:\n\n";
		show_grid(in);
		cout << "\nYour code returned the following:\n\n";
		show_grid(out);
		cout << "\nWhen it should have returned the following:\n";
		show_grid(correct);
	}
	return right;
}

bool test_sense() {
	vector < vector <float> > in, out, correct;
	in = zeros(4, 2);

	int i, j;
	for (i = 0; i<in.size(); i++)
	{
		for (j = 0; j<in[0].size(); j++) {
			in[i][j] = 1.0 / 8.0;
		}
	}

	char color = 'r';
	vector < vector <char> > map;
	map = read_map("maps/half_red.txt");
	float p_hit, p_miss;
	p_hit = 2.0;
	p_miss = 1.0;

	out = sense(color, map, in, p_hit, p_miss);
	float total = 0.0;

	for (i = 0; i<out.size(); i++)
	{
		for (j = 0; j<out[0].size(); j++) {
			total += out[i][j];
		}
	}

	bool right = true;
	if ((total < 0.99) || (total > 1.01)) {
		right = false;
	}

	if ((out.size() != in.size()) || out[0].size() != in[0].size()) {
		right = false;
		cout << "X - sense function not working correctly.\n";
		cout << "Your function returned a grid with incorrect dimensions.\n";
		return right;
	}

	float r_prob, g_prob, r_exp, g_exp;
	r_prob = out[0][0];
	g_prob = out[0][1];

	r_exp = 1.0 / 6.0;
	g_exp = 1.0 / 12.0;

	if (close_enough(r_prob, r_exp) && close_enough(g_prob, g_exp)) {
		cout << "! - sense function worked correctly\n";
		return false;
	}
	else {
		cout << "X - sense function did not work correctly.\n";
		cout << "When p_hit=2.0, p_miss=1.0 and with\nthe following beliefs:\n\n";
		show_grid(in);
		cout << "\nYour code returned the following:\n\n";
		show_grid(out);
		cout << "\nbut this is incorrect.\n";
	}
	return right;
}

bool test_localizer() {
	bool correct = true;
	bool question_correct;

	question_correct = test_initialize();
	if (!question_correct) {
		correct = false;
	}
	if (!correct) {
		// map could not be loaded
		return false;
	}

	cout << endl;

	question_correct = test_move();
	if (!question_correct) {
		correct = false;
	}

	cout << endl;

	question_correct = test_sense();
	if (!question_correct) {
		correct = false;
	}
	return correct;
}

// bool test_simulation() {
//     // todo 
// }

//int main() {
//	cout << endl;
//	test_helpers();
//	test_localizer();
//	cout << endl;
//	return 0;
//}