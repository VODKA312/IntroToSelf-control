#include "print.hpp"

using namespace std;

void print(vector< vector<int> > matrix) {
    
    vector<int>::size_type nrows = matrix.size();
    vector<int>::size_type ncols = matrix[0].size();
    
    for (int i = 0; i < nrows; i++) {
        for (int j = 0; j < ncols; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
    
}
;

