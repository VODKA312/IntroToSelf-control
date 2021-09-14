#include <iostream>
#include <vector>
#include <ctime>
#include "blur_factor.hpp"
#include "blur_factor_improved.hpp"
#include "print.hpp"

using namespace std;

int main() {
    
    vector< vector<float> > window;
    vector< vector<float> > window_improved;
    int iterations = 1000000;
    
    std::clock_t start;
    double duration, duration_improved;
    
    start = std::clock();
    for (int i = 0; i < iterations; i++) {
        window = blur_factor();
    }

    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;

    start = std::clock();
    for (int i = 0; i < iterations; i++) {
        window_improved = blur_factor_improved();
    }

    duration_improved = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    
  	cout << "blur window \n";
    print(window);
  	cout << "\n blur_improved window \n";
    print(window_improved);
    
    cout << "duration milliseconds blur_factor: " << 1000 * duration << '\n';
    cout << "duration milliseconds blur_factor_improved: " << 1000 * duration_improved << "\n";
    
    return 0;
}

