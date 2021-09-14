//#pragma once
#ifndef LOCALIZER_H
#define LOCALIZER_H

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;

vector< vector <float> > initialize_beliefs(vector< vector <char> > grid);
vector< vector <float> > sense(char color, vector< vector <char> > grid, vector< vector <float> > beliefs, float p_hit, float p_miss);
vector< vector <float> > move(int dy, int dx, vector < vector <float> > beliefs, float blurring);

#endif /* LOCALIZER_H */
