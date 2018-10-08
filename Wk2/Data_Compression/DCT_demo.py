'''
import math
import numpy as np
class DCT_Demo(object):
    def __init__(self, level):
        self.N = 8
        self.n = 8.0
        self.T = np.zeros((self.N, self.N), dtype='float_')
        self.Tt = np.zeros((self.N, self.N), dtype='float_')
        self.DCT = np.zeros((self.N, self.N), dtype='float_')
        self.TM = np.zeros((self.N, self.N), dtype='flat_')
        self.R = np.zeros((self.N, self.N), dtype='flat_')
        self.Q_Mat = np.zeros((self.N, self.N), dtype='int32')
        self.C = np.zeros((self.N, self.N), dtype='int32')
        self.fin = np.zeros((self.N, self.N), dtype='int32')

        self.Q50 = np.array([...])

        self.M = np.array([...])

        self.Qlevel = level
        self.Generate_T()
        self.CalculateQ()

    def Calculate_FDCT(self):

    def Calculate_IDCT(self):

    def CalculateQ(self):

    def Generate_T(self):

    def printMatrix(self):

    def QuantizationStepForward(self):

    def QuantizationStepInverse(self):

    def Compare(self):
    '''
