def famous_quote():
    author = "Hedy Lamar"
    message = "'All creative people want to do the unexpected.'"
    print(author + " once said: " + message)

def number_eight(): #addition, subtraction, multiplication, division and exponentiation
    print(5 + 3)
    print(12 - 4)
    print(4 * 2)
    print(int(16 / 2))
    print(2**3)

def name_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: ")) #Achtung integer plus Klammern
    print(f"Hello {name}. You are {age} years old.")
    print("Hello {}. You are {} years old.".format(name, age))
    print("Hello {0}. You are {1} years old".format(name, age))
    print("Hello " + name + ". You are " + str(age) + " years old.")

def swap_integers():
    x = 10
    y = 22
    print("x = " + str(x))
    print("y = " + str(y))

    x, y = y, x
    print("x = " + str(x))
    print("y = " + str(y))

def check_numbers(number1, number2):
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if (number1 % 6 == 0 or number2 % 6 == 0) and (number2 % 10 == 0 and number2 % 10 == 0):
        print("At least one number is divisible by 6.")
        print("At least one number is divisible by 10.")
    else:
        print("One or both numbers aren't divisible by 6.")
        print("One or both numbers aren't divisible by 10.")

def sum_up(number1, number2):
    print("Enter two numbers. The second number should be bigger than the first number.")
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if number1 >= number2:
        print("Error, number 1 isn't bigger than number 2.")
        sum_up(number1, number2)
    else:
        sum = int((number2 * (number2 + 1) / 2) - (number1 * (number1 + 1) / 2) + number1)
        print(sum)

def sequence(number):
    print("Enter a number from 0 to 9.")
    number = int(input("Enter number: "))

    if (number >= 9 or number < 0):
        print("Error, number is too big or too small. Please try again")
        sequence(number)
    else:
        range_without_number = list(range(10))
        (range_without_number.remove(number))
        print(range_without_number)

def check_string(text):
    print("Following function will tell you if a text ends or begins with the letter 'A/a'.")
    text = str(input("Enter your text: "))
    x = text.casefold()
    if x.startswith("a") or x.endswith("a"):
        print("The text ends and/or begins with the letter 'A/a'.")
        return True
    else:
        print("The text doesn't end and/or begins with the letter 'A/a'.")

#O, -1

    #alles lower case und 'a' suchen
    """str.endswith(suffix[, start[, end]])
Return True if the string ends with the specified suffix, otherwise return False. suffix 
can also be a tuple of suffixes to look for. With optional start, 
test beginning at that position. With optional end, stop comparing at that position."""

def triangle(rows):
    rows = int(input("Enter the number of rows: "))
    for i in range (1, rows+1):
       print ("* " * i)




famous_quote()
number_eight()
name_age()
swap_integers()
check_numbers(1, 2)
sum_up(3, 4)
sequence(6)
check_string("check check")
triangle(4)