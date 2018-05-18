import sys

# sum = 0
#
# num = input("Enter a positive number to check if its a perfect number or not: ")
#
# if num <= 0 or isinstance(num, float):
#     sys.exit()
#
# for i in xrange(1, num):
#     if num % i == 0:
#         sum = sum + i
#         print sum
#
# if sum == num:
#     print num
#     print "is a perfect number"
# else:
#     print num
#     print "is not a perfect number"
    
x = input("Enter x co-ordinate: ")
y = input("Enter y co-ordinate: ")

if x == 0 and y == 0:
    print "The point is the origin"
elif x == 0:
    print "The point is on y axis"
elif y == 0:
    print "The point is on x axis"
elif x > 0 and y > 0:
    print "The point is in first quadrant"
elif x > 0 and y < 0:
    print "The point is in fourth quadrant"
elif x < 0 and y < 0:
    print "The point is in third quadrant"
elif x < 0 and y > 0:
    print "The point is in second quadrant"