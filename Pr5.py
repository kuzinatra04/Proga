from PIL import Image, ImageDraw
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

rectangle_width = width * 0.4
rectangle_height = height * 0.3
rectangle_position = ((width - rectangle_width) / 2, (height - rectangle_height) / 2)
draw.rectangle((rectangle_position, (rectangle_position[0] + rectangle_width, rectangle_position[1] + rectangle_height)), fill=random_color())

draw.polygon(((width * 0.1, height * 0.1), (width * 0.2, height * 0.2), (width * 0.3, height * 0.3), (width * 0.1, height * 0.3)), fill=random_color())

ellipse_width = width * 0.4
ellipse_height = height * 0.4
ellipse_position = ((width - ellipse_width) / 4, (height - ellipse_height) / 4)
draw.ellipse((ellipse_position, (ellipse_position[0] + ellipse_width, ellipse_position[1] + ellipse_height)), fill=random_color())

image.save("original_image.png")

filtered_image = Image.open('original_image.png')
pixels = filtered_image.load()
x, y = filtered_image.size

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = 255 - r, 255 - g, 255 - b

filtered_image.save("filtered_image.png")
