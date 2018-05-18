import math

def printGreeting():
    print "This program classifies positive integers as"
    print "Odd/Even, Prime/Composite, Perfect/Abundant/Deficient,"
    print "Square, and Triangular"
    print 
    print "You will now get to choose the range of positive integers that "
    print "you would like to see classified."
    
def printTableHeading():
    print "Int     Classifications........................................"
    print "----------------------------------------------------------------"
    
def isOdd(n):
    return n % 2 == 1
        
def isPrime(n):
    if n == 2:  
        return True
    for divisor in xrange(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True   

def isDivisor(a,b):
    if b % a == 0:
        return True
    else:
        return False
    
def sumDivisors(n):
    divisor = 0
    for i in xrange(1,n):
        if isDivisor(i,n):
            divisor = divisor + i
    return divisor
     
def checkForPerfect(n):
    if sumDivisors(n) == n:
        return "Perfect"
    elif sumDivisors(n) < n:
        return "Deficient"
    else:
         return "Abundant"
    
def isSquare(n):
    sqrt = 0.0
    sqrt = math.sqrt(n)
    intsqrt = 0
    intsqrt = int(math.sqrt(n))
    if sqrt == intsqrt:
        return True
    else:
        return False
    
#
# def isTriangular(n):

def getTriangulars(n):
    tris = 1;
    i = 2;
    tris_lst = []
    while tris <= n:
        tris_lst.append(tris);
        tris = tris + i;
        i += 1
    return tris_lst
    
    
def printTableLine(n, odd, prime, perfect, square, triangle):
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    str5 = ""
    
    if odd == True:
        str1 = "Odd"
    else:
        str1 = "Even"
        
    if prime == True:
        str2 = "Prime"
    elif prime == False:
        str2 = "Composite"
    else:
        str2 = prime
        
    if perfect == "Perfect":
        str3 = "Perfect"
    elif perfect == "Deficient":
        str3 = "Deficient"
    else:
        str3 = "Abundant"
        
    if square == True:
        str4 = "Perfect"
    else:
        str4 == " "
        
    if triangle == True:
        str5 = "triangle"
    else:
        str5 = " "
        
    print "%-3i %-7s %-15s %-20s %-23s %-25s" % (n,str1, str2, str3, str4, str5)
    
def main():
    printGreeting()
    print "Start with which positive integer ?"
    start_num = input("Please enter an integer between 1 and 100000 : ")
    print "End with which positive integer ?"
    end_num = input("Please enter an integer between " + str(start_num) + " and 100000 : ")
    printTableHeading()
    tris_list = getTriangulars(end_num)
    for i in xrange(start_num, end_num + 1):
        if i == 1:
            printTableLine(i, isOdd(i), "Neither", checkForPerfect(i), isSquare(i), i in tris_list)
        else:   
            printTableLine(i, isOdd(i), isPrime(i), checkForPerfect(i), isSquare(i), i in tris_list)

main()
        
    
        
    
