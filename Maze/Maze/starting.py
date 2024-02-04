import tkinter as tk
from tkinter import messagebox
import subprocess

# Dictionary mapping options to their corresponding files
option_files = {
    "BFS": "Maze/BFS/input.py",
    "DFS": "Maze/DFS/input.py",
    "A STAR": "Maze/AStar/input.py",
}

def run_selected_file():
    selected_option = var.get()
    if selected_option in option_files:
        file_to_run = option_files[selected_option]
        subprocess.run(["python", file_to_run])
    else:
        messagebox.showwarning("Option Not Found", "Selected option does not have a corresponding file.")

# Create the main window
root = tk.Tk()
root.title("Options Window")

# Set the initial size of the window (width x height)
root.geometry("200x150")

# Create a label
label = tk.Label(root, text="Choose an Option:")
label.pack()

# Options (including an initial default option)
options = ["BFS", "DFS", "A STAR"]

# Create a variable to hold the selected option
var = tk.StringVar(root, value="None")  # Set an initial default value ("None")

# Create radio buttons for each option
for option in options:
    radio_button = tk.Radiobutton(root, text=option, variable=var, value=option)
    radio_button.pack(anchor=tk.W)  # Align radio buttons to the left

# Create a button to display the selected option
select_button = tk.Button(root, text="Select", command=run_selected_file)
select_button.pack()

# Run the main loop
root.mainloop()