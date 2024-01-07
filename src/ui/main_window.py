import tkinter as tk
from chart.realtime_chart import RealTimeChart

class RealTimeDataApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Real-Time Data Visualization")

        # Initialize UI components
        self.realtime_chart = RealTimeChart(master=self.master)


