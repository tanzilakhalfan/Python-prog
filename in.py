fhand=open("fileread.txt")
count=0
for line in fhand:
    line=line.rstrip()
    count=count+1
    if not "@gmail.com" in line:
        continue
    print line
print "Total Line count: ",count