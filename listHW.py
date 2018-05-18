partA = ["CMSC 201", "CMSC 202", "CMSC 203", "CMSC 304", "CMSC 313", "CMSC 331", "CMSC 341", "CMSC 345", "CMSC 411", "CMSC 421", "CMSC 441"]
partB = ["MATH 151", "MATH 152", "MATH 221"]
partC = ["STAT 355", "STAT 451"]
partD_1 = ["BIOL 100", "BIOL 301"]
partD_2 = ["CHEM 101", "CHEM 102"]
partD_3 = ["PHYS 121", "PHYS 122"]
listOfSciClasses = ["BIOL 100 BIOL 100L", "BIOL 251 BIOL 251L", "BIOL 252 BIOL 252L", "BIOL 275 BIOL 275L", "BIOL 301", "BIOL 302 BIOL 302L", "BIOL 303 BIOL 303L", "BIOL 304 BIOL 304L", "BIOL 305 BIOL 305L", "CHEM 101", "CHEM 102 CHEM 102L", "GES 110  GES 111", "GES 120  PHYS 121", "PHYS 122 PHYS 122L"]
global counter
counter = 0

inputList = list()

numOfClasses = input("How many classes you have taken: \n")

print "\nEnter classes in the form <MAJOR-CODE> <COURSE-NUMBER>"

for i in xrange(numOfClasses):
    x = raw_input("Class: ")
    inputList.append(x)

print "\nPart A Requirements: "

for course in partA:
    if course not in inputList:
        print("You need to take " + course)
     
print "\nPart B Requirements:"

for course in partB:
    if course not in inputList:
        print("You need to take " + course)
       
print "\nPart C Requirements:"

if partC[0] not in inputList or partC[1] not in inputList:
        print("You need to take " + partC[0] + " or " + partC[1]) 
        

def isSubList(inputtedList, originalList):
    global counter
    returnList = []
    for course in originalList:
        if course not in inputtedList:
            returnList.append(course)
        else:
            counter = counter + 4
    return returnList  
    
def printList(listToPrint):
    if len(listToPrint) == 1:
        print "You need to take " + listToPrint[0]
    else:
        print "You need to take " + listToPrint[0] + " AND " + listToPrint[1]
    
def printOtherCourses(listOfSciClasses):
    print "\nYou currently have " + str(counter) + " science credits."
    print "You need to have 12 total science credits taken from the following list: "
    for courses in xrange(len(listOfSciClasses)):
        print listOfSciClasses[courses]
    
print "\nPart D Requirements: "

list_1 = isSubList(inputList,partD_1) 
list_2 = isSubList(inputList,partD_2)
list_3 = isSubList(inputList,partD_3)

d1 = False
if not list_1 or not list_2 or not list_3 :
    d1 = True
else:
    printList(list_1)
    print "OR"
    printList(list_2)
    print "OR"
    printList(list_3)    
    
if not d1 or counter < 12:
    printOtherCourses(listOfSciClasses)
else:
    print ("Part D requirments has been met")
# def firstHalfForBio(inputList):
#     global counter
#     if partD_a[0] in inputList and partD_a[1] in inputList:
#         if counter < 12:
#             print "You have completed first half of part D requirements"
#             counter = counter + 8
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[0] in inputList:
#         print counter
#         counter = counter + 4
#         if counter < 12:
#             print("You need to take " + partD_a[1] + "\nOR\nYou need to take " + partD_a[2] + " AND " + partD_a[3] + "\nOR\nYou need to take " + partD_a[4] + " AND " + partD_a[5])
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[1] in inputList:
#         counter = counter + 4
#         if counter < 12:
#             print("You need to take " + partD_a[0] + "\nOR\nYou need to take " + partD_a[2] + " AND " + partD_a[3] + "\nOR\nYou need to take " + partD_a[4] + " AND " + partD_a[5])
#         else:
#             print "You have satisfied the part D requirement"
#
# def firstHalfForChem(inputList):
#     global counter
#     if partD_a[2] in inputList and partD_a[3] in inputList:
#         if counter < 12:
#             print "You have completed first half of part D requirements"
#             counter = counter + 8
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[2] in inputList:
#         if counter < 12:
#             print("You need to take " + partD_a[0] + " AND " + partD_a[1] + "\nOR\nYou need to take " + partD_a[3] + "\nOR\nYou need to take " + partD_a[4] + " AND " + partD_a[5])
#             counter = counter + 4
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[3] in inputList:
#         if counter < 12:
#             print("You need to take " + partD_a[0] + " AND " + partD_a[1] + "\nOR\nYou need to take " + partD_a[2] + "\nOR\nYou need to take " + partD_a[4] + " AND " + partD_a[5])
#             counter = counter + 4
#         else:
#             print "You have satisfied the part D requirement"
#
# def firstHalfForPhy(inputList):
#     global counter
#     if partD_a[4] in inputList and partD_a[5] in inputList:
#         if counter < 12:
#             print "You have completed first half of part D requirements"
#             counter = counter + 8
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[4] in inputList:
#         if counter < 12:
#             print("You need to take " + partD_a[0] + " AND " + partD_a[1] + "\nOR\nYou need to take " + partD_a[2] + " AND " + partD_a[3] + "\nOR\nYou need to take " + partD_a[5])
#             counter = counter + 4
#         else:
#             print "You have satisfied the part D requirement"
#     elif partD_a[5] in inputList:
#         if counter < 12:
#             print("You need to take " + partD_a[0] + " AND " + partD_a[1] + "\nOR\nYou need to take " + partD_a[2] + " AND " + partD_a[3] + "\nOR\nYou need to take " + partD_a[4])
#             counter = counter + 4
#         else:
#             print "You have satisfied the part D requirement"
#
# firstHalfForBio(inputList)
# firstHalfForChem(inputList)
# firstHalfForPhy(inputList)
#
# if counter < 12 :
#     print "\nYou currently have " + str(counter) + " science credits."
#     print "You need to have 12 total science credits taken from the following list: "
#     for courses in xrange(len(listOfSciClasses)):
#         print listOfSciClasses[courses]
         