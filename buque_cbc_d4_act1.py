shapes = ["square", "heart", "circle", "diamond"]
numbers = [1, 5, 3, 2]

shapes.insert(3, "hexagon")
shapes.append("triangle")
print("Inserted shape:", shapes)


shapes.sort()

print("Sorted List:", shapes)

total = sum(numbers)

print("Sum of numbers:", total)

numbers.clear()
print("Cleared list:", numbers)