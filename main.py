import random

numbers = []
for i in range(random.randint(0, 100)):
  numbers.append(random.randint(0, 10000000000))
  minimum = min(numbers)
  maximum = max(numbers)

sum = 0
for i in numbers:
  sum += i

print("Random Numbers:", numbers)
print("Minimum Number:", minimum)
print("Maximum Number:", maximum)
print("Sum:", sum)
