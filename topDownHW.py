def printGreeting():
    print "World Traveler Program (Converting) \n"
    
    
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

def displayMainMenu():
    
    print "What would you like to convert ?"
    print "\t 1 - Time"   
    print "\t 2 - Currency"    
    print "\t 3 - Temperature"   
    print "\t 4 - QUIT"
    choice = getValidInt("Your choice ",1,4)
    return choice
    
def displayLocationsMenu():
    print "Choose a location or M to return to Main Menu"
    print "\tL  - London"
    print "\tS  - Stockholm"
    print "\tT  - Tampere"
    print "\tH  - Helsinki"
    print "\tP  - St. Petersburg"
    print "\tM  - Return to Main Menu"
    user_input = raw_input("Enter location or M to return to Main Menu :")
    return user_input
    
def foriegnTimeToEastern(hour, adjustment):
    hour = hour - adjustment
    if hour < 0:
        hour = hour + 24
    
    if hour <= 11 or hour >= 24:
        if hour >= 24:
            return hour - 24, 'AM'
        else:
            return hour , 'AM'
    if hour >= 12 and hour < 24:
        if hour == 12:
            return hour, 'PM'
        else:
            return hour - 12, 'PM'

def getHourAndMinute():
    print "What time is it ?"
    hour = getValidInt("Enter the hour",0,23)
    minute = getValidInt("Enter the minute",0,59) 
    return hour,minute
    
def convertTime():
    
    user_input = ""

    
    while user_input != 'M' and user_input != 'm':
        
        user_input = displayLocationsMenu()
        
        
        if user_input == 'L' or user_input == 'l':
               
            hour, minute = getHourAndMinute()
            adj_time, s = foriegnTimeToEastern(hour,5)
            print str(hour) + ":" + str(minute) + " in London is " + str(adj_time) + ":" + str(minute) +  " " + s + " EST"

        elif user_input == 'S' or user_input == 's':
            
            hour, minute = getHourAndMinute()
            adj_time, s = foriegnTimeToEastern(hour,6)
            print str(hour) + ":" + str(minute) + " in Stockholm is " + str(adj_time) + ":" + str(minute) +  " " + s + " EST"
            
        elif user_input == 'T' or user_input == 't':
            
            hour, minute = getHourAndMinute()
            adj_time, s = foriegnTimeToEastern(hour,7)
            print str(hour) + ":" + str(minute) + " in Tampere is " + str(adj_time) + ":" + str(minute) +  " " + s + " EST"
            
        elif user_input == 'H' or user_input == 'h':
            
            hour, minute = getHourAndMinute()
            adj_time, s = foriegnTimeToEastern(hour,7)
            print str(hour) + ":" + str(minute) + " in Helsinki is " + str(adj_time) + ":" + str(minute) +  " " + s + " EST"
            
        elif user_input == 'P' or user_input == 'p':
            
            hour, minute = getHourAndMinute()
            adj_time, s = foriegnTimeToEastern(hour,8)
            print str(hour) + ":" + str(minute) + " in St. Petersburg is " + str(adj_time) + ":" + str(minute) +  " " + s + " EST"
            
        elif user_input == 'M' or user_input == 'm':
            break
            
        else:
            print user_input + ' is not a valid choice\n'
            user_input = displayLocationsMenu()
            
def foriegnToDollars(units,conversion):
    return units * conversion
    
def convertCurrency():
    user_input = ""
    
    while user_input != 'M' and user_input != 'm':
        
        user_input = displayLocationsMenu()
        
        if user_input == 'L' or user_input == 'l':
            
            pound = input("How many pounds ?")
            dollars = foriegnToDollars(pound, 1.53730)
            print str(pound) + " pounds is $ " + str(dollars)

        elif user_input == 'S' or user_input == 's':
            
            kronor = input("How many kronor ?")
            dollars = foriegnToDollars(kronor,0.139083)
            print str(kronor) + " kronors is $ " + str(dollars)
            
        elif user_input == 'T' or user_input == 't':
            
            euro = input ("How many euros ?")
            dollars = foriegnToDollars(euro,1.34960)
            print str(euro) + " euros is $ " + str(dollars)
            
        elif user_input == 'H' or user_input == 'h':
            
            euro = input ("How many euros ?")
            dollars = foriegnToDollars(euro,1.34960)
            print str(euro) + " euros is $ " + str(dollars)
            
        elif user_input == 'P' or user_input == 'p':
            
            ruble = input ("How many ruble ?")
            dollars = foriegnToDollars(ruble,0.0343348)
            print str(ruble) + " rubles is $ " + str(dollars)
            
        elif user_input == 'M' or user_input == 'm':
            break
            
        else:
            print user_input + ' is not a valid choice\n'
            user_input = displayLocationsMenu()
            
def main():
    
    choice = ""
    printGreeting()
    
    while choice != 4:
        
        choice = displayMainMenu()    
        if choice == 1:
            convertTime()
        elif choice == 2:
            convertCurrency()
        elif choice == 3:
            convertTemp()
        elif choice == 4:
            print
        else:
            print choice + ' is not a valid choice\n'
    
main()