def first():
    x=45
    if x <=2:
        print "Small"
    else:
        print "Large"
try:
    inp=raw_input("Enter Hours: ")
    hours=float(inp)
    inp=raw_input("Enter Rate: ")
    rate=float(inp)
except:
    print "Error, please enter numeric input"
    quit()
if hours <=40:
    pay=rate*hours
else:
    pay=rate*40+(rate*1.5*(hours-40))
print pay
first()
