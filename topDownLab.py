import calendar
# some constants
MIN_YEAR = 1900
MAX_YEAR = 2500
 
SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
weekdayFor1990 = 0

def printGreeting():
    print "This program will print the calender for the year you enter"

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
    
def monthName(monthNum):
    if monthNum == 1:
        return "January"
    elif monthNum == 2:
        return "February"
    elif monthNum == 3:
        return "March"
    elif monthNum == 4:
        return "April"
    elif monthNum == 5:
        return "May"
    elif monthNum == 6:
        return "June"
    elif monthNum == 7:
        return "July"
    elif monthNum == 8:
        return "August"
    elif monthNum == 9:
        return "September"
    elif monthNum == 10:
        return "October"
    elif monthNum == 11:
        return "November"
    else:
        return "December"
           
# def isLeapYear(year):
#     if year%4 == 0 and year%100 !=0:
#         if year%400 == 0:
#             return True
#     else:
#         return False     

def weekdayFor1900(month,year):
    global weekdayFor1990
    if month == 1:
        weekdayFor1990 = 1
    else:
        numDays = monthDays(month - 1,year)
        weekdayFor1990 = (weekdayFor1990 + numDays) % 7
    return weekdayFor1990

def firstDayOfTheMonth(monthNum,year):
    
    weekday = weekdayFor1900(monthNum,year)
    
    for years in xrange(1900, year):
            if calendar.isleap(years):
                weekday = (weekday + 366) % 7
            else:
                weekday = (weekday + 365) % 7
    return weekday

def indentFirstLine(weekday):
    if weekday == 0:
        print 
    elif weekday == 1:
        print "  ",
    elif weekday == 2:
        print "     ",
    elif weekday == 3:
        print "        ",
    elif weekday == 4:
        print "           ",
    elif weekday == 5:
        print "              ",
    else:
        print "                 ",


def monthDays(month,year):
    if month == 2:
        if calendar.isleap(year):
            return 29
        else:
            return 28
    if month == 9 or month == 4 or month == 6 or month == 11 :
        return 30
    else:
        return 31



def printMonth(monthNum,year):
    month = ""
    weekday = ""
    month = monthName(monthNum)
    print
    print "    " + str(month) + " " + str(year) 
    print
    print "Su Mo Tu We Th Fr Sa"
    
    weekday = firstDayOfTheMonth(monthNum,year)
    indentFirstLine(weekday)
    
    numDays = monthDays(monthNum,year)
    
    for day in range(1, numDays + 1):
        print "%2d" % (day),
        if weekday == SATURDAY:
            print 
        weekday = (weekday + 1) % 7
    if weekday != SUNDAY:
        print   
            
def printCalendar(year):
    for month in xrange(1,13):
        printMonth(month,year) 
    
 
def main():
 
    printGreeting()
 
    year = getValidInt("Which year would you like? ", MIN_YEAR, MAX_YEAR )
    printCalendar(year)
 
main()