import numpy as np
from PIL import Image

def create_heatmap(depth_data):
    min_depth = np.min(depth_data)
    max_depth = np.max(depth_data)
    normalized = (depth_data - min_depth) / (max_depth - min_depth)

    heatmap = np.zeros((*depth_data.shape, 3), dtype=np.uint8)
    heatmap[..., 0] = (255 * normalized).astype(np.uint8)  # Red
    heatmap[..., 1] = (255 * (1 - abs(0.5 - normalized) * 2)).astype(np.uint8)  # Green
    heatmap[..., 2] = (255 * (1 - normalized)).astype(np.uint8)  # Blue

    return Image.fromarray(heatmap)

