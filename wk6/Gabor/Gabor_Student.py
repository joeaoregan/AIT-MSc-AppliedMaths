import math
import numpy as np
from numpy import arange, cos, pi, exp, power
from PIL import Image
# from matplotlib.pyplot import plot, draw, show, ion
import matplotlib as ml
import matplotlib.pyplot as plt


class D2GaborWavelet(object):

    def __init__(self, l, t, v, u, b, sze):
        self.lamda = l
        self.theta = t / (180 / math.pi)        #Convert to Rads
        self.varphi = v / (180 / math.pi)   #convert to Rads
        self.upsi = u
        self.bandW = b
        self.kappa = (2 * math.pi) / self.lamda
        self.sigma = self.CalculateSigma()
        self.size = sze
        self.gaussian = sze / 2
        self.GaborGrid = np.zeros((self.size, self.size))
        self.GaborNormGrid = np.zeros((self.size, self.size))
        self.PrintParameters()

    def PrintParameters(self):
        print("--------------------------------------------")
        print("Parameters Accepted")
        print("Image Size: \t\t%s x %s" % (self.size, self.size))
        print("Wavelength:\t\t%s" % ("{:10.2f}".format(self.lamda)))
        print("Orientation:\t%s" % ("{:10.2f}".format(self.theta * (180 / math.pi))))
        print("Phase Offset:\t%s" % ("{:10.2f}".format(self.varphi * (180 / math.pi))))
        print("Aspect Ratio:\t%s" % ("{:10.2f}".format(self.upsi)))
        print("Bandwidth:\t\t%s" % ("{:10.2f}".format(self.bandW)))
        print("Kappa:\t\t\t%s" % ("{:10.5f}".format(self.kappa)))
        print("Sigma:\t\t\t%s" % ("{:10.5f}".format(self.sigma)))

    def CalculateSigma(self):
        B = (1 / math.pi) * (0.588705011) * ((math.pow(2, self.bandW) + 1) / (math.pow(2, self.bandW) - 1))
        self.sigma = B * self.lamda
        print("Sigma: %f\nBandwidth: %f" % (self.sigma, B))
        return self.sigma

    def GetKappaSigma(self):
        data = (self.kappa, self.sigma)
        return data

    def RunGabor(self):
        """
            Use the code provided along with your notes, published papers and
            references available on the internet to code the Gabor equation to
            generate a 2D Gabor wavelet.  The data to construct the wavelet must
            be stroed in the GaborGrid 2D array
        :return:
        """

    def GetNormGaborWavelet(self):
        """
            Use the code provided along with your notes and sources availalbe on the
            internet to code normalise the GaborGrid 2darray.  The result should be stored
            in the GaborNorGrid 2darray
        :return: GaborNormGrid
        """
        return self.GaborNormGrid

    def ShowGrayScaleWavelet(self):
        img = Image.fromarray(self.GetNormGaborWavelet().astype('uint8'), 'L')
        img.show()
        img.save('Test.png')

    def ShowColourWavelet(self):
        print("here")
        fig = plt.figure(figsize=(11, 3.75))

        ay = fig.add_subplot(1, 2, 1)
        x = arange(-self.size, self.size, 1)
        ay.set_xlim([-self.size, self.size])
        ay.set_ylim([-1.2, 1.2])
        ay.set_title('Gabor Wavelet - 1D')
        ay.plot(x, np.exp(-(np.power(x, 2) / (2 * np.power(self.sigma, 2)))) * np.cos(2 * np.pi * (x / self.lamda) + self.varphi))
        ax = fig.add_subplot(1, 2, 2)
        ax.set_title('Gabor Wavelet - 2D')
        plt.imshow(self.GaborGrid)
        ax.set_aspect('equal')

        plt.colorbar(orientation='vertical')
        plt.show()

