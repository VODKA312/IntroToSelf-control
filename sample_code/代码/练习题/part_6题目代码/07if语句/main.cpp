#include <iostream>
#include <vector>
#include <ctime>

#include "initialize_matrix.hpp"
#include "initialize_matrix_improved.hpp"

#include "print.hpp"

using namespace std;

int main(int argc, const char * argv[]) {

    vector< vector<int> > matrix;
    vector <vector<int> > matrix_improved;
    vector<int> new_row;

    int num_rows = 10;
    int num_cols = 5;
    int intitial_value = 5;
    int iterations = 100000;
    
    std::clock_t start_one, start_two;
    double duration_one, duration_two;

    // nested for loop
    start_one = std::clock();
    
    for (int i = 0; i < iterations; i++) {
        matrix = initialize_matrix(num_rows, num_cols, intitial_value);
    }
    
    duration_one = ( std::clock() - start_one ) / (double) CLOCKS_PER_SEC;

    start_two = std::clock();
    
    for (int i = 0; i < iterations; i++) {
        // TODO: Change the code in initialize_matrix_improved.cpp
        // The solution should not use nested for loops
        // HINT: Each row has the values {5, 5, 5, 5, 5}. Do you need to recreate that row multiple times?
        matrix_improved = initialize_matrix_improved(num_rows, num_cols, intitial_value);
    }
    duration_two = ( std::clock() - start_two ) / (double) CLOCKS_PER_SEC;

    // print the matrices to the terminal
    cout << "matrix \n";
    print(matrix);
    cout << "matrix_improved \n";
    print(matrix_improved);
    
    // print the time results to the terminal
    cout << "duration milliseconds original code: " << 1000 * duration_one << '\n';
    cout << "duration milliseconds improved code: " << 1000 * duration_two << '\n';

    return 0;
}
