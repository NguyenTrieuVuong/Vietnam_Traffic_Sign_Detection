import torch
from IPython.display import Image, clear_output  # to display images

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')  # adjust the path as necessary

# Process the video
vid_path = 'video.mp4'  # replace with your video path
save_path = 'output.mp4'  # replace with the path where you want to save the output

results = model(vid_path)
results.save(save_path)

print(f"Output video saved to {save_path}")
