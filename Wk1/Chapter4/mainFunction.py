#!/usr/bin/env python3

# Lecture 2 Python Introduction S103

import math as m

def CalculateChannelCapacity(B, SNR):
    SN = m.pow(10.0,SNR/10.0)
    C = B*((m.log(1+SN))/(m.log(2)))
    print("Calculation Complete")
    return C


def main():
    B = float(input("Enter the available Bandwith in Hz:"))
    SNR = float(input("Enter the SNR in dB:"))
    C = CalculateChannelCapacity(B,SNR)
    print('Channel Capacity = %f bps' %C)
    print('Channel Capacity = %s bps' %format(C,'0.3E'))


if __name__ == "__main__":
    main()
