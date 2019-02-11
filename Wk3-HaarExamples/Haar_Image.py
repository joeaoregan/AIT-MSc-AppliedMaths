#https://homepages.cae.wisc.edu/~ece533/images/

import numpy as np
from PIL import Image
import requests
from io import BytesIO
import pywt as pw
import os
import matplotlib.pyplot as plt
from scipy.stats import norm

def LoadImageFromURL(url):
    """
        Make a  http request for an image, download and open the image
        giving information about its file format, image size and mode.
        Finially display the image.
    :param url:
    :return: image
    """
    image_url = url
    response = requests.get(image_url)
    #image = Image.open(BytesIO(response.content)).convert('LA') - To convert directly to grayscale
    image = Image.open(BytesIO(response.content))
    print ("Image acquired:")
    print ("Image Name: {0}".format(os.path.basename(image_url)))
    print ("Image Size: {0}".format(image.size))
    print ("Image Format: {0}".format(image.mode))
    return image

def LoadImageFromFile(fileName):
    """
        Read an image from a local file
    :param fileName:
    :return: image
    """
    image = Image.open(fileName)
    print(image.format, image.size, image.mode)
    return image

def convertTo2DArray(img):
    """
        Conver the image to a 2D gray scale image with grayscale values.
        Information about the array are printed to the user
    :param img:
    :return: 2d numpy array
    """
    #width, height = img.size
    grayImage =  img.convert('L')
    print((type(grayImage)))
    #imageMat = np.array(grayImage).reshape(width, height)
    imageMat = np.asanyarray(grayImage)
    print("\n=============================\n2D Array Details")
    print("Class:\t{0}\nSize:\t{1}\nDimensions:\t{2}".format(type(imageMat), np.size(imageMat), imageMat.shape))
    return imageMat

def Haar_dwt2D(img):
    """
        Preform a 2D Haar decomposition on an image
    :param imgArray (2D):
    :return:
    """
    titles = ['Approximation', ' Horizontal detail',
              'Vertical detail', 'Diagonal detail']
    coeffs2 = pw.dwt2(img, 'haar')
    LL, (LH, HL, HH) = coeffs2
    fig = plt.figure(figsize=(6, 6))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(2, 2, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout()
    plt.show()


def plotHistogrm(imgArray):
    """
    Ca
    :param imgArray:
    :return:
    """
    rows = np.size(imgArray, 0)
    cols = np.size(imgArray, 1)

    mu = np.mean(imgArray)
    sigma = np.std(imgArray)
    print("\n=============================\n2D Histogram Details")
    print("Mu: {0}\nSigma: {1}".format(mu, sigma))

    (mu1, sigma1) = norm.fit(imgArray)
    print("Scipy Fit\nMu: {0}\nSigma: {1}".format(mu1, sigma1))

    num_bins = 50
    fig, ax = plt.subplots()
    # the histogram of the data
    n, bins, patches = ax.hist(imgArray.ravel(), num_bins, density=1)
    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))

    ax.plot(bins, y, '--')
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Histogram of Lena: $\mu={0:0.2f}$, $\sigma={1:.2f}$'.format(mu, sigma))
    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.xlabel('Pixels')
    plt.ylabel('Probability')
    plt.show()

def main():
    print("2D Haar Example")
    url = 'https://homepages.cae.wisc.edu/~ece533/images/lena.png'
    fileName = 'Lena.png'
    img = LoadImageFromURL(url)
    #img = LoadImageFromFile(fileName)
    imgArray = convertTo2DArray(img)
    plotHistogrm(imgArray)
    Haar_dwt2D(imgArray)
    print('finished')

if __name__=='__main__':
    main()