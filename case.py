fname=raw_input("Enter the file name: ")
fhand=open(fname,"r")
for line in fhand:
    line=line.rstrip()
    print line.upper()
 

hh=raw_input("Enter the file name: ")
handle=open(fname,"r")
for line in handle:
    line=line.rstrip()
    print line.lower()
    
    
