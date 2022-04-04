from PIL import Image, ImageDraw        # use pip install Pillow


if __name__ == '__main__':
    # side = int(input())
    side = 800
    back = Image.new('RGB', (side, side))
    h = back.height
    w = back.width
    h_half = back.height / 2
    w_half = back.width / 2
    draw = ImageDraw.Draw(back)
    draw.line((h_half, 0) + (h_half, w), fill=128)
    draw.line((0, w_half) + (h, w_half), fill=128)
    back.show()
    # print(f'{back.size}\n{type(back.size)}')
