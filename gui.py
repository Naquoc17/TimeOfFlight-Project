import tkinter as tk
from PIL import ImageTk
import time


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
        current_frame = self.frames[self.current_frame_index]

        # Apply smoothing
        from heatmap_display import smooth_depth_data, create_heatmap
        smoothed_frame = smooth_depth_data(current_frame)
        heatmap_image = create_heatmap(smoothed_frame)

        # Detect movement
        if self.previous_frame is not None:
            from object_detection import detect_movement
            detect_movement(self.previous_frame, smoothed_frame)

        self.previous_frame = smoothed_frame

        # Update GUI
        photo = ImageTk.PhotoImage(heatmap_image.resize((800, 600)))
        self.label.config(image=photo)
        self.label.image = photo

        # Next frame
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.root.after(100, self.update_frame)
