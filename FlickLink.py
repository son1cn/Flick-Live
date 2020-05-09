#!/usr/bin/env python3

import os
import sys
import time
import signal
import time
#probably unecessary
import curses
from curses import wrapper

lib_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/modules/link-python/lib/')
sys.path.insert(0, lib_dir)
#print(lib_dir)

try:
    import link
except ImportError:
    exit("Link is not properly installed")


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


while True:
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
    sys.stdout.write(
      'tempo ' + tempo_str + ' | playing: ' + playing_str + ' | beats ' + beats_str
      + ' | ' + phase_str + '  \r')
    sys.stdout.flush()
    time.sleep(0.02)
except KeyboardInterrupt:
    pass

