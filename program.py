try:
    inp=raw_input("Enter Hours: ")
    hours=float(inp)
    inp=raw_input("Enter Rate: ")
    rate=float(inp)
except:
    print "Error, please enter numeric input"
    quit()
#print rate,hours
if hours <=40:
    pay=rate*hours
else:
    pay=rate*40+(rate*1.5*(hours-40))
print pay
#BOTH ARE GOOD
try:
    inp=raw_input("Enter Hours: ")
    hours=float(inp)
except:
    print "Error, Please enter numeric input"
    quit()
try:
    inp=raw_input("Enter Rate: ")
    rate=float(inp)
    print rate,hours
except:
    print "Error, Please enter numeric input"
    quit()
if hours<=40:
    pay=rate*hours
else:
    pay=rate*40+(hours*1.5*(hours-40))
print pay