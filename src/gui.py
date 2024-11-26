import tkinter as tk
from PIL import ImageTk
import numpy as np
import time
from object_detection import frame_filter

class HeatmapGUI:
    def __init__(self, frames):
        self.frames = frames
        self.current_frame_index = 0
        self.root = tk.Tk()
        self.root.title("ToF Heatmap Display")
        self.label = tk.Label(self.root)
        self.label.pack()

        self.update_frame()
        self.root.mainloop()

    def update_frame(self):
        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = 0

        current_frame = self.frames[self.current_frame_index]

        # Skip frame if ...
        if frame_filter(current_frame):
            print(f"Skipping frame {self.current_frame_index} due to low quality.")
            self.current_frame_index += 1
            self.root.after(100, self.update_frame)
            return

        # Apply smoothing
        from heatmap_display import smooth_depth_data, create_heatmap
        smoothed_frame = smooth_depth_data(current_frame)
        heatmap_image = create_heatmap(smoothed_frame)

        # Update GUI
        photo = ImageTk.PhotoImage(heatmap_image.resize((1200, 900)))
        self.label.config(image=photo)
        self.label.image = photo

        # Next frame
        self.current_frame_index += 1
        self.root.after(1000, self.update_frame)
