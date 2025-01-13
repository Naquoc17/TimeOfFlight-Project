import os
import cv2
import numpy as np

# Directory to save the frames
output_dir = "../data/test"
os.makedirs(output_dir, exist_ok=True)


# Save each frame as an image
def save_frames_as_images(frames, output_dir):
    try:
        for i, frame in enumerate(frames):
            # Normalize frame for better visualization
            normalized_frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
            image = np.uint8(normalized_frame)

            # Save the image
            image_path = os.path.join(output_dir, f"frame_{i:04d}.png")
            cv2.imwrite(image_path, image)

        print(f"All {len(frames)} frames have been saved to {output_dir}.")
    except Exception as e:
        print(f"Error saving frames: {e}")


# Save the frames
save_frames_as_images(frames, output_dir)
