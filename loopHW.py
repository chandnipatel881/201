def isOdd(n):
    return n % 2 == 1
    
def hailStone(n, isPrint):
    counter = 0
    
    while n != 1:
        if isPrint:
            print str(n) + " -> ",
        counter = counter + 1
        if isOdd(n):
            n = n * 3 + 1
        else: 
            n = n / 2
    counter = counter + 1

    if isPrint:
        print str(n), " ; length = " + str(counter)
    return counter
    
def getValidInt(question, min, max):
 
    # use a bad value to enter the loop
    value = max + 1
 
    # compose the prompt
    prompt = question + " (" + str(min) + "-" + str(max) + "): "
 
    # continue to get values until the user enters a valid one
    while value == "" or value < min or value > max:
        value = raw_input(prompt)
        if len(value) != 0:
            value = int(value)
 
    # return a valid value
    return value    
    
def printGreeting():
    print "This program finds hailstone sequences of numbers you choose."
    print "The next number in the hailstone sequence is found by dividing"
    print "the number in half if it's even and multiplying by 3 and adding"
    print "one if it is odd."
    
def printMenu():
    print "\t I - view sequence for an Individual value"
    print "\t R - view sequence for a Range of values"
    print "\t L - find the Longest chain"
    print "\t X - Extra Credit"
    print "\t Q - Quit"

def main():
    
    START_QUES = "Enter the starting integer"
    END_QUES = "Enter the ending integer"
    choice = ""
    max_length = 0
    length = 0
    num = 0
    
    printGreeting()
    
    while choice != 'Q' and choice != 'q':
        print "\n"
        printMenu()
        choice = raw_input("Enter your choice: ")
        
        if choice == 'I' or choice == 'i':
            num = input("Enter your number (1 - 10000): ")
            hailStone(num, True)
            
        elif choice == 'R' or choice == 'r':
  
            start = getValidInt(START_QUES, 1, 10000)
            stop  = getValidInt(END_QUES, start, 10000)
    
            for i in xrange(start, stop + 1):
                hailStone(i, True)
                
        elif choice == 'L' or choice == 'l':
            
            start = getValidInt(START_QUES, 1, 10000)
            stop  = getValidInt(END_QUES, start, 10000)
    
            for i in xrange(start, stop + 1):
               length = hailStone(i, False)
               while length > max_length:
                   num = i
                   max_length = length
               
            print str(num) + " had the longest chain " + str(max_length)
            
        elif choice == 'X' or choice == 'x':
            
            start = getValidInt(START_QUES, 1, 1000000)
            stop  = getValidInt(END_QUES, start, 1000000)
    
            for i in xrange(start, stop + 1):
               length = hailStone(i, False)
               while length > max_length:
                   num = i
                   max_length = length
               
            print str(num) + " had the longest chain " + str(max_length)
            
        elif choice == 'Q' or choice == 'q':
            print
        else:
            print choice + ' is not a valid choice\n'
            
    
main() 
        