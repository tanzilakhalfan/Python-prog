#3fruit="banana"
#letter=fruit[2]
#print letter

#fruit="avocado"
#n=3
#w=fruit[n-2]
#print w 
    
#fruit="avocado"
#print len(fruit)

#fruit="avocado"
#letter=fruit[8]
#print letter

#ERROR string index out of range

#fruit="avocado"
#index=0
#while index<len(fruit):
#    letter=fruit[index]
#    print index,letter 
#    index=index+1
    
fruit="avocado"
for letter in fruit:
    print fruit
    
    
    
word="avocado"
count=0
for letter in word:
    if letter=="v":
        count=count+1
print count


s="Monty Python"
print s[0:4]

    
s="Monty Python"
print s[6:7]


s="Monty Python"
print s[6:20]

s="Monty Python"
print s[:]

greet="HellO Bob one"
abc=greet.capitalize()
print abc


print "Hi There".lower()
print "hello world".upper()
