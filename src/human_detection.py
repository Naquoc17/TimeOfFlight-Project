from roboflow import Roboflow
import cv2
import os

# Roboflow API Details
API_KEY = 'R42FZQ54BjgwMmdryrMe'
PROJECT_ID = 'tof-humandetection-project'
MODEL_ID = 1
INPUT_VIDEO = '../output/mp4_video/video_016.mp4'
OUTPUT_VIDEO = '../output/detection_video/video_016_detected.mp4'
TEMP_FRAME_PATH = 'temp_frame.jpg'

# Ensure output folder exists
output_folder = os.path.dirname(OUTPUT_VIDEO)
os.makedirs(output_folder, exist_ok=True)

# Initialize Roboflow model
rf = Roboflow(api_key=API_KEY)
project = rf.workspace().project(PROJECT_ID)
model = project.version(MODEL_ID).model


def run_inference_on_video(video_path, output_path):
    # Open the input video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video properties - Width: {width}, Height: {height}, FPS: {fps}, Frames: {frame_count}")

    # Initialize video writer for saving the output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame temporarily for model inference
        cv2.imwrite(TEMP_FRAME_PATH, frame)

        # Run inference using the Roboflow model
        try:
            prediction = model.predict(TEMP_FRAME_PATH).json()
        except Exception as e:
            print(f"Error during inference on frame {frame_idx}: {e}")
            continue

        # Draw predictions on the frame
        for pred in prediction.get('predictions', []):
            x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
            confidence = pred['confidence']
            label = pred['class']

            # Draw bounding box
            top_left = (x - w // 2, y - h // 2)
            bottom_right = (x + w // 2, y + h // 2)
            cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 1)

            # Add label and confidence score
            cv2.putText(frame, f"{label}: {confidence:.2f}",
                        (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.15, (255, 0, 0), 1)

        # Write the processed frame to the output video
        out.write(frame)
        frame_idx += 1
        print(f"Processed frame {frame_idx}/{frame_count}")

    # Release resources
    cap.release()
    out.release()
    print(f"Inference completed. Results saved to {output_path}")


# Run the inference function
run_inference_on_video(INPUT_VIDEO, OUTPUT_VIDEO)
