from PIL import Image, ImageDraw        # pip install Pillow
from functions import polar_to_decart


if __name__ == '__main__':
    # side = int(input())
    h = 800
    w = 600
    h_half = h / 2
    w_half = w / 2
    back = Image.new('RGB', (h, w))
    draw = ImageDraw.Draw(back)
    draw.line((h_half, 0) + (h_half, w), fill=(63, 127, 255))
    draw.line((0, w_half) + (h, w_half), fill=(63, 63, 255))
    step = 5
    for i in range(10000):
        point_pre_coordinates = polar_to_decart(i, i)
        point_coordinates = (point_pre_coordinates[0] +
                             h_half, point_pre_coordinates[1] + w_half)
        draw.point(point_coordinates, fill=(255, 255, 255))
    print(point_coordinates)

    back.show()
# add colouring for different rows or spirals
