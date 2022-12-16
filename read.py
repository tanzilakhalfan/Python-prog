fhand=open("LibraryAPI.docx","r")
inp=fhand.read()
print len(inp)
print inp [12:20]


fhand=open("LibraryAPI.docx","r")
count=0
for line in fhand:
    count= count+1
print "line count:",count
