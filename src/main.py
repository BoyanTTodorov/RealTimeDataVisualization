import tkinter as tk
from ui.main_window import RealTimeDataApp

# Create the main Tkinter window
root = tk.Tk()

# Instantiate the RealTimeDataApp class
app = RealTimeDataApp(root)

# Start the Tkinter event loop
root.mainloop()
