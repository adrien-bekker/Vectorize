from PIL import Image, ImageColor
import numpy as np
from flask import Flask
from flask_cors import CORS

main = Flask("__name__")
CORS(main)

@main.route("/vectorize/<data>")
def vectorize(data):
    # Manipulating inputted colors into desired form
    separatedColors = []
    for i in range(0, len(data), 7):
        separatedColors.append(ImageColor.getcolor(data[i:i+7],"RGB"))

    # Importing image
    img = np.array(Image.open("./sample.png"), dtype="int64")

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

    # Combines colors into one image
    newImg = np.dstack((np.array(newImgRed, dtype="int64"), np.array(newImgBlue, dtype="int64"), np.array(newImgBlue, dtype="int64")))
    newImg = Image.fromarray(newImg.astype(np.uint8))
    newImg.save("./src/assets/vectorized.png")
    return "Done"

if __name__ == "__main__":
    main.run()