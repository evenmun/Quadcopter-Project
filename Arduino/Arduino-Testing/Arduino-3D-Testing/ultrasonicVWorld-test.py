


#import serial
from visual import *; #import vPython

scene = display(title='Ultrasonic Sentor test',autoscale=False); #This will create the scene for the 3D-view

scene.width = 900;
scene.height = 800;
scene.range = (15,15,15);

box = box(length=1, width=10, height=5, pos=(-6,0,0));


while True:
    rate(25);