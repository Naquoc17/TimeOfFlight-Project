import numpy as np

def detect_movement(previous_frame, current_frame, threshold=500):
    difference = np.abs(current_frame - previous_frame)
    movement_count = np.sum(difference > threshold)
    print(f"Detected movement in {movement_count} pixels.")
    return movement_count
