import cv2
import os
import glob


image_folder = "Your Path"
video_name = 'video.avi'
image_pattern = os.path.join(image_folder, "*.jpg")
jpg_files = glob.glob(image_pattern)

jpg_files_sorted = sorted(jpg_files, key=lambda x: int(os.path.basename(x).split("_")[0]))
print(jpg_files_sorted[:10])

frame = cv2.imread(jpg_files_sorted[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(os.path.join(image_folder, video_name), 0, 1, (width,height))

for image in jpg_files_sorted:
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()