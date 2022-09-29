for ref in range(10):
    print(ref, end=" ")
print()
for rev in range(0, 11, 2):
    print(rev, end=" ")
print()
#traverse thro a string
s = 'Hello World'

for r1 in range(len(s)):
    print(s[r1], end=" ")
print()
for r2 in s:
    print(r2, end="")

print()
#for traversing thro as set

s1 = {1,2,3,4}

for ele in s1:
    print(ele, end=" ")
print()
for ele1 in range(len(s1)):
    print(ele1, end=" ")

print()
#iterate over a string in reverse direction

s = 'Hello World'
for rev in range(-1, -12, -1):
    print(s[rev], end=" ")
print()
str1 = "hi"

str1 = str1 + s
print(str1)
print(id(s))
print(id(str1))

#enumerate

s = 'Hello World'

for item in enumerate(s):
    print(item, end=" ")

print()
# to print only indices using enumerate

for item in enumerate(s):
    print(item[0], end=" ")
print()

for item in enumerate(s):
    print(item[1], end=" ")

#for list
print()
l = [1,2,3,4]

for ilist in enumerate(l):
    print(ilist, end=" ")
print()
d = {1: "one", 2: " two", 3: "three"}

for diction in enumerate(d):
    print(diction, end=" ")



