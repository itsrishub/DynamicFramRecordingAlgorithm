#TODO: its not saving the recorded frame, will implement savinf of video file later.


import cv2


cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

prev_frame = None
curr_frame = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    fgmask = fgbg.apply(frame)
    thresh = 10000

    fgcount = cv2.countNonZero(fgmask)

    if fgcount > thresh:
        prev_frame = curr_frame
        curr_frame = frame
        cv2.imshow('Recorded Frame', curr_frame)
        cv2.putText(frame, "Recording", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Not recording", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
