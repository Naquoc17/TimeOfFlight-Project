from src.exporter import export_frames
from src.exporter import export_frames_to_text

export_frames("../data/data.bin", "../exported_frames/frames_npy")
export_frames_to_text("../data/data.bin", "../exported_frames/frames_txt")