#import time library to record execution
import time

#initialize a value that is equal to the current state of time.time()
start_time = time.time()

#create an array for potential Fibonacci sequence outputs
#array takes first two Fibonacci numbers as 0 & 1
FibArray = [0,1]

#define the Fibonacci sequence
def Fibonacci(n):
    #if n is less than or equal to 0, the program will return an error message
    if n<=0:
        print("Incorrect input")
    #if n is greater than 0 less than or equal to the length of the Fibonacci 
    #array (which is size 2), the program will return 1
    elif n<=len(FibArray):
        return FibArray[n-1]
    #if n is greater than 1, the program will compute the nth Fibonacci number
    else:
        #computes Fibonacci number
        temp_fib = Fibonacci(n-1)+Fibonacci(n-2)
        #appends (or "adds to") the array of Fibonacci numbers
        FibArray.append(temp_fib)
        #exits the loop by returning the nth Fibonacci number
        return temp_fib

#defined the last two numbers of my L-number
last_two_digits_of_l_number = 61
# computes the necessary "n_last" number per the requirements of the assignment
# computation takes into account that we are searching through an array to print our 
# nth Fibonacci number (note: "+ 1" at the end of the calculation). In this case, 
# our computation finds the 69th index of the array of Fibonacci numbers, which is 
# ultimately the 68th Fibonacci number
n_last = (7 + last_two_digits_of_l_number) + 1
#print the nth Fibonacci number
print(Fibonacci(n_last))
#print amount of second the program took to execute
print("Program took %s seconds to complete" % (time.time() - start_time))
