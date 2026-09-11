test="i love python programming"
new_test="i love python programming"
my_list=["banana","apple"]
my_list.append("chillies")
print(my_list)

newTest=test.capitalize()
print(newTest)
print(test.lower())
print(test.upper())
print(test.strip())
print(test.split(" "))

print("python" in test)
print(test.replace("python", "java"))
print(test)

import string
import random

ascii_encoding=string.ascii_letters

def isAlpha(ch):
    if ch in ascii_encoding:
        print('the given charatcer is alphabet')
    else:
        print("is not an alphabet")

ch=input("please a provide a charater ")
isAlpha(ch)


def createRandomPassword(len):
    password=""

    for i in range(len):
        password=password+ random.choice(ascii_encoding)
    return password


len=int(input("please provide the length of the password you want to generate: "))
new_password=createRandomPassword(len)
print(new_password)


def countString(test):
    count=0
    for ch in test:
        if ch in ascii_encoding:
            count+=1
    print(count)

countString("test44")

