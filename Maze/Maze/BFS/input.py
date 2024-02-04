import tkinter as tk
import BFS

def get_text():
    rtext = rtextbox.get("1.0", "end-1c")
    r_lines = rtext.split("\n")
    ctext = ctextbox.get("1.0", "end-1c") 
    c_lines = ctext.split("\n")
    print("Entered text:")
    for line in r_lines:
        print(line)
        r_array.append(line)
    for line in c_lines:
        print(line)
        c_array.append(line)
    root.destroy()


def pass_arrays_to_another_module():
    BFS.receive_arrays(r_array[-1], c_array[-1])

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root = tk.Tk()
root.title("Maze Dimension Input")

label = tk.Label(root, text="Enter rows:")
label.pack()

rtextbox = tk.Text(root, height=1, width=40)
rtextbox.pack(padx=10, pady=10)

label = tk.Label(root, text="Enter columns:")
label.pack()

ctextbox = tk.Text(root, height=1, width=40)
ctextbox.pack(padx=10, pady=10)

get_text_button = tk.Button(root, text="create", command=get_text)
get_text_button.pack(pady=5)

r_array = []
c_array = []

window_width = 300
window_height = 155
center_window(root, window_width, window_height)

root.mainloop()
BFS.create_maze(r_array[-1], c_array[-1])