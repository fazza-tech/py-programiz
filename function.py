def greet(name):
    print(f"Hi {name}")
    print("How are you?")

greet("Fazza")


#function for add two numbers

def add_numbers(num1, num2):

    result = num1+num2
    print(f"The sum of two numbers are:: {result}")


number1 = 10
number2 = 20


add_numbers(number1,number2)

#function for add two numbers type 2

def add_numbers(num1, num2):
    result = num1+num2
    return result

a = 12
b = 13

result = add_numbers(a,b)
print("The sum is", result)

#len

marks = [10,20,30,30,40,50]

length = len(marks)
print(length)