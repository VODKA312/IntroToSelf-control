#include "scalar_multiply_improved.hpp"
using namespace std;

vector< vector<int> > scalar_multiply_improved(vector< vector<int> > matrix, int scalar) {
    
    vector<int>::size_type num_rows = matrix.size();
    vector<int>::size_type num_cols = matrix[0].size();
    
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            matrix[i][j] = matrix[i][j] * scalar;
        }
    }
    
    return matrix;
}
