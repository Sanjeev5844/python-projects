import tkinter as tk
from tkinter import messagebox

# Create a tkinter window
window = tk.Tk()

# Hide the main window
window.withdraw()

# Create a pop-up message box
messagebox.showinfo("Title", "This is a pop-up message!")

# Start the tkinter event loop
window.mainloop()