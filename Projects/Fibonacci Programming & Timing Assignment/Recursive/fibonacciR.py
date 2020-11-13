#import time library to record execution
import time

#initialize a value that is equal to the current state of time.time()
start_time = time.time()

#define the Fibonacci sequence
def Fibonacci(n):
    #if n is less than 0, the program will return an error message
    if n < 0:
        print("Incorrect input")
    #if n is equal to 0, the program will return 0
    elif n == 0:
        return 0
    #if n is equal to 1, the program will return 1
    elif n == 1:
        return 1
    #if n is greater than 1, the program will compute the nth Fibonacci number
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

#defined the last two numbers of my L-number
last_two_digits_of_l_number = 31
# computes the necessary "n_last" number per the requirements of the assignment
# in this particular case, we are computing the 68th Fibonacci number
n_last = 7 + last_two_digits_of_l_number

#print the nth Fibonacci number
print(Fibonacci(n_last))
#print amount of second the program took to execute
print("Program took %s seconds to complete" % (time.time() - start_time))

#for loop that increments from 0 to 60
for i in range(0, 60, 1):
    #initialize a value that is equal to the current state of time.time()
    loop_time = time.time()
    #print the nth Fibonacci number
    print(Fibonacci(i))
    #print amount of second the program took to execute
    print(i, "took %s seconds to complete" % (time.time() - loop_time))
