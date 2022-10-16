import cv2

camera_port = 0
cameraCapture = cv2.VideoCapture(camera_port + cv2.CAP_DSHOW)    #设置摄像头端口
face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\Desktop\haarcascade_frontalface_default.xml')##导入人脸识别数据库

fps = 30##帧数
success, frame = cameraCapture.read() #获取摄像头数据  第一个参数表示帧是否捕捉成功，如果成功为True，否则为False
numFramesRemaining = 100 * fps
print(numFramesRemaining)
while success and numFramesRemaining > 0:
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y+ h), (123, 122, 55), 2)##xy表示左边的坐标，wh表示长度，RGB颜色，后面表示线的宽度
    cv2.imshow('frame_gray', frame)
    cv2.waitKey(1)
