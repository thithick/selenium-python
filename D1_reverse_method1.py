# Method2
# Using function
def reverseNumber(number):
    reverse = 0
    while (number > 0):
            lastDigit = number % 10
            reverse = (reverse * 10) + lastDigit
            number = number // 10
    print(reverse)

number = int(input("Please input a number to be reversed.\n"))
reverseNumber(number);
