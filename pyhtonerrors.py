# print "This program finds the average of two integers."
# num1, num2 = input("Enter two numbers separated by a comma")
# average = (num1 + num2) / 2.0
# print "The average of the two numbers is " +  str(average)

import math
 
def isPrime(n):
    if n == 2:  
        return True
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True
 
for i in range(2, 18):
    print "Is %d prime?  %s" % (i, isPrime(i))