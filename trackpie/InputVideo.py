import cv2

class InputVideo:
    def __init__(self):
        pass

    def __call__(self, video_path):
        frames = []
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Could not open the video file.")
            exit()

        while True:
            ret, frame = cap.read()
            
            if ret and not(frame is None):
                frames.append(frame)
            else:
                break

        return frames


        