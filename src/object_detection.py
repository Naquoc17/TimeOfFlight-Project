import numpy as np
from scipy.ndimage import label

def frame_filter(frame):
    max = np.max(frame)
    min = np.min(frame)
    filter = max - min
    print(f"{np.max(frame)} - {np.min(frame)}")
    if min<100 or max>3100 or filter < 1000: # Adjust this threshold as needed
        return True
    return False

def detect_human_head(depth_data, variance_threshold=600000, size_range=(100, 1500)):
    # Calculate variance
    variance = np.var(depth_data)
    if variance < variance_threshold:
        return None  # Frame is uniform, skip it

    # Apply fixed threshold to eliminate background noise
    binary_image = np.zeros_like(depth_data)
    binary_image[depth_data > variance_threshold] = 1

    # Label connected regions
    labeled_image, num_features = label(binary_image)

    # Filter regions based on size
    for region in range(1, num_features + 1):
        region_size = np.sum(labeled_image == region)
        if region_size < size_range[0] or region_size > size_range[1]:
            labeled_image[labeled_image == region] = 0

    return labeled_image

def detect_movement(previous_frame, current_frame, threshold=500):
    difference = np.abs(current_frame - previous_frame)
    movement_count = np.sum(difference > threshold)
    print(f"Detected movement in {movement_count} pixels.")
    return movement_count
