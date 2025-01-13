import numpy as np
import os


def read_depth_data(buffer, width, height, depth_size):
    """
    Reads depth data from a binary buffer and returns it as a 2D NumPy array.

    Args:
        buffer (bytes): Binary data for a single frame.
        width (int): Width of the frame.
        height (int): Height of the frame.
        depth_size (int): Number of bytes per depth value.

    Returns:
        np.ndarray: 2D array of depth values.
    """
    if depth_size == 1:
        # Interpret buffer as unsigned 8-bit integers
        depth_data = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width))
    elif depth_size == 2:
        # Interpret buffer as unsigned 16-bit big-endian integers
        depth_data = np.frombuffer(buffer, dtype='>u2').reshape((height, width))
    elif depth_size == 4:
        # Interpret buffer as signed 32-bit big-endian integers
        depth_data = np.frombuffer(buffer, dtype='>i4').reshape((height, width))
    elif depth_size == 8:
        # Interpret buffer as 64-bit little-endian floating-point numbers
        depth_data = np.frombuffer(buffer, dtype='<f8').reshape((height, width))
    else:
        raise ValueError("Unsupported depth size")
    return depth_data

def export_frames_to_text(file_path, output_dir, width=80, height=60, depth_size=8):
    """
    Exports frames from a binary file into .txt files for each frame.

    Args:
        file_path (str): Path to the binary file.
        output_dir (str): Directory to save the exported frames.
        width (int): Width of each frame.
        height (int): Height of each frame.
        depth_size (int): Number of bytes per depth value.
    """
    frame_size = width * height * depth_size  # Calculate total bytes per frame
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    with open(file_path, "rb") as f:
        frame_index = 0
        while True:
            # Read binary data for one frame
            buffer = f.read(frame_size)
            if len(buffer) != frame_size:
                # Stop if the remaining data is less than a full frame
                break

            # Convert binary buffer into a 2D NumPy array
            depth_data = read_depth_data(buffer, width, height, depth_size)

            # Save the depth data as a text file
            output_file = os.path.join(output_dir, f"frame_{frame_index}.txt")
            np.savetxt(output_file, depth_data, fmt='%s', delimiter=" ")
            frame_index += 1

    print(f"Exported {frame_index} frames to {output_dir}")

def export_frames_as_vector(file_path, output_dir, width=80, height=60, depth_size=8):
    """
    Exports frames from a binary file into .npy files for each frame.

    Args:
        file_path (str): Path to the binary file.
        output_dir (str): Directory to save the exported frames.
        width (int): Width of each frame.
        height (int): Height of each frame.
        depth_size (int): Number of bytes per depth value.
    """
    frame_size = width * height * depth_size  # Calculate total bytes per frame
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    with open(file_path, "rb") as f:
        frame_index = 0
        while True:
            # Read binary data for one frame
            buffer = f.read(frame_size)
            if len(buffer) != frame_size:
                # Stop if the remaining data is less than a full frame
                break

            # Convert binary buffer into a 2D NumPy array
            depth_data = read_depth_data(buffer, width, height, depth_size)
            # Save the frame as a .npy file
            np.save(os.path.join(output_dir, f"frame_{frame_index}.npy"), depth_data)
            frame_index += 1

    print(f"Exported {frame_index} frames to {output_dir}")


# def export_frames_to_images(file_path, output_dir, width=80, height=60, depth_size=8):
#     """
#     Exports frames from a binary file into .png files for each frame.
#
#     Args:
#         file_path (str): Path to the binary file.
#         output_dir (str): Directory to save the exported frames.
#         width (int): Width of each frame.
#         height (int): Height of each frame.
#         depth_size (int): Number of bytes per depth value.
#     """
#     frame_size = width * height * depth_size  # Calculate total bytes per frame
#     os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
#
#     with open(file_path, "rb") as f:
#         frame_index = 0
#         while True:
#             # Read binary data for one frame
#             buffer = f.read(frame_size)
#             if len(buffer) != frame_size:
#                 # Stop if the remaining data is less than a full frame
#                 break
#
#             # Convert binary buffer into a 2D NumPy array
#             depth_data = read_depth_data(buffer, width, height, depth_size)
#
#             # Save the depth data as a text file
#             output_file = os.path.join(output_dir, f"frame_{frame_index}.txt")
#             np.savetxt(output_file, depth_data, fmt='%s', delimiter=" ")
#             frame_index += 1
#
#     print(f"Exported {frame_index} frames to {output_dir}")