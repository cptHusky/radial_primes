from PIL import Image, ImageDraw, ImageFont        # pip install Pillow
from functions import *

STEP = 0.1
RANGE = 10000


if __name__ == '__main__':
    primes = prime_gen(RANGE)
    # side = int(input())
    h = 800
    w = 800
    h_half = h / 2
    w_half = w / 2
    back = Image.new('RGB', (w, h))
    draw = ImageDraw.Draw(back)
    text = ImageDraw.Draw(back)
    draw.line((w_half, 0) + (w_half, h), fill=(63, 127, 255))
    draw.line((0, h_half) + (w, h_half), fill=(63, 63,  255))
    # font!!!!!
    for i in range(RANGE):
        font = ImageFont.FreeTypeFont(font='OpenSans-Light.ttf', size=int(i/5))
        point_pre_coordinates = polar_to_descartes(i, i)
        point_coordinates = (point_pre_coordinates[0] * STEP +
                             w_half, point_pre_coordinates[1] * STEP + h_half)
        text_coordinates = (point_coordinates[0], point_coordinates[1] + 10)
        text.text(text_coordinates, str(i), font=font)
        k = i % 6
        draw.point(point_coordinates, fill=f'hsl({60 * k}, 100%, 50%)')
    point_coordinates = (w_half, h_half)
    back.show()
# add colouring for different rows or spirals based on % remainder
