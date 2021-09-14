#include "initializer.hpp"

using namespace std;

vector < vector<int> > initializer(int rows, int cols, int initial_value) {
    
    vector <vector<int> > matrix(rows, vector<int>(cols, initial_value));
    return matrix;
    
}
