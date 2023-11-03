import numpy as np
import matplotlib.pyplot as plt

def get_user_input(prompt):
    return float(input(prompt))

def get_integer_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer_input(prompt)

def generate_data_points(x, y, d, s, n):
    data_points = 11 + (n - 1) * 8
    print(f"You entered the integer: {n}")
    print(f"Number of data points: {data_points}")

    list_x = [0, 0, x, x, d + s]
    list_y = [0, y, y, 0, 0]

    for i in range(1, n):
        x1 = i * (d + s)
        x2 = x - i * (d + s)
        x3 = x - i * (d + s)
        x4 = (i + 1) * (d + s)

        second_x = [x1, x2, x3, x4]
        list_x = np.append(list_x, second_x)

        y1 = y - i * (d + s)
        y2 = y - i * (d + s)
        y3 = i * (d + s)
        y4 = i * (s + d)

        second_y = [y1, y2, y3, y4]
        list_y = np.append(list_y, second_y)

    center_x = n * (d + s)
    center_y = (n - 1) * s + n * d

    list_x = np.append(list_x, center_x)
    list_y = np.append(list_y, center_y)

    for j in range(n - 1, 0, -1):
        x5 = x - (j + 1) * d - (j) * s
        x6 = x - (j + 1) * d - (j) * s
        x7 = (j + 1) * d + (j) * s
        x8 = (j + 1) * d + (j) * s

        last_x = [x5, x6, x7, x8]
        list_x = np.append(list_x, last_x)

        y5 = (j + 1) * d + (j) * s
        y6 = y - (j + 1) * d - (j) * s
        y7 = y - (j + 1) * d - (j) * s
        y8 = j * d + (j - 1) * s

        last_y = [y5, y6, y7, y8]
        list_y = np.append(list_y, last_y)

    list_x = np.append(list_x, [x - d, x - d, d, d, 0])
    list_y = np.append(list_y, [d, y - d, y - d, 0, 0])

    return list_x, list_y

while True:
    x = get_user_input("Enter the value of x: ")
    y = get_user_input("Enter the value of y: ")
    d = get_user_input("Enter the value of d: ")
    s = get_user_input("Enter the value of s: ")
    n = get_integer_input("Enter the value of n: ")

    print("You entered the following values:")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"d: {d}")
    print(f"s: {s}")
    print(f"n: {n}")

    if x < (2+(n-1)*2)* d + (1+(n-1)*2) * s:
        print("Your X value is smaller, please try again.")
    elif y < (2+(n-1)*2)* d + (1+(n-1)*2) * s:
        print("Your Y value is smaller, please try again.")
    else:
        list_x, list_y = generate_data_points(x, y, d, s, n)

        print(f"List X = {list_x}")
        print(f"List Y = {list_y}")

        paired_values = [(x, y) for x, y in zip(list_x, list_y)]

        for x, y in paired_values:
            print(f"{x}, {y}")

            #add option to download this as a txt file to the file

        plt.plot(list_x, list_y, marker='o', linestyle='-', color='b')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Data Points Plot')
        plt.grid()
        plt.show()

    run_again = input("Do you want to run the script again? (yes/no): ").lower()
    if run_again != "yes":
        break