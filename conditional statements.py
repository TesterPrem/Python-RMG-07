#wap to check whether a string is alphabet or digit or special characters
a = "A"

if ord("a") <= ord(a) <= ord("z") or ord("A") <= ord(a) <= ord("Z"):
    print("alphabet")
elif ord("0") <= ord(a)<= ord("9"):
    print("digit")

else:
    print("special char")


s = "Hello"
if s[0] in "aeiouAEIOU" :
    print("vowel")
else:
    print("consonant")

# lower cae string to upper case string and vice versa

a = "m"

if ord("a") <= ord(a) <= ord("z"):
    print(chr(ord(a)-32))
elif ord("A") <= ord(a) <= ord("Z"):
    print(ord(a)+32)

#check whether an iterable is empty or not
l = [1,2,3,4]

if l:
    print("not empty")
else:
    print("empty")

#wap to check the iterable have even number of elements

if len(l) % 2 ==0:
    print("even")
else:
    print("odd")

#wap to check whether the iterable is a sequence. if it is a sequence reverse it or keep it as it is.

if isinstance(l,(str, tuple, list)):
    print(l[::-1])
else:
    print(l)

#in a dictionary if keys are odd in numbers, add a key value pair else print the dictionary

d = {1: "one", 2:"true", 3:"three"}

if len(d) % 2 == 1:
    d[4] = "four"
    print(d)
else:
    print(d)


#wap to find the largest number

a = 10
b = 20
c = 30

if a>b and a>c :
    print("a is large")
elif b>a and b>c:
    print("b is large")
else:
    print("c is large")
# wap to write the first digit in the number is even or odd

n1 = 485
n2 = str(n1)
print(n2)
if int(n2[0]) % 2 ==0:
    print("even")
else:
    print("odd")


c = "6"

if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z"):
    print(c + c)
else:
    print(int(c)**2)
