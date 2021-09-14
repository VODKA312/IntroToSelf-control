#include <iostream>
#include <vector>
#include <ctime>

#include "scalar_multiply.hpp"
#include "scalar_multiply_improved.hpp"
#include "print.hpp"

using namespace std;

int main() {

    int num_rows = 10;
    int num_cols = 5;
    int initial_value = 20;
    
    vector< vector<int> > matrix(num_rows, vector<int>(num_cols, initial_value));
    vector< vector<int> > matrix_original(num_rows, vector<int>(num_cols, initial_value));
    vector< vector<int> > matrix_improved(num_rows, vector<int>(num_cols, initial_value));

    int iterations = 100000;
    
    std::clock_t start_one, start_two;
    double duration_one, duration_two;
    
    // nested for loop
    start_one = std::clock();
    
    for (int i = 0; i < iterations; i++) {
        matrix_original = scalar_multiply(matrix, 3);
    }
    
    duration_one = ( std::clock() - start_one ) / (double) CLOCKS_PER_SEC;
    
    start_two = std::clock();
    
    for (int i = 0; i < iterations; i++) {
        // TODO: Change the code in scalar_multiply_improved.cpp to avoid defining extra variables
        matrix_improved = scalar_multiply_improved(matrix, 3);
    }
    duration_two = ( std::clock() - start_two ) / (double) CLOCKS_PER_SEC;
    
    // print the matrices to the terminal
    cout << "matrix \n";
    print(matrix_original);
    cout << "matrix_improved \n";
    print(matrix_improved);
    
    // print the time results to the terminal
    cout << "duration milliseconds original code: " << 1000 * duration_one << '\n';
    cout << "duration milliseconds improved code: " << 1000 * duration_two << '\n';
    
    return 0;
}

