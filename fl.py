fname=raw_input("Enter the file name: ")
fhand=open(fname,"r")
for line in fhand:
    line=line.rstrip()
    print line.title()
