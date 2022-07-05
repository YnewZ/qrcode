# 摄像头实时识别二维码
import cv2

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 初始化QR二维码的检测器
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    # 检测 解码
    data, bbox, _ = detector.detectAndDecode(img)
    # 标识二维码的外框，识别数据
    if bbox is not None:
        n_lines = len(bbox)  # 有几条线
        for i in range(n_lines):  # 两个点画一条线
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i + 1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)  # opencv BGR
    if data:
        print("数据是:", data)q
    cv2.imshow("Camera shooting", img)
    if cv2.waitKey(1) == ord("q"):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
