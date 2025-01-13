import numpy as np
from scipy.ndimage import median_filter


def detect_human(current_frame, first_frame):
    """
    Detect humans in the current frame based on the given conditions.

    Parameters:
    - current_frame: numpy.ndarray, the current frame data
    - first_frame: numpy.ndarray, the first frame data used for comparison

    Returns:
    - List of coordinates representing detected humans
    """
    # Condition 1: Process points with insufficient differences or exceeding thresholds
    processed_frame = np.copy(current_frame)
    diff = np.abs(current_frame - first_frame)

    # Ignore points where the difference is less than or equal to 300
    binary_frame = median_filter(diff, size=3)
    binary_frame = binary_frame.astype(str)
    binary_frame[diff <= 900] = "0"
    # binary_frame[(diff > 450) & (diff <= 470)] = "1"
    binary_frame[(diff > 900) & (diff <= 2600)] = " "
    binary_frame[(diff > 2600)] = "1"
    print(f"binary frame:")
    for row in binary_frame:
        print(" ".join(row))

    # Set values to match the first frame if the difference exceeds 2000
    processed_frame[diff > 2000] = first_frame[diff > 2000]

    # Condition 2: Find points with values between 100 and 400
    possible_heads = np.where((processed_frame >= 100) & (processed_frame <= 400))

    head_points = list(zip(possible_heads[0], possible_heads[1]))

    # Condition 3: Confirm humans based on the average value within a 10x10 square
    detected_humans = []

    return detected_humans
