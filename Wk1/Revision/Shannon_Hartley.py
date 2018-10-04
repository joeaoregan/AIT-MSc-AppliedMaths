# Simple script to calculate the channel capacity based on
# the Shannon-Hartley theorem

import math as m
B = float(input("Enter the available Bandwidth in Hz: "))
SNR = float(input("Enter the SNR in dB: "))
SN = m.pow(10.0,SNR/10.0)
C = B*((m.log(1+SN))/(m.log(2)))
print('Channel Capacity = %f bps' %C)
print('Channel Capacity = %s bps' %format(C, '0.3E'))
