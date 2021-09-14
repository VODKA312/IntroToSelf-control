#include <iostream>
#include <vector>
#include <ctime>

#include "unreserved.hpp"
#include "reserved.hpp"
#include "initializer.hpp"
#include "print.hpp"

using namespace std;

int main() {
    
    int num_rows = 100000;
    int num_cols = 100;
    int initial_value = 2;
    
    vector< vector<int> > matrix_unreserved;
    vector< vector<int> > matrix_reserved;
    vector< vector<int> > matrix_initialized;
    
    std::clock_t start_one, start_two, start_three;
    double duration_one, duration_two, duration_three;
    
    // unreserved matrix
    start_one = std::clock();
    matrix_unreserved = reserved(num_rows, num_cols, initial_value);
    duration_one = ( std::clock() - start_one ) / (double) CLOCKS_PER_SEC;
    
    start_two = std::clock();
    matrix_reserved = unreserved(num_rows, num_cols, initial_value);
    duration_two = ( std::clock() - start_two ) / (double) CLOCKS_PER_SEC;
    
    start_three = std::clock();
    matrix_initialized = initializer(num_rows, num_cols, initial_value);
    duration_three = ( std::clock() - start_three ) / (double) CLOCKS_PER_SEC;

                                 
    // print the matrices to the terminal
//    cout << "matrix \n";
//    print(matrix_unreserved);
//    cout << "matrix_improved \n";
//    print(matrix_reserved);
//    cout << "matrix_improved \n";
//    print(matrix_initialized);

                                 
    // print the time results to the terminal
    cout << "duration milliseconds reserved: " << 1000 * duration_one << '\n';
    cout << "duration milliseconds unreserved: " << 1000 * duration_two << '\n';
    cout << "duration milliseconds initialized: " << 1000 * duration_three << '\n';

    return 0;
}


