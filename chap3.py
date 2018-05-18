print "This program illustrates average of numbers"

# total_num = input ("How many numbers you want to average : ")
# sum = 0.0
#
# for i in xrange(total_num):
#     sum = sum + input("Enter: " )
# average = sum/total_num
# print average

avg = 0.0
count = 0

while True:
    total = avg * count
    num = input("Enter : ")
    count = count + 1
    total = total + num
    avg = total/count
    print avg
