import numpy as np

def detect_human(current_frame, first_frame):
    """
    Detect humans in the current frame based on the given conditions.

    Parameters:
    - current_frame: numpy.ndarray, the current frame data
    - first_frame: numpy.ndarray, the first frame data to compare with

    Returns:
    - List of coordinates representing detected humans
    """
    # Điều kiện 1: Xử lý các điểm không đủ chênh lệch hoặc vượt giới hạn
    processed_frame = np.copy(current_frame)
    diff = np.abs(current_frame - first_frame)

    # Bỏ qua điểm nếu chênh lệch nhỏ hơn hoặc bằng 300
    processed_frame[diff <= 300] = 0

    # Đặt giá trị về giống frame đầu tiên nếu chênh lệch vượt quá 2000
    processed_frame[diff > 2000] = first_frame[diff > 2000]

    # Điều kiện 2: Tìm điểm có giá trị từ 40 đến 400
    possible_heads = np.where((processed_frame >= 40) & (processed_frame <= 400))
    head_points = list(zip(possible_heads[0], possible_heads[1]))

    # Loại bỏ các điểm đã bị bỏ qua trong điều kiện 1
    valid_heads = [
        (x, y) for x, y in head_points if processed_frame[x, y] != 0
    ]

    # Điều kiện 3: Xác nhận người dựa trên trung bình ô vuông 10x10
    detected_humans = []
    for x, y in valid_heads:
        # Lấy ô vuông 10x10
        x_min, x_max = max(0, x - 5), min(processed_frame.shape[0], x + 5)
        y_min, y_max = max(0, y - 5), min(processed_frame.shape[1], y + 5)
        square = processed_frame[x_min:x_max, y_min:y_max]

        # Tính trung bình
        avg_value = np.mean(square)
        if abs(avg_value - processed_frame[x, y]) <= 50:
            detected_humans.append((x, y))

    return detected_humans
