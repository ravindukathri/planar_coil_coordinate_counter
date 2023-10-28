import numpy as np
import matplotlib.pyplot as plt


# Ask the user for values of x, y, d, s, and n
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
d = float(input("Enter the value of d: "))
s = float(input("Enter the value of s: "))
n = int(input("Enter the value of n: "))

# Display the entered values
print(f"You entered the following values:")
print(f"x: {x}")
print(f"y: {y}")
print(f"d: {d}")
print(f"s: {s}")
print(f"n: {n}")

# Convert the user's input to an integer (int)
try:
    data_points = int(11+(n-1)*8)
    print(f"You entered the integer: {n}")
    print(f"Numberof data points: {data_points}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


calculate_coordinates()

print(f"List X = {list_x}")
print(f"List Y = {list_y}")


#Paired Values
paired_values = [(x, y) for x, y in zip(list_x, list_y)]

for x, y in paired_values:
    print(f"{x}, {y}")


# Create a plot
plt.plot(list_x, list_y, marker='o', linestyle='-', color='b')

# Set axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set a title for the plot
plt.title('Data Points Plot')

# Show the plot
plt.grid()
plt.show()
    
    
def calculate_coordinates(x, y, d, s, n):
    # First 5 numbers
    list_x = [0, 0, x, x, x + d + s]
    list_y = [0, y, y, 0, 0]

    # Second Sets
    max_val = n
    i = 1
    if max_val > 1:
        while i <= max_val - 1:
            x1 = i * (d + s)
            x2 = x - i * (d + s)
            x3 = x - i * (d + s)
            x4 = (i + 1) * (d + s)
            second_x = [x1, x2, x3, x4]
            list_x.extend(second_x)

            y1 = y - i * (d + s)
            y2 = y - i * (d + s)
            y3 = i * (d + s)
            y4 = i * (s + d)
            second_y = [y1, y2, y3, y4]
            list_y.extend(second_y)

            i += 1

    # Center Number
    center_x = n * (d + s)
    center_y = (n - 1) * s + n * d
    list_x.append(center_x)
    list_y.append(center_y)

    # Last Sets
    max_val = n
    j = max_val - 1
    if max_val > 1:
        while j >= 1:
            x5 = x - (j + 1) * d - j * s
            x6 = x - (j + 1) * d - j * s
            x7 = (j + 1) * d + j * s
            x8 = (j + 1) * d + j * s
            last_x = [x5, x6, x7, x8]
            list_x.extend(last_x)

            y5 = (j + 1) * d + j * s
            y6 = y - (j + 1) * d - j * s
            y7 = y - (j + 1) * d - j * s
            y8 = j * d + (j - 1) * s
            last_y = [y5, y6, y7, y8]
            list_y.extend(last_y)

            j -= 1

    # Last 5 numbers
    list_x.extend([x - d, x - d, d, d, 0])
    list_y.extend([d, y - d, y - d, 0, 0])

    return list_x, list_y

# Usage example:
x = 10
y = 20
d = 2
s = 3
n = 5

result_x, result_y = calculate_coordinates(x, y, d, s, n)
print(result_x)
print(result_y)