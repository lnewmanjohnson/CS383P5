import numpy as np
import imageio

if __name__ == "__main__":
    img = imageio.imread("final\\birds.png")
    height, width, channels = img.shape
    print ("Height:", height, "Width:", width, "Number of Channels:", channels)
    
    for r in range(height):
        for c in range(width):
        	for channel in range(0, 4):
        		if (img[r, c][channel] % 2 == 1):
        			img[r, c][channel] = 128
        		else:
        			img[r, c][channel] = 0

    imageio.imwrite("TestOut.png", img)