import tkinter as tk
from PIL import ImageTk
import numpy as np
from src.object_detection import *
from src.heatmap_display import *
from src.filter import *


class HeatmapGUI:
    def __init__(self, frames):
        self.frames = frames
        self.current_frame_index = 0
        self.previous_frame = None
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

        # If this is the first frame, initialize the previous frame and skip processing
        # if self.previous_frame is None:
        #     self.previous_frame = current_frame
        #     self.current_frame_index += 1
        #     self.root.after(100, self.update_frame)
        #     return


        # Skip frame if ...
        # if frame_filter(current_frame):
        #     print(f"Skipping frame {self.current_frame_index} due to low quality.")
        #     self.current_frame_index += 1
        #     self.root.after(100, self.update_frame)
        #     return

        heatmap_image = create_heatmap(smooth_depth_data(current_frame))

        humans = detect_human(current_frame, self.frames[0])
        print(f"Detected humans at: {humans}")


        # Update GUI
        photo = ImageTk.PhotoImage(heatmap_image.resize((800, 600)))
        print(f"Frame: {self.current_frame_index} - max: {np.max(current_frame)} - min: {np.min(current_frame)} - {np.unravel_index(np.argmin(current_frame), current_frame.shape)}")
        self.label.config(image=photo)
        self.label.image = photo

        # Next frame
        self.previous_frame = current_frame
        self.current_frame_index += 1
        self.root.after(100, self.update_frame)

