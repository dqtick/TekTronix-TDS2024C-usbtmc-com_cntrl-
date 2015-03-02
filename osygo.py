import tds2024Cusb
import numpy
import matplotlib.pyplot as plot
import tds2024Cusb
import numpy
import matplotlib.pyplot as plot

scope = tds2024Cusb.tek2024('/dev/usbtmc0')

channel1 = tds2024Cusb.channel(scope,1)
channel2 = tds2024Cusb.channel(scope,2)
channel3 = tds2024Cusb.channel(scope,3)
channel4 = tds2024Cusb.channel(scope,4)

scope.set_hScale(frequency=800000, cycles=1)  # Set the time scale to the mimimum that contains 1 waveforms
scope.set_averaging(0)                        # Set the scope to do 0X averaging
channel1.set_vScale(0.2)                      # Set the voltage scale to 200mV
channel2.set_vScale(0.2)                      # Set the voltage scale to 200mV
channel3.set_vScale(0.2)                      # Set the voltage scale to 200mV
channel4.set_vScale(2)                        # Set the voltage scale to 2V

data_adc_d_p = channel1.get_waveform()                         # Download the waveform from channel 1
data_adc_clk_p = channel2.get_waveform(wait=False)      # Download the waveform from channel 2
data_adc_cnv_p = channel3.get_waveform(wait=False)      # Download the waveform from channel 3
data_adc_osmp = channel4.get_waveform(wait=False)       # Download the waveform from channel 4

fig = plot.figure(figsize=(15.75,11.25))
plot.title("Oscilloscope Channels 1-4")
plot.ylabel("Voltage (V)\n")
plot.xlabel("Time (Sec)")
ax1 = fig.add_subplot(411,axisbg =(0.85, 0.85, 0.85))
ax1.plot(data_adc_d_p[0], data_adc_d_p[1], color='yellow')
ax1.grid(True)
#ax1.axhline(0, color='blue', lw=2)
ax2 = fig.add_subplot(412, sharex=ax1, axisbg =(0.85, 0.85, 0.85)) 
ax2.plot(data_adc_clk_p[0], data_adc_clk_p[1], color='cyan')
ax2.grid(True)
#ax2.axhline(0, color='cyan', lw=2)
ax3 = fig.add_subplot(413, sharex=ax1, axisbg =(0.85, 0.85, 0.85))
ax3.plot(data_adc_cnv_p[0], data_adc_cnv_p[1], color='magenta')
ax3.grid(True)
#ax3.axhline(0, color='magenta', lw=2)
ax4 = fig.add_subplot(414, sharex=ax1, axisbg =(0.85, 0.85, 0.85))
ax4.plot(data_adc_osmp[0], data_adc_osmp[1], color='green')
ax4.grid(True)
#ax4.axhline(0, color='green', lw=2)

f = open( 'data_adc_d_p.py', 'w' )
f.write( 'data_adc_d_p = ' + repr(data_adc_d_p) + '\n' )
f.close()

f = open( 'data_adc_clk_p.py', 'w' )
f.write( 'data_adc_clk_p = ' + repr(data_adc_clk_p) + '\n' )
f.close()

f = open( 'data_adc_cnv_p.py', 'w' )
f.write( 'data_adc_cnv_p = ' + repr(data_adc_cnv_p) + '\n' )
f.close()

f = open( 'data_osmp.py', 'w' )
f.write( 'data_osmp = ' + repr(data_adc_osmp) + '\n' )
f.close()

plot.show()
