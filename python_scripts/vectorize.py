from PIL import Image
import numpy as np
import os

# Manipulating inputted colors into desired form
data = "0,0,0,255,255,255"

print(os.getcwd())

colors = data.split(",")
separatedColors = []
for i in range(0, len(colors), 3):
    separatedColors.append(colors[i:i+3])
print(separatedColors)
# Importing image
img = np.array(Image.open("./drincrop.png"), dtype="int64")

# Creating new image
newImg = []
newImgRed = []
newImgGreen = []
newImgBlue = []
newImgRedRow = []
newImgGreenRow = []
newImgBlueRow = []

for r in range(img.shape[0]):
    for c in range(img.shape[1]):
        # Greater than the Euclidean distance between black and white
        lowestColorDifference = 445
        currentColor = -1
        for color in separatedColors:
            currentColorDifference = 0
            for z in range(3):
                currentColorDifference += (img[r][c][z] - int(color[z]))**2
            currentColorDifference = currentColorDifference ** 0.5
            if currentColorDifference < lowestColorDifference:
                lowestColorDifference = currentColorDifference
                closestColor = color

        # Adds closest color to newImgRows
        newImgRedRow.append(int(closestColor[0]))
        newImgGreenRow.append(int(closestColor[1]))
        newImgBlueRow.append(int(closestColor[2]))

    # Adds rows to newImgs
    newImgRed.append(newImgRedRow)
    newImgGreen.append(newImgGreenRow)
    newImgBlue.append(newImgBlueRow)
    newImgRedRow = []
    newImgGreenRow = []
    newImgBlueRow = []

print(closestColor)
print(np.array(newImgBlueRow).shape)
print(np.array(newImgRed).shape)
print(img.shape[1])

# Combines colors into one image
newImg = np.dstack((np.array(newImgRed, dtype="int64"), np.array(newImgBlue, dtype="int64"), np.array(newImgBlue, dtype="int64")))
Image.fromarray(newImg.astype(np.uint8)).show()