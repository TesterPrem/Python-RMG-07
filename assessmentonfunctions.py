sen = "big black bug bit a big black dog on his big black nose"
words = sen.split()
d = {}
def duplic(iterable):
    for item in words:
        if words.count(item) > 1:
            d[item] = words.count(item)
    print(d)
duplic(sen)
