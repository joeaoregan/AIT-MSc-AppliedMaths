import numpy as np


class IntImage(object):
    def __init__(self, w, h, imageData):
        self.width = w
        self.height = h
        self.IImage = np.copy(imageData)
        self.II()

    def II(self):
        for r in range(1, self.width):
            self.IImage[r][0] += self.IImage[r-1][0]
        for c in range(1, self.height):
            self.IImage[0][c] += self.IImage[0][c-1]
        for r in range(1, self.width):
            for c in range(1, self.height):
                self.IImage[r][c]+=(self.IImage[r][c - 1] + self.IImage[r - 1][c]) - self.IImage[r - 1][c - 1];
        print(self.IImage)

    def CalculateSum(self, x, y, w, h):
        d = self.IImage[x+w][y+h]
        a = self.IImage[x][y]
        b = self.IImage[x][y+h]
        c = self.IImage[x+w][y]
        sum = d + a - b - c
        print(sum)


def main():
    image = np.random.randint(255, size=(8, 8))
    """image = [[69,34,13,168,203,193,187,49],
             [246,97,99,144,207,190,206,213],
             [247,61,207,147,239,84,28,233],
             [102,181,38,52,72,46,122,75],
             [170,185,39,112,19,241,81,8],
             [169,217,201,50,1,220,115,55],
             [35,214,5,7,170,163,114,123],
             [224,25,191,37,66,18,202,126]]"""
    print(image)
    ii = IntImage(8,8, image)
    area = ii.CalculateSum(1,1,4,4)

if __name__=="__main__":
    main()

