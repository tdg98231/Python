#variables
div_30 = 0
div_5 = 0
div_3 = 0
div_2 = 0
div_3_2 = 0
div_none = 0

while True:
    try:
        l_number = int(input("Enter the lower number....not zero: "))
        if l_number > 0:
            break
    except:
        print("Please enter a valid number: ")

while True:
    try:
        u_number = int(input("Enter the upper number, larger than the lower number: "))
        if u_number > l_number:
            break
    except:
        print("Please enter a number larger than the lower number: ")

for number in range(l_number, u_number + 1):
    if number > 0:
        if number % 30 == 0:
            print("Foo")
            div_30 += 1
        elif number % 5 == 0:
            print("Bar")
            div_5 += 1
        elif  number % 3 == 0 and number % 2 == 0:
            print("FizzBuzz")
            div_3_2 +=  1
        elif number % 3 == 0:
            print("Fizz")
            div_3 += 1
        elif number % 2 == 0:
            print("Fizz")
            div_2 += 1
        else:
            print("Bazz")
            div_none += 1

print("The total numbers evaluated was " + str(number) + '.')
print("There were", div_30, "numbers that were divisible by 30.")
print("There were", div_5, "numbers that were divisible by 5.")
print("There were", div_3, "numbers that were divisible by 3.")
print("There were", div_2, "numbers that were divisible by 2.")
print("There were", div_3_2, "numbers that were divisible by 3 and 2.")
print("There were", div_none, "that did not meet the criteria.")


