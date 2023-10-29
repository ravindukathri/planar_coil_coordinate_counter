# Planar Coil Coordinate Counter

# Developed by Ravindu Kathriarachchie (github.com/ravindukathri)

This Python script helps you generate the coordinates of a planar coil based on the provided parameters. It calculates the coordinates for a planar coil with specified dimensions and properties.

## Parameters

The script uses the following parameters:

- **x**: Length in the x-direction.
- **y**: Length in the y-direction.
- **d**: Diameter of the coil (thickness).
- **s**: Gap between two coils.
- **n**: Number of turns.

## Installation (Libraries if you run locally)

Before running the script, make sure to install the necessary libraries:

```bash
pip install numpy
pip install matplotlib
```

## Running the Code

You can run the code by either cloning the repository or using an online Python compiler.

### Option 1: Clone Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/ravindukathri/planar_coil_coordinate_counter.git
```

### Option 2: Online Compiler

Alternatively, you can copy the code from `code.py` and run it on an online Python compiler, such as [Programiz's online compiler](https://www.programiz.com/python-programming/online-compiler/).

## Checking the Output

After running the code, you can generate the coordinates and visualize the result. The generated coordinates can be copied and pasted into the following online tool to visualize the planar coil:

[Coordinate Drawer](https://ctlessons.org/apps/coordinateDrawer)

## Example Usage

As an example, if you want to generate coordinates for a planar coil with the following parameters:

- x-10
- y-15
- s-1
- d-1
- n-2

The generated coordinates would be as follows:

```
0.0, 0.0
0.0, 15.0
10.0, 15.0
10.0, 0.0
2.0, 0.0
2.0, 13.0
8.0, 13.0
8.0, 2.0
4.0, 2.0
4.0, 3.0
7.0, 3.0
7.0, 12.0
3.0, 12.0
3.0, 1.0
9.0, 1.0
9.0, 14.0
1.0, 14.0
1.0, 0.0
0.0, 0.0
```

These coordinates can be used to visualize the planar coil's shape.