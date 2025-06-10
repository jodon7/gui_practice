'''Practice for Python GUI programming with Tkinter'''
import tkinter as tk
from tkinter import filedialog, messagebox
from utils import select_input_folder, select_output_folder, close_window


#TKinter GUI class
root = tk.Tk()
# Creating a root window title, this will be displayed at the top of the window
root.title("Python GUI Practice")
# Initial size of the window
root.geometry("400x300")

root.configure(bg="#e7fbf7")  # Setting a background color for the window
# Creating a label for input folder and also entry box
tk.Label(root, text="Input Folder:", bg="#b2e6dd").pack(pady=10)
input_folder_var = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(pady=5)
tk.Entry(input_frame, textvariable=input_folder_var, width=32).pack(side="left", padx=(0, 5))
tk.Button(
    input_frame,
    text="Select Folder",
    command=lambda: select_input_folder(input_folder_var),
    bg="#0074D9",      # Button background color
    fg="white"         # Button text color
).pack(side="left")

# Creating a label for output folder and also entry box
tk.Label(root, text="Output Folder:", bg="#b2e6dd").pack(pady=10)
output_folder_var = tk.StringVar()
output_frame = tk.Frame(root)
output_frame.pack(pady=5)
tk.Entry(output_frame, textvariable=output_folder_var, width=32).pack(side="left", padx=(0, 5))
tk.Button(
    output_frame,
    text="Select Folder",
    command=lambda: select_output_folder(output_folder_var),
    bg="#0074D9",      # Button background color
    fg="white"         # Button text color
).pack(side="left")

exit_button = tk.Button(
    root,
    text="Exit",
    command=lambda: close_window(root),
    bg="#FF4136",      # Red background for exit
    fg="white"         # White text
)
exit_button.pack(pady=30)
root.mainloop()