numbers = [1, 2, 3 ,40.5, 'asd']

# random indexing --> O(1) get items if we know the index !!!
print(numbers[4])

numbers[1] = 'Adam'

print(numbers[1])

for num in numbers:
  print(num)


for i in range(len(numbers)):
  print(numbers[i])

print(numbers[:-2])


# O(N) search running time
maximum = numbers[0]
for num in numbers:
  if (
    isinstance(num, int)
    or isinstance(num, float)
  ) and num > maximum:
    maximum = num

print(maximum)