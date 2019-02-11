#Simple script to calculate the Signal to Noise Ratio (SNR) based on
#the Shannon-Hartley theorm.
import math as m
C = float(input("Enter the channel capacity in bps: "))
B = float(input("Enter the available bandwidth in Hz: "))
SN = m.pow(2.0, (C/B))-1
SNR = 10*m.log10(SN)
print('Signal to Noise Ratio = %f db ' %SNR)
print('Signal to Noise Ratio = %s db ' %format(SNR, '0.3E'))
 
