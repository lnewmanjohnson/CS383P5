
import numpy as np
import imageio
import binascii
if __name__ == "__main__":
    img = imageio.imread("final\\lewisStructureBonds.png")
    height, width, channels = img.shape
    print ("Height:", height, "Width:", width, "Number of Channels:", channels)

    string = ""
    array = []
    for row in range(height):
    	for column in range(width):
    		array.append(img[row, column][0] % 2)
    		array.append(img[row, column][1] % 2)
    		array.append(img[row, column][2] % 2)


    #print (string)
    
    file = open("testOutput.txt", "w")


    valueErrorCount = 0
    count = 1
    for i in range(0, len(array), 8):
    	byteList = bytes(array[i:i + 8])
    	bitString = ""
    	for bit in byteList:
    		bitString += str(bit)
    	intByte = int(bitString, 2)
    	text = bytes([intByte]).decode("ISO-8859-1")
    	if (ord(text) < 128):
    		string += text
    		count += 1

    print(string)


    file.write(string)