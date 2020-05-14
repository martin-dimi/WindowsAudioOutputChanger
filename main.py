import os
from pynput import keyboard

def activateHeadphones():
    os.system('nircmd setdefaultsounddevice "Speakers" 1')

def activateSpeakers():
    os.system('nircmd setdefaultsounddevice "C27JG5x" 1')

def on_press(key):
    if key == keyboard.Key.scroll_lock:
        activateHeadphones()
    elif key == keyboard.Key.pause:
        activateSpeakers()

with keyboard.Listener(on_press=on_press) as Listener:
    Listener.join()