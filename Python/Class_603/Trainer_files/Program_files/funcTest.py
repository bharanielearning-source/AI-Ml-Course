def test(a,b):
    print("the value of a is ",a)
    print("the value of b is", b)

test(10,20)
print("*"*60)
test(90,80)
print("*"*60)
test(70,55)
global_result=100

def calculator(input1=10, input2=20, operator="-"):
    """ this is a calculator function, it accepts two values as inputs and a third value as the operator function"""
    result=0
    if(operator=="+"):
        result=input1+input2
        print("this is addition call, the sum of the given number is", result)
    elif(operator=="-"):
        result=input1-input2
        print("this is substraction call, the minus of the given number is", result)
    elif(operator=="*"):
        result=input1*input2
        print("this is MULTIPLICATION call, the product of the given number is", result)
    elif(operator=="/"):
        result=input1/input2
        print("this is division call, the division of the given number is",result)
    else:
        print("Hello sir/madam, please check the operator provided")
    return result



input1=int(input("please provide the input1 number"))
input2=int(input("please provide the input2 number"))
operator=(input("please provide the operator from the below choice: +, -, /, *"))
print(global_result)
calculator_result=calculator(input1, input2, operator)
print("------------", calculator_result)


def is_palindrome(input):
    strin_input=str(input)
    reversed=strin_input[::-1]
    if reversed==strin_input:
        print("the given input is a palindrome")
    else:
        print("not a palindrome")
test=input("provide a character, number or text to check a palindrome or not")
is_palindrome(test)






