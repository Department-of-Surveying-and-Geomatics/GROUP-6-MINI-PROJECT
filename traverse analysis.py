import tkinter as tk
from tkinter import ttk
import math
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('traverse_data.csv')

# Calculate the total number of points
total_points = len(data)

# Calculate the minimum and maximum Easting and Northing values
min_easting = data['Easting'].min()
max_easting = data['Easting'].max()
min_northing = data['Northing'].min()
max_northing = data['Northing'].max()

# Calculate the distance and bearing between any two points
def calculate_distance_and_bearing(point1, point2):
    easting1 = data.loc[data['Point'] == point1, 'Easting'].values[0]
    northing1 = data.loc[data['Point'] == point1, 'Northing'].values[0]
    easting2 = data.loc[data['Point'] == point2, 'Easting'].values[0]
    northing2 = data.loc[data['Point'] == point2, 'Northing'].values[0]

    distance = math.sqrt((easting2 - easting1)**2 + (northing2 - northing1)**2)
    bearing = math.atan2(northing2 - northing1, easting2 - easting1) * 180 / math.pi

    return distance, bearing

# GUI function
def calculate_and_display():
    point1 = int(point1_entry.get())
    point2 = int(point2_entry.get())

    distance, bearing = calculate_distance_and_bearing(point1, point2)

    distance_label.config(text=f"Distance between point {point1} and point {point2}: {distance:.2f} meters")
    bearing_label.config(text=f"Bearing from point {point1} to point {point2}: {bearing:.2f} degrees")

# Create the GUI
root = tk.Tk()
root.title("Traverse Characteristics")
root.configure(bg="#f0f0f0")  # Set the background color

# Display the total number of points
total_points_label = tk.Label(root, text=f"Total number of points: {total_points}", font=("Arial", 14), bg="#f0f0f0")
total_points_label.pack(pady=10)

# Display the minimum and maximum Easting and Northing values
min_easting_label = tk.Label(root, text=f"Minimum Easting: {min_easting}", font=("Arial", 12), bg="#f0f0f0")
min_easting_label.pack(pady=5)
max_easting_label = tk.Label(root, text=f"Maximum Easting: {max_easting}", font=("Arial", 12), bg="#f0f0f0")
max_easting_label.pack(pady=5)
min_northing_label = tk.Label(root, text=f"Minimum Northing: {min_northing}", font=("Arial", 12), bg="#f0f0f0")
min_northing_label.pack(pady=5)
max_northing_label = tk.Label(root, text=f"Maximum Northing: {max_northing}", font=("Arial", 12), bg="#f0f0f0")
max_northing_label.pack(pady=5)

# User input for points
point1_label = tk.Label(root, text="Point 1:", font=("Arial", 12), bg="#f0f0f0")
point1_label.pack(pady=10)
point1_entry = ttk.Entry(root, font=("Arial", 12))
point1_entry.pack(pady=5)

point2_label = tk.Label(root, text="Point 2:", font=("Arial", 12), bg="#f0f0f0")
point2_label.pack(pady=10)
point2_entry = ttk.Entry(root, font=("Arial", 12))
point2_entry.pack(pady=5)

# Button to calculate and display the distance and bearing
calculate_button = ttk.Button(root, text="Calculate", command=calculate_and_display, style="TButton")
calculate_button.pack(pady=20)

# Display the distance and bearing
distance_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
distance_label.pack(pady=10)
bearing_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
bearing_label.pack(pady=10)

# Apply some styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white", padding=10)
style.configure("TEntry", font=("Arial", 12), padding=5)

root.mainloop()