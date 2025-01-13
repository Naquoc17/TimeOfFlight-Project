import numpy as np
from PIL import Image

def create_heatmap(binary_data):
    min_depth = np.min(binary_data)
    max_depth = np.max(binary_data)
    normalized = (binary_data - min_depth) / (max_depth - min_depth)

    heatmap = np.zeros((*binary_data.shape, 3), dtype=np.uint8)
    heatmap[..., 0] = (255 * normalized).astype(np.uint8)  # Red
    heatmap[..., 1] = (255 * (1 - abs(0.5 - normalized) * 2)).astype(np.uint8)  # Green
    heatmap[..., 2] = (255 * (1 - normalized)).astype(np.uint8)  # Blue

    # Ensure the heatmap shape is valid for Image.fromarray
    if len(heatmap.shape) == 4 and heatmap.shape[0] == 1:
        heatmap = heatmap[0]  # Remove the batch dimension if it exists

    return Image.fromarray(heatmap)

