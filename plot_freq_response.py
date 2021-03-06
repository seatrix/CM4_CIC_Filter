#!/usr/bin/env python

import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sys

#Names of data and results folders, see makefile
test_temp_folder = "./test_temp/"
test_result_folder = "./test_results/"
#Names of data in/out file
infile = test_temp_folder + "freq.txt"
outfile = test_temp_folder +"freq_out.txt"
#Name of output image
plotfile = test_result_folder + "freq_resp.png"

def print_stderr(string):
    sys.stderr.write(string)
    sys.stderr.flush()

M = 100
length = 10000
n_steps = 400.0
A = 2000
A_rms = A / np.sqrt(2.0)

gains = []
freqs = np.linspace(0,0.4,n_steps)

#For each frequency
for freq in freqs:
    #Generate input data
    datain = A*np.sin(2*np.pi*freq*np.arange(length))
    np.savetxt("sin.txt", datain, "%d")

    #Call the thing
    subprocess.call("./test_cic %s %d 32 2 1" % ("sin.txt",M), shell=True)

    #Read the output data
    dataout = np.loadtxt("out.txt")

    gains.append(np.sqrt(np.mean(dataout**2))/A_rms) #Append RMS
    print_stderr(".")

plt.semilogy(freqs, gains)
plt.ylabel("Gain (dB)")
plt.xlabel("Normalised Frequency")
plt.savefig(plotfile)
#plt.show()
