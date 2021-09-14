# For Loops Exercise

The code in this exercises intitializes a 2D vector using nested for loops. For an m by n matrix, the nested for loops involve m * n operations. However, you can initialiaze the matrix in m + n operations.

Your task is to rewrite the code in initialize_matrix_improved.cpp so that the matrix gets initialized in m + n steps. 

The main.cpp runs both the initialize_matrix() function from initialize_matrix.cpp and the initialize_matrix_improved() function from initialize_matrix_improved.cpp. But currently, the two functions have the exact same code.

Here are the steps to complete the exercise:
1. First, double click on the "ForLoops" folder to explore the code. Then open a new terminal.
2. Run the code as is using the following commands
cd /home/workspace/ForLoops
g++ main.cpp initialize_matrix.cpp initialize_matrix_improved.cpp print.cpp
./a.out

3. The execution time for each function should be roughly the same because they contain the same code. You can run the ./a.out command a few times to convince yourself that the times are the same. Now, open the initialize_matrix_improved.cpp file and optimize the code. Try to initialize the matrix with m + n operations instead of m * n operations. (HINT: Think about what goes into the new_row variable.)

4. Run the code again using the following commands:
g++ main.cpp initialize_matrix.cpp initialize_matrix_improved.cpp print.cpp
./a.out

5. Has your execution time improved? If you get stuck, check out the file solution.cpp