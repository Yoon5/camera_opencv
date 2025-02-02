import cv2

capture = cv2.VideoCapture(0)
capture.set(3, 320)
capture.set(4, 240)

while True:
  ret, frame = capture.read()
  
  if ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) > 0: 
      break

capture.release()
cv2.destroyAllWindows()
