#print the numbers from 10 to 1
num = 1
while (num<=10):
    print(num, end = " ")
    num = num +1

#print numbers from 10 to 1
print()
num = 10
while(num >=1):
    print(num, end= " ")
    num = num -1
#print even numbers upto 20
print()
num = 0
while num <= 20:
    print(num, end= " ")
    num+= 2
print()

#print odd numbers upto 20

num = 1
while num <= 20:
    print(num, end= " ")
    num+=2

print()
#iterate over the string and print all the characters

s = "Hello World"
i = 0
while i < len(s):
    print(s[i], end= "")
    i+= 1
print()
#print alternate character of the string

i = 0
while i < len(s):
    print(s[i], end= "")
    i+= 2

print()
#print string in the reverse order

i = len(s) - 1

while i >= 0:
    print(s[i], end= "")
    i-= 1

print()
#print all the vowels in the string

i = 0
while i < len(s):
    if s[i] in "aeiouAEIOU":
        print(s[i], end="")
    i+= 1


