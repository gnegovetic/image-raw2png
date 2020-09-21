# image-raw2png

This script converts a raw image that is saved as 32BPP (32-bit word per pixel) into a PNG image. Supported color modes are RGBA and CMYK.
Raw files don't have any headers, just pixel data, so image dimensions have to be specified. Image width times height must be equal to the number of 32-bit words in the raw file:
### Raw file size = (height x width x 4) bytes 

# Example usage:

python raw2png.py -input=rgba_256x176.raw -width=256 -height=176
