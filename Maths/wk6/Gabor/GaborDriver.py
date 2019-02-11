from wk6.Gabor.Gabor_Student import D2GaborWavelet


def main():
    gab = D2GaborWavelet(75,0,0,1,1,501)
    gab.RunGabor()
    gab.ShowColourWavelet()
    gab.ShowGrayScaleWavelet()


if __name__=="__main__":
    main()
