# flick-link
 Flick setup to Ableton Link

## Get:
```
git clone --recursive https://github.com/son1cn/Flick-link.git
```
##Build
Flick requires root to install
```
sudo ./install.sh
```

Ableton Link is not the tool that we need. We need to emulate something that Live can see over the network. After much Googling, it seems finding a working implementation of OpenSoundControl (OSC from now on) using the correct version of python.

Flick requires python 3.7.3, 3.8 doesn't seem to work

Installing osc4py3 manually
https://pypi.org/project/osc4py3/
```
pip3 install osc4py3
```
https://osc4py3.readthedocs.io/en/latest/userdoc.html#simple-use

LiveOSC for MIDI control in Ableton Live
https://github.com/ideoforms/LiveOSC
*Needs to be installed on Live PC (not the Pi)

List of OSC commands
https://github.com/ideoforms/LiveOSC/blob/master/OSCAPI.txt





