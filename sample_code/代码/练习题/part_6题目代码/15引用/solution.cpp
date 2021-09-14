#include "blur_factor_improved.hpp"

using namespace std;

vector < vector <float> > blur_factor_improved() {
        
    // calculate blur factors
    static float blurring_improved = .12;
    static float center_improved = 1.0 - blurring_improved;
    static float corner_improved = blurring_improved / 12.0;
    static float adjacent_improved = blurring_improved / 6.0;
    
    //create the blur window
    static vector< vector<float> > window_improved = {
        {corner_improved, adjacent_improved, corner_improved},
        {adjacent_improved, center_improved, adjacent_improved},
        {corner_improved, adjacent_improved, corner_improved}
    };
    
    return window_improved;
}

