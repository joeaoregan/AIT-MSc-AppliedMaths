from DCT import DCT_Demo

def main():
    value = int(input("\n\n\nSelect Quantisation Level"
                      " (integer values only): "))
    print("{0} is a {1}" .format(value, type(value)))
    dct = DCT_Demo(value)
    print("\n\nData to be compressed:")
    dct.printMatrix(dct.M, 1)
    dct.Calculate_FDCT()
    dct.QuantizationStepForward()
    print("\n\nCompressed Message")
    dct.printMatrix(dct.C, 0)
    print("\n\nDecompressed Message")
    dct.QuantizationStepInverse()
    dct.Calculate_IDCT()
    dct.printMatrix(dct.fin, 1)
    dct.Compare()

if __name__=="__main__":
    main()
