from PIL import Image, ImageDraw, ImageColor        # pip install Pillow
from functions import polar_to_descartes


if __name__ == '__main__':
    # side = int(input())
    h = 800
    w = 600
    h_half = h / 2
    w_half = w / 2
    back = Image.new('RGB', (h, w))
    draw = ImageDraw.Draw(back)
    draw.line((h_half, 0) + (h_half, w), fill=(63, 127, 255))
    draw.line((0, w_half) + (h, w_half), fill=(63, 63,  255))
    step = 5
    for i in range(1000):
        point_pre_coordinates = polar_to_descartes(i, i)
        point_coordinates = (point_pre_coordinates[0] +
                             h_half, point_pre_coordinates[1] + w_half)
        k = i % 6
        print(60*k)
        draw.point(point_coordinates, fill=f'hsl({60 * k}, 100%, 50%)')
    back.show()
# add colouring for different rows or spirals based on % remainder
