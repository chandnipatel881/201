from stack import *
from queue import *
import sys

def extractTags(line,queueOfTags): 
    tag = ""
    in_tag = False
    
    #looping through the lines in the file
    for i in range(0,len(line)):
        #when < is encountered, tag is started. Setting the variable in_tag true
        if line[i] == "<":
            in_tag = True
        # when > is encountered, tag is ended. Setting the variable in_tag to false, adding the 
        # tag to the queue and resetting the tag varaible
        elif line[i] == ">" and in_tag:
            in_tag = False
            enqueue(queueOfTags,tag)
            tag = ""
        # keeps track of the tag text by checking the variable in_tag
        elif in_tag:
            tag += line[i]
    #If the program ends in <htm, this if statement takes care of it
    if in_tag:
        print "The input file ends in the middle of the program"
        exit()

def balancing(queueOfTags):
    balancedStack = stack()
    for tag in queueOfTags:
        if tag[0] == "/":
            start_tag = pop(balancedStack)
            end_tag = tag[1:]
            if start_tag == end_tag:
                print "<" + start_tag + "> matches </" + end_tag + ">"
        elif tag[-1] == "/":
            print "<" + tag + "> is self-closing"
        else:
            push(balancedStack, tag)
    

def readFromFile(filename):
    infile = open(filename, 'r')
    #creating queue to store tags
    queueOfTags = queue()
    for line in infile:
        extractTags(line,queueOfTags)
    
    for tag in queueOfTags:
        print "<" + tag + ">"
    print "Phase 1:  End of file was reached for " + filename + " with no errors"    
    balancing(queueOfTags)
    
    infile.close()

def main():
    filename = str(sys.argv[1])
    readFromFile(filename)
    
    
main()
    
    
    
