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
    max = np.max(frame)
    min = np.min(frame)
    filter = max - min
    print(f"{np.max(frame)} - {np.min(frame)}")
    if min<100 or max>3050 or filter < 1000: # Adjust this threshold as needed
        return True
    return False
