def printGreeting():
    print "This program prints statistics about the exam"
    
def readFile(filename):
    dict = {}
    infile = open(filename, 'r')
    for line in infile:
        splitLine = line.split(' ')
        dict[splitLine[0]] = int(splitLine[1].strip())
    infile.close()
    return dict

def findMean(scores):
    sum = 0.0
    if len(scores) == 0:
        return sum
    for num in scores:
        sum = sum + num
    return sum/len(scores)
    
    
def main():
    examDict = {}
    printGreeting()
    filename = raw_input("Enter the name of the file: ")
    examDict = readFile(filename)
    scores = examDict.values()
    mean = findMean(scores)
    print "The mean of the scores is : " + str(mean)
    scores.sort()
    print "The minimum of the scores is : " + str(scores[0])
    print "The maximum of the scores is : " + str(scores[-1])
    
main()