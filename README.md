# DJITelloPy
DJI Tello drone python interface using the official [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) and [Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf). Yes, this library has been tested with the drone. 
Please see [example.py](https://github.com/damiafuentes/TelloSDKPy/blob/master/example.py) for a working example controlling the drone as a remote controller with the keyboard and the video stream in a window.  

Tested with Python 3.6, but it also may be compatabile with other versions.

Feel free to contribute!

## Install through git clone
```
$ pip install --upgrade pip
$ git clone https://github.com/damiafuentes/TelloSDKPy.git
$ cd TelloSDKPy
$ pip install -r requirements.txt
(use sudo if package not found)
```
Sometimes you need to update the virtual environment indexes and skeletons in order for the `example.py` file to work with `pygame`. If you are working with PyCharm, this can be done to ```File > Invalidate Caches```

## ~~Install through pip~~
**DEPRECATED**: The python package at PyPi library is not maintained anymore. I would recommend to install it through ``git clone``.
```
$ pip install djitellopy
```

## install pyenv (if system python version unsupported)
* run pyenv_install.sh (for raspberry pi)
* add to .bashrc (or .zshrc)
```sh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
* install and use specific python version (recommend 3.6.10)
```sh
# example
#  -install (this will last a few minute)
pyenv install 3.6.10
#  -use
pyenv shell 3.6.10
```
* other usage of pyenv
```sh
# check installed python versions
pyenv versions 

# check currently used version
pyenv version
# or
python --version
```

## Install on Raspberry Pi
* install pyenv and run python 3.6.10 (see above)
* install missing packages:
```sh
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libatlas3-base libjasper1 libqtgui4 libqt4-test
```
* install dependency:
```sh
sudo pip3 install -r requirement.txt
```
* troubleshooting:
  * if libxxx.so.xx missing:
```sh
sudo apt-get install apt-file
apt-file update
apt-file search libxxx.so.xx
```


## Usage

### Simple example

```python
from TelloSDKPy.djitellopy import Tello
import cv2
import time

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(45)

tello.land()
tello.end()
```

### Example using pygame and the video stream
Please see [example.py](https://github.com/damiafuentes/TelloSDKPy/blob/master/example.py). 

The controls are:
- T: Takeoff
- L: Land
- Arrow keys: Forward, backward, left and right.
- A and D: Counter clockwise and clockwise rotations
- W and S: Up and down.

### Swarm example
Only for Tello EDU's.
```python
from TelloSDKPy.djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.178.42",
    "192.168.178.43",
    "192.168.178.44"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(100)

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_forward(i * 20))

# making each tello do something unique in parallel
swarm.parallel(lambda i, tello: tello.move_left(i * 100))

swarm.land()
swarm.end()
```

### Notes
- If you are using the ```streamon``` command and the response is ```Unknown command``` means you have to update the Tello firmware. That can be done through the Tello app.
- Mission pad detection and navigation is only supported by the Tello EDU.
- Connecting to an existing wifi network is only supported by the Tello EDU.
- When connected to an existing wifi network video streaming is not available.

## Author

* **Damià Fuentes Escoté** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/damiafuentes/TelloSDKPy/blob/master/LICENSE) file for details

