# This script converts a raw image that is saved as 32BPP (32-bit word per pixel) into a PNG image. 
# Supported color modes are RGBA and CMYK.
# Raw files don't have any headers, just pixel data, so image dimensions have to be specified.
# Image width times height must be equal to the number of 32-bit words in the raw file:
# Raw file size = (height x width x 4) bytes 

import numpy as np
from PIL import Image   # install from Pillow
import argparse

def raw2png(rawFile, pngFile, width, height, colors):
    try:
        

        if colors not in ['RGBA', 'CMYK']:
            raise ValueError('Color mode not supported.')

        # must be 4 bytes per pixel
        bin = np.fromfile(rawFile, np.uint32) 

        # do we have the correct size
        if bin.size != (width * height):
            raise Exception('Data size mismatch')

        # See http://jehiah.cz/a/creating-images-with-numpy
        pilImage = Image.frombuffer(colors, (width, height), bin, 'raw', colors, 0, 1)
        pilImage.save(pngFile)

        print('Output file generated: ' + pngFile)

    except Exception as e:
        print('Error: ' + str(e))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''Converts raw image into PNG.
        Example usage: python bin2img.py -input rgba_256x176.raw -width=256 -height=176''')
    parser.add_argument('-input', type=str, default=None, required=True, help='Input file')
    parser.add_argument('-output', type=str, default='out.png', required=False, help='Output image file, for example out.png')
    parser.add_argument('-width', type=int, required=True, help='Image width')
    parser.add_argument('-height', type=int, required=True, help='Image height')
    parser.add_argument('-colors', type=str, default='RGBA', help='Colors')

    args = parser.parse_args()

    # do the conversion
    raw2png(args.input, args.output, args.width, args.height, args.colors)


## In MATLAB/Octive
#   124 cd h:\work\data
#   125 dir
#   126 fid=fopen('data.bin', 'r');
#   127 a=fread(fid, 'uint8=>uint8');
#   128 r=a(1:4:end);
#   129 g=a(2:4:end);
#   130 b=a(3:4:end);
#   132 alpha=a(4:4:end);
#   133 size(alpha)
#   134 ri=reshape(r,[720 480]);
#   135 gi=reshape(g,[720 480]);
#   136 bi=reshape(b,[720 480]);
#   137 ai=reshape(alpha, [720 480]);
#   138 im=zeros(480,720,4,'uint8');
#   139 im(:,:,1)=ri';
#   140 im(:,:,2)=gi';
#   141 im(:,:,3)=bi';
#   142 im(:,:,4)=ai';
#   143 imshow(im)
#   146 imwrite(im, 'data4.bmp');
#   147 exit
#   148 # Octave 3.2.4, Mon Oct 07 21:20:17 2019 Pacific Daylight Time <unknown@unknown>
