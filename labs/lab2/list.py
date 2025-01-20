'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''

goodlist = ['work','study','discipline']
badlist = ['be lazy','waste time','depression']

print(goodlist)
print(badlist)

print('Change your mind')

badlist[0]='sport'
badlist[1]='friends'
badlist[2]='music'

goodlist.insert(2,'relax')
badlist.append('anger')
goodlist.extend(badlist)

print('Lets se what we get')
print(goodlist)
print('we have a mistake lets fix it') 

goodlist.pop()

for x in goodlist:
    if "s" in x:
        print(x)

print('Lets sort it')
goodlist.sort()

print(goodlist)