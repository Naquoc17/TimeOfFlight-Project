from reader import read_exported_frames
from gui import HeatmapGUI

def main():
    folder_path = "../exported_frames/frames_npy"
    frames = read_exported_frames(folder_path)

    if not frames:
        print("No frames found!")
        return

    # Start the GUI for heatmap visualization
    HeatmapGUI(frames)

if __name__ == "__main__":
    main()
