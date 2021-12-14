import urllib.request 

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for line in fhand:
    print(line.decode().strip())
print('$'*20)
counts = dict()
for x in fhand:
    words=x.decode().strip()
    for word in words:
        counts[word]= counts.get(word,0)+1
print(counts)