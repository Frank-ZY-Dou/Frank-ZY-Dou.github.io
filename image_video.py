import os
from PIL import Image
import cv2
folder_path = '/Users/Frank/Downloads/'


image_files = []
for i in range(1,192):
    image_files.append("untitled%d.png"%i)

if not image_files:
    print("No image files found in the folder.")
    exit()

output_video_path = 'output_video.mp4'
fps = 10

first_image_path = os.path.join(folder_path, image_files[0])
print(first_image_path)
first_image = cv2.imread(first_image_path)
height, width, _ = first_image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4编解码器
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)

video_writer.release()

print(f"Video saved at: {output_video_path}")

