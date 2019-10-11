import cv2


#Compute the frames diferences
def frame_diff(prev_frame, cur_frame, next_frame):
    #Difference between the current frame and the next frame
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)

    #Difference between the current frame and the previous one
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)

    return cv2.bitwise_and(diff_frames_1, diff_frames_2)

def get_frame(cap, scaling_factor):
    #Read the current frame from the video object
    _, frame = cap.read()

    # Resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor,
                    fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # Converto to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    return gray

if __name__ == "__main__":

    # define the video capture object
    cap = cv2.VideoCapture(0)
    
    # define the scaling factore
    scaling_factor = 0.5

    # grab the current frame
    prev_frame = get_frame(cap, scaling_factor)

    # Grab the next frame
    cur_frame = get_frame(cap, scaling_factor)

    # Grab the frame after that
    next_frame = get_frame(cap,scaling_factor)

    # Keep reding the frames from the screen until user press ESC Key

    while True:

        # Display the frame difference
        cv2.imshow('Object Movement',frame_diff(prev_frame,cur_frame,next_frame))

        # update the variables
        prev_frame = cur_frame
        cur_frame = next_frame

        # Grab the next frame
        next_frame = get_frame(cap,scaling_factor)

        # Check if the user pressed the ESC key
        key = cv2.waitKey(10)
        if key == 27:
            break
    
    # Close all windows
    cv2.destroyAllWindows()
