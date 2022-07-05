import qrcode   # qrcode5.3

# 数据
data = "abcdefghijklmnopqrstuvwxyz"
# 文件
filename = "qrcode.png"
# 生成二维码
img = qrcode.make(data)
# 保存文件
img.save(filename)
