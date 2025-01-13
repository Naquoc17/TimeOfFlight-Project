import os
from src.exporter import export_frames_as_vector,export_frames_to_text

input_folder =  "../data/roh"
output_folder_npy = "../exported_frames/frames_npy"
output_folder_img = "../exported_frames/frames_img"
output_folder_txt = "../exported_frames/frames_txt"

# Ensure output directories exist
os.makedirs(output_folder_npy, exist_ok=True)
os.makedirs(output_folder_txt, exist_ok=True)

# Loop through all files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".bin"):
        # Remove .bin from the file name
        base_name = os.path.splitext(file_name)[0]

        input_file_path  = os.path.join(input_folder, file_name)
        npy_output_path = os.path.join(output_folder_npy, base_name)
        txt_output_path = os.path.join(output_folder_txt, base_name)

        # Create directories for each file's output
        os.makedirs(npy_output_path, exist_ok=True)
        os.makedirs(txt_output_path, exist_ok=True)

        # Export frames to .npy and .txt
        export_frames_as_vector(input_file_path, npy_output_path)
        export_frames_to_text(input_file_path, txt_output_path)

    print("Export completed!")