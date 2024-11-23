import numpy as np
import os

def read_exported_frames(directory):
    frames = []
    for file_name in sorted(os.listdir(directory)):
        if file_name.endswith(".npy"):
            frame = np.load(os.path.join(directory, file_name))
            frames.append(frame)
    return frames

def read_frames_from_text(directory):
    frames = []
    for file_name in sorted(os.listdir(directory)):
        if file_name.endswith(".txt"):
            with open(os.path.join(directory, file_name), "r") as f:
                depth_data = []
                for line in f:
                    row = list(map(float, line.strip().split()))
                    depth_data.append(row)
                frames.append(depth_data)
    return frames