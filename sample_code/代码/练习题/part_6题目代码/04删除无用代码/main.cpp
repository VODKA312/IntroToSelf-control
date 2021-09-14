#include <iostream>
#include <vector>
#include <ctime>
#include "matrix_addition.h"
#include "matrix_addition_improved.h"


using namespace std;

int main(int argc, const char * argv[]) {
    
    vector< vector<int> > matrixa = {
        {7, 1, 2, 3},
        {6,5,9,0},
        {17, 5, 2, 9},
        {5, 8, 9, 1}
        
    };
    
    vector< vector<int> > matrixb = {
        {11, 61, 5, 2},
        {4, 9, 5, 1},
        {16, 2, 7, 8},
        {2, 4, 1, 16}
    };
    
    vector< vector<int> > matrixsum;
    vector< vector<int> > matrixsum_improved;
    int iterations = 1000000;
    
    std::clock_t start;
    double duration;
 
    start = std::clock();
    for (int i = 0; i < iterations; i++) {
        matrixsum = matrix_addition(matrixa, matrixb);
    }
    
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    cout << "duration milliseconds matrix addition: " << 1000 * duration << '\n';

    start = std::clock();
    for (int i = 0; i < iterations; i++) {
        matrixsum_improved = matrix_addition_improved(matrixa, matrixb);
    }
    
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    cout << "duration milliseconds matrix addition improved: " << 1000 * duration << "\n\n";

    cout << "matrix addition sum: " << "\n";
    for (int i = 0; i < matrixsum.size(); i++) {
        for (int j = 0; j < matrixsum.size(); j++) {
            cout << matrixsum[i][j] << " ";
        }
        cout << "\n";
    }
	
  	cout << "\n";
    cout << "matrix addition sum: " << "\n";
    for (int i = 0; i < matrixsum_improved.size(); i++) {
        for (int j = 0; j < matrixsum_improved.size(); j++) {
            cout << matrixsum_improved[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}