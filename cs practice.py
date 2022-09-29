#number is even or odd
num = 101

if num %2 ==0:
    print("even")
else:
    print("odd")

#string is palindrome or not

s = "malayalam"
if s == s[::-1]:
    print("palindrome")
else:
    print("not palidrome")

#number is a palindrome or not

n = 36543
s = str(n)

if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
#a character is alphabet or digit or special character

a = "@"
if ord("a")<= ord(a)<= ord("z") or ord("A") <= ord(a) <= ord("Z"):
    print("alphabet")
elif ord("0") <= ord(a) <= ord("9"):
    print("digit")
else:
    print("special character")

#given string starts with vowel or not

s = "output"

if s[0] in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

if s[3] in "aeiouAEIOU":
    print("is vowel")
else:
    print("no vowel")

#lowercase to upper case and vise versa

c = "9"
if ord("a")<= ord(c) <= ord("z") :
    print(chr(ord(c)-32))
elif ord("A") <= ord(c) <= ord("Z"):
    print(chr(ord(c)+32))
else:
    print("number")
#check whether a string or list or tuple is empty

s = "hi"
if s:
    print("not empty")
else:
    print("empty")
l = []
if l:
    print("not empty")
else:
    print("empty")

# check whether an itreable has even no of elements

s = {1,2,3,4}
if len(s) % 2==0:
    print("even")
else:
    print("odd")
#check whether the given iterable is a sequence, if it is reverse it.

l = [10,20,30,40,50]
if isinstance(l, (str, tuple, list)):
    print(l[::-1])
else:
    print(l)
#check the dictionary of odd no of keys, if it is add 1 more key value to dictionary.

d = {(1,2): 1, (3,4): 2, (5,6): 3}
if len(d) % 2 == 1 :
    d[(7,8)] = 4
    print(d)
else:
    print(none)

c = "&"

if c.isdigit():
    print("it is a number")
elif c.isalpha():
    print("it is alphabet")
else:
    print("special character")

#check whether last number is even or odd

p = 46536
p1 = str(p)
if int(p1[4]) % 2 == 0:
    print("even")
else:
    print("odd")

l1 = [20,50,50,91]

if int(l1[3]) % 2 == 1:
    print("odd")
else:
    print("even")



