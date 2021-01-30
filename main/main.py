import numpy.distutils.system_info
import pydirectinput

# stop program if mouse at a corner of the screen?
# useful for testing, but default = False
safeMode = False

if safeMode:
    pydirectinput.FAILSAFE = True
else:
    pydirectinput.FAILSAFE = False


while 1:
    pydirectinput.keyDown('scrolllock')

