import cv2

# 读取图片
img = cv2.imread("qrcode.png")
# 创建QR检测器实例
detector = cv2.QRCodeDetector()
# 使用检测器检测数据并解码
# data 表示二维码数据
# bbox 表示二维码四边形顶点坐标数组
# straight_qrcode 表示校正后生成的二进制格式二维码
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"二维码的数据是：{data}")
    # 显示二维码图片的边线
    n_lines = len(bbox)  # 有几条线
    for i in range(n_lines):   # 两个点画一条线
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)  # opencv BGR

# 显示退出处理
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
