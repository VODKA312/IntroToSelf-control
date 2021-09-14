# Instructions Vector Storage Exercise

In the VectorStorage folder, you'll find a program that initializes a 2D vector three different times. The first time uses a function called reserved(), the second time a function called unreserved(), and the third time uses a function called initializer().

You can find the definitions for these functions in their respective .cpp files. Your task is to modify the code in reserved.cpp to use the standard library vector reserve method. You'll see if this helps make the program run faster.

Here are the steps to complete
1. Look at the code files especially main.cpp, unreserved.cpp and initializer.cpp. 

2. Open a new terminal window and use the following commands to run the program:
cd /home/workspace/VectorStorage
g++ main.cpp reserved.cpp unreserved.cpp initializer.cpp print.cpp
./a.out

The program prints out the time it took to run each function.

You'll also notice that main.cpp has some code to print out the resulting matrices but this code is commented out. If you'd like to see a print out of the matrices, uncomment code lines 40 through 45. 

3. Modify the code in reserved.cpp to use the reserve method. If you a a vector variable called myvector, you use the reserve method with myvector.reserve(length);

4. Re-run the program using the following commands (make sure you are still inside the VectorStorage folder in the terminal window)
g++ main.cpp reserved.cpp unreserved.cpp initializer.cpp print.cpp
./a.out

5. Notice whether or not your changes made the code run faster. Execute ./a.out a few times to convince yourself whether or not the reserve() function code is running faster. You can see two different solutions in the solution1.cpp and solution2.cpp files. Solution2.cpp uses a technique you haven't seen yet for looping through a vector. This solution uses a special variable called an iterator. But the main point of solution2 is to see if reserving the inner vector of a 2D vector makes the code run faster or not.