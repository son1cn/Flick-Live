#!/usr/bin/env python3

import os
import sys
import time
import signal
import time
import threading

try:
    from osc4py3.as_eventloop import *
    from osc4py3 import oscbuildparse
except ImportError:
    exit("osc4py3 is not properly installed")


lib_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/modules/Flick/flick/')
sys.path.insert(0, lib_dir)
#print(lib_dir)

try:
    import flicklib
except ImportError:
    exit("Flick is not properly installed")

@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = start + ' - ' + finish
    
@flicklib.tap()
def tap(position):
    global taptxt
    taptxt = position

@flicklib.touch()
def touch(position):
    global touchtxt
    touchtxt = position
  
# Start the system.
osc_startup()

# Make client channels to send packets.
#Can use windows computer hostname instead of IP
osc_udp_client("NelsonL", 9000, "aLive")
#osc_udp_client("DESKTOP-AFDTU4J", 9000, "aLive")


#the tests below output just flick, touch and tap messages to the stdout window using print
touchtxt = ''
touchcount = 0
taptxt = ''
tapcount = 0
flickupcount = 0
flickdowncount = 0
track = 0
flicktxt = ''
sendlvl = 0.0
try:
    while True:
        #flick test
        if flicktxt:
            os.system('clear')
            print(flicktxt)
            if flicktxt == "south - north" and flickupcount <3:
                flickupcount += 1
            elif flickupcount == 3:
                if sendlvl < 1.0:
                    sendlvl += 0.1
                #increase sendlvl by 10% and send to Ableton
                msg0 = oscbuildparse.OSCMessage("/live/send", ",iif", [track, 0, sendlvl])
                msg1 = oscbuildparse.OSCMessage("/live/send", ",iif", [track, 1, sendlvl])
                bun = oscbuildparse.OSCBundle(oscbuildparse.unixtime2timetag(time.time()),
                    [msg0, msg1])
                print("Increasing track " , track , " to " , sendlvl)
                #print("Live should be playing")
                #msg just to play
                #msg = oscbuildparse.OSCMessage("/live/play", None, ["play"])
                osc_send(bun, "aLive")
                osc_process()
                flicktxt = ''
                flickupcount = 0
            if flicktxt == "north - south" and flickdowncount <3:
                flickdowncount += 1
            elif flickdowncount == 3:
                if sendlvl > 0.0:
                    sendlvl -= 0.1
                #decrease sendlvl by 10% and send to Ableton
                msg0 = oscbuildparse.OSCMessage("/live/send", ",iif", [track, 0, sendlvl])
                msg1 = oscbuildparse.OSCMessage("/live/send", ",iif", [track, 1, sendlvl])
                bun = oscbuildparse.OSCBundle(oscbuildparse.unixtime2timetag(time.time()),
                    [msg0, msg1])
                print("Decreasing track " , track , " to " , sendlvl)
                #print("Live should be playing")
                #msg just to play
                #msg = oscbuildparse.OSCMessage("/live/play", None, ["play"])
                osc_send(bun, "aLive")
                osc_process()
                flicktxt = ''
                flickdowncount = 0
        time.sleep(0.2)
        #tap test
        if taptxt:
            os.system('clear')
            print(taptxt)
        if len(taptxt) > 0 and tapcount < 5:
            tapcount += 1
        else:
            taptxt = ''
            tapcount = 0
except KeyboardInterrupt:
    exit(0)

#old Link testing
touchtxt = ''
touchcount = 0
taptxt = ''
tapcount = 0
flickcount = 0
flicktxt = ''

l = link.Link(120)
l.enabled = True
l.startStopSyncEnabled = True

try:
  while True:
    s = l.captureSessionState()
    link_time = l.clock().micros();
    tempo_str = '{0:.2f}'.format(s.tempo())
    beats_str = '{0:.2f}'.format(s.beatAtTime(link_time, 0))
    playing_str = str(s.isPlaying())
    phase = s.phaseAtTime(link_time, 4)
    phase_str = ''
    for x in range(0, 4):
      if x < phase:
        phase_str += 'X'
      else:
        phase_str += '0'
    os.system('clear')
    sys.stdout.write(
      'tempo ' + tempo_str + ' | playing: ' + playing_str + ' | beats ' + beats_str
      + ' | ' + phase_str + '  \r')
    sys.stdout.flush()
    time.sleep(0.2)
    #tap test
    if taptxt:
        os.system('clear')
        print(taptxt)
    if len(taptxt) > 0 and tapcount < 5:
        tapcount += 1
    else:
        taptxt = ''
        tapcount = 0
    print(taptxt)
    
    if taptxt:
        os.system('clear')
        print(taptxt)
        if taptxt == 'center':
            if not s.isPlaying():
                print("Should be playing")
                s.setIsPlaying(True, link_time)  
                print("should go up to 140bpm")
                s.setTempo(140, link_time)
                l.commitSessionState(s)
            else:
                print("Stopping playback")
                s.setIsPlaying(False, link_time)  
                print("should go to 120bpm")
                s.setTempo(120, link_time)
                l.commitSessionState(s)
    if len(taptxt) > 0 and tapcount < 5:
        tapcount += 1
    else:
        taptxt = ''
        tapcount = 0
        
except KeyboardInterrupt:
    exit(0)  
    

#the tests below output just flick, touch and tap messages to the stdout window using print
touchtxt = ''
touchcount = 0
taptxt = ''
tapcount = 0
flickcount = 0
flicktxt = ''
try:
    while True:
        #flick test
        if flicktxt:
            os.system('clear')
            print(flicktxt)
        time.sleep(0.2)
        if len(flicktxt) > 0 and flickcount < 5:
            flickcount += 1
        else:
            flicktxt = ''
            flickcount = 0
        #touch test    
        if touchtxt:
            os.system('clear')
            print(touchtxt)
        if len(touchtxt) > 0 and touchcount < 5:
            touchcount += 1
        else:
            touchtxt = ''
            touchcount = 0
        #tap test
        if taptxt:
            os.system('clear')
            print(taptxt)
        if len(taptxt) > 0 and tapcount < 5:
            tapcount += 1
        else:
            taptxt = ''
            tapcount = 0
except KeyboardInterrupt:
    exit(0)
    

