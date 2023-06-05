numbers = []
l = len(numbers)

print("Enter a list of numbers, type 0 when finished.")

while True:
    number = float(input("Enter a number: "))
    numbers.append(number)
    s = sum(numbers)
    print(f"The sum is {s}")
    a = s / l 
    largest = max(numbers)
    print(f"The largest number is {largest}")
    if number == 0:
        break

