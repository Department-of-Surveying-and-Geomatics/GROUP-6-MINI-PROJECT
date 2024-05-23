import csv

def read_traverse_data(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            traverse_data = []
            for row in csv_reader:
                point_number = row[0]
                easting = row[1]
                northing = row[2]
                traverse_data.append((point_number, easting, northing))
            return traverse_data
    except FileNotFoundError:
        print("Error: File not found.")
    except IndexError:
        print("Error: Invalid data format in CSV file.")

# Example usage
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)

if traverse_data:
    for point_number, easting, northing in traverse_data:
        print(f"Point Number: {point_number}, x: {easting}, y: {northing}")