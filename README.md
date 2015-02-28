# TekTronix-TDS2024C-usbtmc-com_cntrl-
TekTronix TDS2024C Oscillioscope USB Communication and Control using Python

I found another git repo with code for a Tektronix TDS2024B Oscillioscope. However the implementation was for serial 
based communication over ttyS0. I needed to use a TDS2024C over usbtmc0. Fortunately he also had usb code for an 
aglient waveform generator. So I used the USB wrapper and modded his code to work via usbtmc0. I also found some code 
from another guy who was hacking a different brand of scope but using the same Python based approach and borrowed/moded some code for making Matlab like plots of the data as well as some code for saving the data as csv files. 

The example top level usage script reads all 4 channels of data at the same time and then saves each channel's data as 
a csv file and then shows a Matlab like plot of all 4 channels.

I would like to be able to set and manipulate the trigger signal parameters. Also it would be nice to be able to set the parameters for the Measure functions as well. Also stop/run and single button functions would be nice. A python 
or Qt gui would be nice too.

The original code I used can be found here:

http://markjones112358.co.nz/projects/Python-Controlled-Oscilloscope/

https://github.com/markjones112358/pyInstruments

What I really need to know is where did this guy get all of the command string names from, maybe from a proprietary 
software dev kit for LabView or Matlab. Prolly a C or C++ implementation. For example:

  self.write("ACQuire:MODe AVERage")
  self.write("ACQuire:NUMAVg " + str(averages))

This sets the acquisition mode to averaging (as opposed to sample or peak detect) and sets the number of averages.
The parts I'm interested in are: "ACQuire:MODe AVERage" and "ACQuire:NUMAVg " I need to find out all of the various 
control strings so that I can fully control all of the features of the scope.


