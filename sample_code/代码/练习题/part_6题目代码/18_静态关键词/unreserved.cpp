#include "unreserved.hpp"

using namespace std;

vector< vector<int> > unreserved(int rows, int cols, int initial_value) {
    
    
    vector< vector<int> > matrix;
    vector<int> new_row;
    
    for (int i = 0; i < rows; i++) {
        new_row.clear();
        for (int j = 0; j < cols; j++) {
            new_row.push_back(initial_value);
        }
        matrix.push_back(new_row);
    }
    
    return matrix;
}
