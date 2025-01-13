import os
import numpy as np
from scipy.ndimage import gaussian_filter, median_filter

def smooth_depth_data(depth_data, use_median_filter=True, use_gaussian_filter=True):
    """
    Smooth depth data to reduce noise and outliers.

    Parameters:
    - depth_data: numpy.ndarray, the depth matrix
    - use_median_filter: bool, whether to apply a median filter for outliers
    - use_gaussian_filter: bool, whether to apply a Gaussian filter for smoothing

    Returns:
    - Smoothed depth data.
    """
    smoothed = np.copy(depth_data)

    # Apply median filter to handle outliers
    if use_median_filter:
        smoothed = median_filter(smoothed, size=3)

    # Apply Gaussian filter for noise smoothing
    if use_gaussian_filter:
        smoothed = gaussian_filter(smoothed, sigma=1)

    return smoothed

def frame_filter(frame):
    """
    Determine whether a frame should be deleted based on the criteria.

    Parameters:
    - frame: numpy.ndarray, the depth matrix

    Returns:
    - True if the frame should be deleted, False otherwise.
    """
    max_value = np.sum(frame > 3000) / 4800
    min_value = np.sum(frame < 100) / 4800
    return min_value > 0.8 or max_value > 0.8


# def process_frames(folder_path):
#     """
#     Process all .npy frames in the specified folder.
#
#     - Deletes frames that do not meet the criteria.
#     - Smooths the data of remaining frames.
#
#     Parameters:
#     - folder_path: str, path to the folder containing .npy frames.
#     """
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith(".npy"):
#             file_path = os.path.join(folder_path, file_name)
#
#             # Load the frame
#             frame = np.load(file_path)
#
#             # Check if the frame meets the filter criteria
#             if frame_filter(frame):
#                 print(f"Deleting frame: {file_name} (does not meet criteria)")
#                 os.remove(file_path)
#             else:
#                 # Smooth the data of the frame
#                 print(f"Smoothing frame: {file_name}")
#                 smoothed_frame = smooth_depth_data(frame)
#                 np.save(file_path, smoothed_frame)

def process_frames(parent_folder_path):
    """
    Process all .npy frames in the specified folder.

    - Deletes frames that do not meet the criteria.
    - Smooths the data of remaining frames.

    Parameters:
    - folder_path: str, path to the folder containing .npy frames.
    """
    for root, _, files in os.walk(parent_folder_path):
        for file_name in files:
            if file_name.endswith(".npy"):
                file_path = os.path.join(root, file_name)

                # Load the frame
                frame = np.load(file_path)

                # Check if the frame meets the filter criteria
                if frame_filter(frame):  # Assuming `frame_filter` returns False for valid frames
                    print(f"Deleting frame: {file_name} (does not meet criteria)")
                    os.remove(file_path)
                else:
                    # Smooth the data of the frame
                    print(f"Smoothing frame: {file_name}")
                    smoothed_frame = smooth_depth_data(frame)
                    np.save(file_path, smoothed_frame)

