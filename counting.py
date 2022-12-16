fname=raw_input("Enter the file name: ")
fhand=open(fname,"r")
d1=dict()
for line in fhand:
    words=line.split()
    print(words)
    for word in words:
        if word in d1:
            d1[word]=d1[word]+1
        else:
            d1[word]=1
print (d1)

# words = ['Goldilocks', 'smelled', 'a', 'wonderful', 'smell,', 'loved', 'loved', 'loved', 'and', 'said', 'good', 'night', 'while', 'there']
# ['Goldilocks', 'smelled', 'a', 'wonderful', 'smell,', 'loved', 'loved', 'loved', 'and', 'said', 'good', 'night', 'while', 'there']