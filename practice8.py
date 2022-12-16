


abc="hello world"
try:
    xyz=int(abc)
except:
    xyz=-1
print "first",xyz

abc="563"
try:
    xyz=int(abc)
except:
    xyz=-1
print "Second",xyz
print "All Done"



abc="123"
try:
    xyz=str(abc)
except:
    xyz=-1
print "fake",xyz