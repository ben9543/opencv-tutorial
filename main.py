import cv2 as cv


def showImage(filepath):
    img = cv.imread(filepath)

    cv.imshow('Cat', img)

    cv.waitKey(0)

def showVideo(filepath):
    capture = cv.VideoCapture(filepath)

    while True:
        isTrue, frame = capture.read() # Returns the frame and boolean
        

        frame_resized = rescaleFrame(frame, scale=0.25)

        cv.imshow('Video', frame_resized)

        # Once you press key 'd' you can terminate the video
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

showVideo("./Videos/ben.mp4")