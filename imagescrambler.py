from PIL import Image


def josephus(data, s, k):
    final = []
    pointer = None

    pointer = data.index(s)

    while len(data) != 1:

        pointer += k

        while pointer > len(data)-1:
            pointer -= len(data)

        temp = data.pop(pointer)
        final.append(temp)
    temp = data.pop()
    final.append(temp)
    return final


# cipher = josephus([1, 2, 3, 4, 5, 6], 1, 4)
# print(cipher)


def scramble(fileName):
    data = []
    image = Image.open(fileName)
    width, height = image.size
    pixels = image.load()
    new_image = Image.new(image.mode, image.size)
    new_image_pix = new_image.load()

    for i in range(width):
        for j in range(height):
            data.append((i, j))

    data = josephus(data, (0, 0), 100)
    # print(data)

    count = -1
    for i in range(0, (image.size)[0]):
        for j in range(0, (image.size)[1]):
            count += 1
            w = data[count][0]
            h = data[count][1]
            new_image_pix[i, j] = pixels[w, h]

    new_image.show()
    new_image.save('scrambeld.png')


file = ""  # Enter the file name here
scramble(file)
