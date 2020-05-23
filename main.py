import os
from pynput import keyboard

HEADPHONES = 0
SPEAKERS = 1

currentDevice = HEADPHONES

def activateHeadphones():
    os.system('nircmd setdefaultsounddevice "Speakers" 1')

def activateSpeakers():
    os.system('nircmd setdefaultsounddevice "C27JG5x" 1')

def getCurrentOutputDevice():
    os.system('nircmd Get-DefaultAudioDevice')

def on_press(key):
    global currentDevice, HEADPHONES, SPEAKERS
    if key == keyboard.Key.pause:
        if(currentDevice == HEADPHONES):
            activateSpeakers()
            currentDevice = SPEAKERS
        else:
            activateHeadphones()
            currentDevice = HEADPHONES

with keyboard.Listener(on_press=on_press) as Listener:
    Listener.join()

