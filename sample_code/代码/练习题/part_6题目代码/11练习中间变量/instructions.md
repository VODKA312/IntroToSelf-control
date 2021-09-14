# Intermediate Variables Exercise

In this exercise, you will see how inefficient it can be to use extra variables that you do not need. The main.cpp file times how long it takes to run two different functions: scalar_multiply() and scalar_multiply_improved().

Currently, both scalar_multiply.cpp and scalar_multiply_improved.cpp contain the exact same code. 

Here are the instructions for completing the exercise:
1. Take a look at main.cpp and scalar_multiply.cpp. Then open a new terminal and run the code using the following commands:
cd /home/workspace/IntermediateVariables
g++ main.cpp scalar_multiply.cpp scalar_multiply_improved.cpp print.cpp
./a.out

2. Both the scalar_multiply() function and scalar_multiply_improved() function should take about the same amount of time to run because they contain the same code. Execute ./a.out a few times to convince yourself that the duration is about the same.

3. Now, optimize the code in scalar_multiply_improved.cpp. Instead of creating a new matrix variable, update the input matrix values directly. (HINT: matrix[i][j] = matrix[i][j] * x)

4. Run the code again by typing ./a.out in the terminal window (make sure you are still in the IntermediateVariables folder in the terminal).

5. Did your code run faster? If you get stuck, check out the solution.cpp file inside the IntermediateVariables folder.