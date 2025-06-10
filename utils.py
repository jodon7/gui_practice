from tkinter import filedialog, messagebox


def select_input_folder(input_folder_var):
    folder_in = filedialog.askdirectory(title="Select Input Folder")
    if folder_in:
        input_folder_var.set(folder_in)

def select_output_folder(output_folder_var):
    folder_out = filedialog.askdirectory(title="Select Output Folder")
    if folder_out:
        output_folder_var.set(folder_out)

def close_window(root):
    root.destroy()
    