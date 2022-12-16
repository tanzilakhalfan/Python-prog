fname=raw_input("Enter the File Name: ")
try:
    fhand=open(fname)
except:
    print "Incorrect file name",fname
    quit()
count=0
for line in fhand:
    if line.startswith("Khalfan"):
        count=count+1 
        
print "There were",count,"Khalfan lines in", fname ,"\nThankYou"