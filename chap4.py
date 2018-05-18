listOfNum = []
sum = 0.0
min = 0
max = 0 
        
for i in range(5):
    list = input("Enter random numbers")
    listOfNum.append(list)

for num in listOfNum:
    sum = sum + num
    
def minmax (list):
    if len(list) == 1:
        min = list[i]
        max = list[i]
    if list[0] > list[1]:
        max = list[0]
        min = list[1] 
    else:
        min = list[0]
        max = list[1]    
    for num in list[2:]:
        if num > max:
            max = num
            print max
        elif num < min:
            min = num
            print min
    return min, max
 
min,max = minmax(listOfNum)
       
print "The total of numbers is:\n", sum
print "Min number is: \n", min
print "Max number is: \n", max
    
    