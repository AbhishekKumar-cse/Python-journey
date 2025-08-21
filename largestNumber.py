numbers = [3 ,6 ,7 ,8 ,9]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(f"Largest number: {max}")