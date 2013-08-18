import ImageGrab
img = ImageGrab.grab()
img.save('test.jpg','JPEG')

with open("test.jpg", "rb") as f:
    data = f.read()
    print data.encode("base64")