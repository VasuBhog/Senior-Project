import cv2 as cv

def find_camera_id():
    # assume the camera id is between 0 and 500; Maybe not!
    cams_tests = 500
    for i in range(0, cams_tests):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            test, frame = cap.read()
            print("i : " + str(i))

camera_number = 0 # default camera

capture = cv.VideoCapture(camera_number)
if not capture.isOpened():
    exit("not obtain camera")

# Tip: press ESC key to end display
while(True):
        ret, frame = capture.read()
        print(ret)
        frame = cv.flip(frame, 1)  # vertical = 0; horizontal > 0 ; both < 0
        cv.imshow("Video2", frame)
        c = cv.waitKey(
            100)  # waitKey(num) will display a frame for num ms, after which display will be automatically closed. (If you put it in a loop to read videos, it will display the video frame-by-frame)
        # It returns the code of the pressed key or -1
        if c == 27:  # press ESC key to break
            break