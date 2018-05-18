FILE_LEN = 28
LAB_POINTS_POSSIBLE = 30

courseDataList = []

def calculateGrade(listOfScores):
    score = 0.0
    for i in xrange(1,len(listOfScores) - 2,2):
        temp = listOfScores[i]
        score = score + (temp * listOfScores[i-1])
        print str(temp) + " * " + str(listOfScores[i-1])
    return score       
    
def findCourseScore(listOfScores):
    courseScore = 0.0
    courseScore = calculateGrade(listOfScores)  
    courseScore = courseScore + (listOfScores[-1]/30) * 10
    return courseScore
    
def findLetterGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60.0 and score < 70:
        return 'D'
    else:
        return 'F'
        
def main():

    #gather name, which is the first item on Lisa.txt
    name = raw_input()

    #create a list from the file Lisa.txt
    for i in range(2,FILE_LEN):
        
	 #grab the rest of the values from the file and place into my list
        courseDataList.append(input())
    print courseDataList
    courseScore = findCourseScore(courseDataList)
 
    letterGrade = findLetterGrade(courseScore)
    print "%s: %.2f - %c" % (name, courseScore, letterGrade)

main()