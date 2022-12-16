data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
abc=data.find("@")
print abc

xyz=data.find(" ",abc)
print xyz

host=data[abc+1:xyz]
print host