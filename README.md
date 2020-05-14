# Windows Audio Output Hotkey Changer

## About
Automatically change the audio output device using a hotkey.  
For headphones press the *Scroll Lock* key and for speakers *Pause*.  
Windows 10 support only. 

## How to run or compile
To run simply start

    dist/main.exe

To recompile use the pip environment included (pipenv) and type:

    pipenv shell
    pyinstaller -Fw .\main.py
    
## Pre-requisites
* Python
* Pipenv
* [Nircmd](https://www.nirsoft.net/utils/nircmd.html)

