count=dict()
print "Enter a line of text: "
line=raw_input("")

words=line.split()
print "words:",words
print "counting"

for word in words:
    count[word]=count.get(words,0)+1
print "counts", count


