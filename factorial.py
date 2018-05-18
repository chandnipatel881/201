def factorial(n):
    product = 1
 
# finds product of all integers from 1 up to
# and including n, where product will finally
# hold the value of n!
    for i in range (1, n+1):
        print i
        product *= i
    return product

def main():
     ans = factorial(5)
     print ans
     
main()