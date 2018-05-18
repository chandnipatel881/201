FILE_LEN = 28
LAB_POINTS_POSSIBLE = 30

courseDataList = []
tot_A = 0
tot_B = 0
tot_C = 0
tot_D = 0
tot_F = 0

def calculateGrade(listOfScores):
    score = 0.0
    for i in xrange(1,len(listOfScores) - 2,2):
        temp = listOfScores[i]
        score = score + (temp * listOfScores[i-1])
        #print str(temp) + " * " + str(listOfScores[i-1])
    return score       
    
def findCourseScore(listOfScores):
    courseScore = 0.0
    courseScore = calculateGrade(listOfScores)  
    courseScore = courseScore + (listOfScores[-1]/30) * 10
    return courseScore
    
def findLetterGrade(score, lst):
    
    if score >= 90.0:
        lst[0] = lst[0] + 1
        return 'A', lst
    elif score >= 80 and score < 90:
        lst[1] = lst[1] + 1
        return 'B', lst
    elif score >= 70 and score < 80:
        lst[2] = lst[2] + 1
        return 'C', lst
    elif score >= 60.0 and score < 70:
        lst[3] = lst[3] + 1
        return 'D', lst
    else:
        lst[4] = lst[4] + 1
        return 'F', lst
        
def main():

    file = open("grades.txt", "r")
    ofile = open("gradesTotal.txt", "w")
    # #gather name, which is the first item on Lisa.txt
    name = ""
    average = 0.0
    total_score = 0
    total_student = 0
    dist_list = [0,0,0,0,0]
    
    for line in file:
        courseDataList = line.split(' ') 
        name = courseDataList[0]
        del courseDataList[0]

        #casting the list from str to float
        for i, val in enumerate(courseDataList):
            courseDataList[i] = float(val)
        courseScore = findCourseScore(courseDataList)
        
        total_score = total_score + courseScore
        total_student = total_student + 1
        average = total_score/total_student
        
        letterGrade , dist_list = findLetterGrade(courseScore, dist_list)
        ofile.write("%s: %.2f - %c \n" % (name, courseScore, letterGrade))

        
    ofile.write("\n")
    ofile.write("Class Average : %.2f" %(average))
    ofile.write("\n \n")
    ofile.write("  A : %s \n " %(dist_list[0]))
    ofile.write(" B : %s \n " %(dist_list[1]))
    ofile.write(" C : %s \n " %(dist_list[2]))
    ofile.write(" D : %s \n " %(dist_list[3]))
    ofile.write(" F : %s \n " %(dist_list[4]))
    
    
    file.close()
    ofile.close()

main()