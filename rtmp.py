
''' Youtube Channel : Asim Code  
View RTSP Stream from IP Camera, Live video streaming over the network with OpenCV in Python
https://youtu.be/ZBRqWPE-_yM
'''
import cv2
import imutils
from imutils.video import VideoStream
rtmp_url = "rtmp://192.168.1.129:1935/live/test"
video_stream = VideoStream(rtmp_url).start()

while True:
    frame = video_stream.read()
    if frame is None:
        continue

    frame = imutils.resize(frame,width=900)
    cv2.imshow('Streaming Policia Federal Argentina', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video_stream.stop()