# Program to find the sum of digits of a number

num = int(input("Enter a number: "))
sum_of_digits = 0
n = num

if n < 0:
    n = -n

while n > 0:
    sum_of_digits += n % 10
    n //= 10

print("Sum of digits:", sum_of_digits)
