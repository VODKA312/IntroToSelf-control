# References Exercise

The code in this exercise is the same as the "Dead Code" exercise. A matrix addition function has already beeen written for you and placed in both the matrix_addition.cpp and matrix_addition_improved.cpp file.

Your task is to modify the code in matrix_addition_improved.cpp, passing the variables by reference. You'll also have to modify the function definition in matrix_addition_improved.hpp. 

This exercise is relatively simple. Your only task is to add the ampersand symbols in the correct place.

Here are your tasks:
1. Read through main.cpp and matrix_addition.cpp. The two files matrix_addition.cpp and matrix_addition_improved.cpp have the same code.

2. Run the code by opening a terminal window and typing the following commands:
cd /home/workspace/References
g++ -std=c++11 main.cpp matrix_addition.cpp matrix_addition_improved.cpp
./a.out

3. Modify the code in matrix_addition_improved.cpp and matrix_addition_improved.hpp. Add the & symbol where necessary to pass the variables in my reference. Remember, you must change the function declaration in .hpp if you change the function inputs in the .cpp file.

4. Run the code again using the following code in the terminal (this assume you are already inside the References folder in your terminal window)
g++ -std=c++11 main.cpp matrix_addition.cpp matrix_addition_improved.cpp
./a.out

5. See if your code got any faster. You can also check out a solution in solution.cpp and solution.hpp