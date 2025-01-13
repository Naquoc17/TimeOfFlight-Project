from reader import read_exported_frames
from src.gui import HeatmapGUI

def main():
    # folder_path = "../exported_frames/frames_npy/2022-05-25 11%3A59%3A01.944108_Terabee_measurement"
    folder_path = "../output/detect_frames"
    frames = read_exported_frames(folder_path)

    if not frames:
        print("No frames found!")
        return

    # Start the GUI for heatmap visualization
    HeatmapGUI(frames)

if __name__ == "__main__":
    main()
