from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import sqlite3
import threading
import time

class RealTimeChart:
    def __init__(self, master):
        self.master = master

        # Initialize variables
        self.is_running = False
        self.data_points = []

        # Create GUI components
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.button = tk.Button(master=self.master, text="Start", command=self.toggle_realtime)
        self.button.pack(pady=20)

    def toggle_realtime(self):
        if not self.is_running:
            self.is_running = True
            self.button["text"] = "Stop"
            self.button["bg"] = "red"
            threading.Thread(target=self.realtime_update).start()
        else:
            self.is_running = False
            self.button["text"] = "Start"
            self.button["bg"] = "green"

    def create_table(self):
        # Create a new SQLite connection for each thread
        conn = sqlite3.connect(":memory:")
        with conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS realtime_data (value REAL)")
        return conn

    def insert_data(self, value, conn):
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO realtime_data (value) VALUES (?)", (value,))

    def fetch_data(self, conn):
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM realtime_data")
            return cursor.fetchall()

    def update_chart(self, conn):
        self.ax.clear()
        data = self.fetch_data(conn)
        if data:
            values = [row[0] for row in data]
            self.ax.plot(values, marker='o')
            self.ax.set_title("Real-Time Data Chart")
            self.canvas.draw()

    def realtime_update(self):
        conn = self.create_table()  # Create a new connection for each thread
        while self.is_running:
            # Generate random data
            value = np.random.rand() * 10

            # Insert data into SQLite database
            self.insert_data(value, conn)

            # Update Matplotlib chart
            self.update_chart(conn)

            # Pause for a short interval (simulating real-time updates)
            time.sleep(1)
