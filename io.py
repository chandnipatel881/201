import string

def main():
  
    # get the filename from the user
    filename = raw_input("Enter the name of the file for line numbers : ")
 
    # construct outfile name
    filenameList = string.split(filename, '.')
    outFilename = filenameList[0] + '.withNum.' + filenameList[1]
 
    # open infile and outfile
    infile = open(filename, 'r')
    outfile = open(outFilename, 'w')
 
    i = 1
    # process each line in the file
    for line in infile:
        num = str(i) + " " + line 
        i+=1
        outfile.write(num)
 
    # close the files
    infile.close()
    outfile.close()
 
 
main()