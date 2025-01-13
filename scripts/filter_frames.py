import os
from src.filter import process_frames

def main():
    # Define the folder containing .npy frames
    frames_folder = "../exported_frames/frames_npy"

    # Check if the folder exists
    if not os.path.exists(frames_folder):
        print(f"Error: The folder '{frames_folder}' does not exist.")
        return

    # Process all frames in the folder
    print(f"Processing frames in folder: {frames_folder}")
    process_frames(frames_folder)
    print("Processing completed!")


if __name__ == "__main__":
    main()