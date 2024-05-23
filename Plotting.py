import csv
import matplotlib.pyplot as plt

# Function to read data from CSV file
def get_file(filename):
    points = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            x = float(row[1])
            y = float(row[2])
            points.append([x, y])
    return points

# Get points from CSV file
filename = 'traverse_data.csv'  # Provide the filename of your CSV file
points = get_file(filename)

x = [point[0] for point in points]  # Easting coordinates
y = [point[1] for point in points]  # Northing coordinates
point_numbers = range(1, len(points) + 1)  # Point numbers

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', alpha=0.7, label='Traverse Points')

# Add point numbers as annotations
for i, (xi, yi, point_number) in enumerate(zip(x, y, point_numbers)):
    plt.annotate(point_number, (xi, yi), textcoords="offset points", xytext=(0, 10), fontsize=8)

# Label axes and add a title
plt.xlabel('EASTING')
plt.ylabel('NORTHING')
plt.title('TRAVERSE VISUALIZATION')
plt.grid(True)

# Add legend
plt.legend()

plt.show()