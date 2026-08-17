# Python program to check whether a number is an Armstrong number

num = int(input("Enter a number: "))

# Find the number of digits
power = len(str(num))

# Calculate the sum of digits raised to the power
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

# Check if it is an Armstrong number
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")