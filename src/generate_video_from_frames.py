import os
import numpy as np
import cv2
from heatmap_display import create_heatmap

# Parent folder containing subfolders with .npy files
parent_folder_path = "../exported_frames/frames_npy"
output_video_folder = "../output/video"

# Ensure the output directory exists
os.makedirs(output_video_folder, exist_ok=True)

# Video settings
frame_rate = 5  # Frames per second
frame_size = (80, 60)  # Width x Height of heatmap (ensure it matches data dimensions)


def create_video_from_folder(input_folder, output_video_path, frame_rate, frame_size):
    # Get sorted list of all .npy files in the folder
    npy_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.npy')])

    if not npy_files:
        print(f"No .npy files found in folder: {input_folder}")
        return

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, frame_size)

    for npy_file in npy_files:
        file_path = os.path.join(input_folder, npy_file)

        # Load depth data
        depth_data = np.load(file_path)

        # Generate heatmap
        heatmap_image = create_heatmap(depth_data)

        # Convert PIL Image to OpenCV format (BGR)
        heatmap_frame = cv2.cvtColor(np.array(heatmap_image), cv2.COLOR_RGB2BGR)

        # Resize frame to match video size if needed
        heatmap_frame = cv2.resize(heatmap_frame, frame_size)

        # Write frame to video
        video_writer.write(heatmap_frame)

    video_writer.release()
    print(f"Heatmap video saved to {output_video_path}")


# Loop through all subfolders in the parent folder
video_index = 1  # Counter for naming videos
for root, _, files in os.walk(parent_folder_path):
    # Filter out only .npy files for processing
    npy_files = [f for f in files if f.endswith('.npy')]

    if npy_files:
        # Create a video for the current folder
        output_video_path = os.path.join(output_video_folder, f"video_{video_index:03d}.mp4")
        print(f"Processing folder: {root}")

        create_video_from_folder(root, output_video_path, frame_rate, frame_size)

        video_index += 1

print("All videos have been generated.")
