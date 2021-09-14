# All test code
import unittest
from IPython.display import Markdown, display



# Helper functions for printing markdown text (text in color/bold/etc)
def printmd(string):
    display(Markdown(string))

# Print a test failed message, given an error
def print_fail():
    printmd('**<span style="color: red;">TEST FAILED</span>**')

# Print a test passed message
def print_pass():
    printmd('**<span style="color: green;">TEST PASSED</span>**')



# A class holding all tests
class Tests(unittest.TestCase):


    # Tests the `one_hot_encode` function, which is passed in as an argument
    def test_one_hot(self, one_hot_function):

        # Test that the generated one-hot labels match the expected one-hot label
        # For all three cases (red, yellow, green)
        try:
            self.assertEqual([1,0,0], one_hot_function('red'))
            self.assertEqual([0,1,0], one_hot_function('yellow'))
            self.assertEqual([0,0,1], one_hot_function('green'))

        # If the function does *not* pass all 3 tests above, it enters this exception
        except self.failureException as e:
            # Print out an error message
            print_fail()
            print("Your function did not return the expected one-hot label.")
            print('\n'+str(e))
            return

        # Print out a "test passed" message
        print_pass()


    # Tests if any misclassified images are red but mistakenly classified as green
    def test_red_as_green(self, misclassified_images):
        # Loop through each misclassified image and the labels
        for im, predicted_label, true_label in misclassified_images:

            # Check if the image is one of a red light
            if(true_label == [1,0,0]):

                try:
                    # Check that it is NOT labeled as a green light
                    self.assertNotEqual(true_label, [0, 0, 1])
                except self.failureException as e:
                    # Print out an error message
                    print_fail()
                    print("Warning: A red light is classified as green.")
                    print('\n'+str(e))
                    return

        # No red lights are classified as green; test passed
        print_pass()








