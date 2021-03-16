
from itertools import combinations
from PIL import Image, ImageDraw

RAINBOW = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white', 'black']
SPICED = ['#6e0096', '#aa0078', '#ff0000', '#ff6900', '#ffa028', '#ffffff']
GRAYSCALE = ['#000000', '#222222', '#444444', '#666666', '#888888', '#aaaaaa', '#cccccc', '#ffffff']

ASOHKA10 = [(80, 31, 17), (0, 13, 158), (138, 126, 117), (243, 224, 205), (59, 58, 54), (15, 18, 23), (228, 114, 70), (177, 153, 132), (104, 94, 87), (40, 45, 115)]

ASOHKA = [
 [0,  13, 158],
 [207,  99 , 65],
 [59,  54 , 55],
 [255, 199, 165],
 [115,  97 , 82],
 [21,  21 , 23],
 [89,  36 , 21],
 [254, 178, 124],
 [165, 146, 121],
 [248, 139 , 90],
 [38,  32 , 33],
 [251, 251, 235],
 [60,  18 , 11],
 [151,  80 , 42],
 [77,  72 , 65],
 [129, 124, 128],
 [23,  29 , 37],
 [92,  86 , 93],
 [50,  51 , 86],
 [104,  47 , 28],
 [144, 112, 100],
 [195, 160, 126],
 [141,  53 , 32],
 [2,   6  , 8],
 [62,  79 , 87],
 [29,  12  , 6],
 [254, 150, 104],
 [68,  62 , 58],
 [51,  51 , 49]]


def full(im, d, col, size):
    return im

def horizontal(im, d, col, size):
    d.rectangle((0, 0, size, size//2), col)
    return im

def vertical(im, d, col, size):
    d.rectangle((0, 0, size//2, size), col)
    return im

def diagonal1(im, d, col, size):
    d.polygon((0, 0, size, 0, 0, size), col)
    return im

def diagonal2(im, d, col, size):
    d.polygon((0, 0, size, size, 0, size), col)
    return im

def diamond(im, d, col, size):
    d.polygon((0, size//2, size//2, 0, size, size//2, size//2, size), col)
    return im

def inset(im, d, col, size):
    d.rectangle((size//4, size//4, size-size//4, size-size//4), col)
    return im

def generate_patterns(colors, func, size):
    for col1, col2 in combinations(colors, 2):
        im = Image.new('RGB', (size, size), color=col1)
        d = ImageDraw.Draw(im)
        func(im, d, col2, size)
        yield im

FULL = [full]
MOSAIC = [full, horizontal, vertical, diagonal1, diagonal2, diamond, inset]



def get_patterns(size, functions=MOSAIC, colors=RAINBOW):
    """
    Returns a list of pattern tiles of the given sizes.

    size      : an integer
    functions : a list of functions
    colors    : a list of color strings or hex codes
    """
    patterns = []
    for f in functions:
        patterns += list(generate_patterns(colors, f, size))
    return patterns
