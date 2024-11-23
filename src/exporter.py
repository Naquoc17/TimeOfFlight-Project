import numpy as np
import os

def export_frames(file_path, output_dir, width=80, height=60, depth_size=8):
    frame_size = width * height * depth_size

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, "rb") as f:
        frame_index = 0
        while True:
            buffer = f.read(frame_size)
            if len(buffer) != frame_size:
                break

            depth_data = np.zeros((height, width), dtype=np.float64)
            index = 0
            for y in range(height):
                for x in range(width):
                    if depth_size == 1:
                        depth = buffer[index]
                        index += 1
                    elif depth_size == 2:
                        depth = int.from_bytes(buffer[index:index+2], byteorder='big')
                        index += 2
                    elif depth_size == 4:
                        depth = np.frombuffer(buffer[index:index+4], dtype='>i4')[0]
                        index += 4
                    elif depth_size == 8:
                        depth = np.frombuffer(buffer[index:index+8], dtype='<f8')[0]
                        index += 8
                    else:
                        raise ValueError("Unsupported depth size")
                    depth_data[y, x] = depth

            np.save(os.path.join(output_dir, f"frame_{frame_index}.npy"), depth_data)
            frame_index += 1

    print(f"Exported {frame_index} frames to {output_dir}")


def export_frames_to_text(file_path, output_dir, width=80, height=60, depth_size=8):
    frame_size = width * height * depth_size

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, "rb") as f:
        frame_index = 0
        while True:
            buffer = f.read(frame_size)
            if len(buffer) != frame_size:
                break

            depth_data = []
            index = 0
            for y in range(height):
                row = []
                for x in range(width):
                    if depth_size == 1:
                        depth = buffer[index]
                        index += 1
                    elif depth_size == 2:
                        depth = int.from_bytes(buffer[index:index+2], byteorder='big')
                        index += 2
                    elif depth_size == 4:
                        depth = int.from_bytes(buffer[index:index+4], byteorder='big', signed=True)
                        index += 4
                    elif depth_size == 8:
                        depth = float.fromhex(buffer[index:index+8].hex())
                        index += 8
                    else:
                        raise ValueError("Unsupported depth size")
                    row.append(depth)
                depth_data.append(row)

            # Record frames into txt
            output_file = os.path.join(output_dir, f"frame_{frame_index}.txt")
            with open(output_file, "w") as frame_file:
                for row in depth_data:
                    frame_file.write(" ".join(map(str, row)) + "\n")
            frame_index += 1

    print(f"Exported {frame_index} frames to {output_dir}")
