fname=raw_input("Enter the File Name: ")
fhand=open(fname,"r")

for line in fhand:
    line=line.rstrip()
    print line.upper()
    

