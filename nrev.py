def Number(number):
    reverse = 0
    while (number > 0):
        lastDigit = int(number % 10)
        reverse = int((reverse * 10) + lastDigit)
        number = int(number / 10)
    print(int(reverse))
number = int(input())
Number(number)
