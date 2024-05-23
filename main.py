import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(df, point1, point2):
    p1 = df[df['Point'] == point1].iloc[0]
    p2 = df[df['Point'] == point2].iloc[0]
    distance = np.sqrt((p2['Easting'] - p1['Easting'])**2 + (p2['Northing'] - p1['Northing'])**2)
    return distance

def calculate_bearing(df, point1, point2):
    p1 = df[df['Point'] == point1].iloc[0]
    p2 = df[df['Point'] == point2].iloc[0]
    angle = np.arctan2(p2['Northing'] - p1['Northing'], p2['Easting'] - p1['Easting'])
    bearing = np.degrees(angle)
    if bearing < 0:
        bearing += 360
    return bearing

def plot_traverse(df):
    plt.plot(df['Easting'], df['Northing'], marker='o')
    for i, row in df.iterrows():
        plt.text(row['Easting'], row['Northing'], str(row['Point']))
    plt.xlabel('Easting')
    plt.ylabel('Northing')
    plt.title('Traverse Plot')
    plt.grid(True)
    plt.show()

class TraverseApp:
    def __init__(self, master):
        self.master = master
        master.title("Traverse Analysis")

        self.label = tk.Label(master, text="Select CSV File:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.file_button = tk.Button(master, text="Browse", command=self.load_file)
        self.file_button.grid(row=0, column=1, padx=5, pady=5)

        self.file_path_label = tk.Label(master, text="")
        self.file_path_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.point1_label = tk.Label(master, text="Point 1:")
        self.point1_label.grid(row=2, column=0, padx=5, pady=5)

        self.point1_entry = tk.Entry(master)
        self.point1_entry.grid(row=2, column=1, padx=5, pady=5)

        self.point2_label = tk.Label(master, text="Point 2:")
        self.point2_label.grid(row=3, column=0, padx=5, pady=5)

        self.point2_entry = tk.Entry(master)
        self.point2_entry.grid(row=3, column=1, padx=5, pady=5)

        self.run_button = tk.Button(master, text="Run", command=self.run_analysis)
        self.run_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.plot_button = tk.Button(master, text="Plot Traverse", command=self.plot_traverse, state=tk.DISABLED)
        self.plot_button.grid(row=6, column=0, columnspan=2, pady=5)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.df = pd.read_csv(self.file_path)
            if 'Point' in self.df.columns and 'Easting' in self.df.columns and 'Northing' in self.df.columns:
                messagebox.showinfo("File Loaded", "CSV file loaded successfully!")
                self.file_path_label.config(text=f"File: {self.file_path}")
                self.plot_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "CSV file must contain 'Point', 'Easting', and 'Northing' columns.")
                self.df = None

    def run_analysis(self):
        if self.df is not None:
            try:
                point1 = int(self.point1_entry.get())
                point2 = int(self.point2_entry.get())
                distance = calculate_distance(self.df, point1, point2)
                bearing = calculate_bearing(self.df, point1, point2)
                self.result_label.config(text=f"Distance: {distance:.2f} m\nBearing: {bearing:.2f}Â°")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def plot_traverse(self):
        if self.df is not None:
            plot_traverse(self.df)

if __name__ == "__main__":
    root = tk.Tk()
    app = TraverseApp(root)
    root.mainloop()