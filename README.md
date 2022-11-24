# [EDU:BIT](https://www.cytron.io/p-edubit-training-and-project-kit-for-microbit?tracking=b-py) Extension for MicroPython
EDU:BIT is a beginner-friendly [micro:bit](https://www.cytron.io/p-micro-bit-board?tracking=b-py) kit specially designed to encourage kids to explore STEAM and learn coding.
This MicroPython library provides extension for [EDU:BIT Training & Project Kit for micro:bit](https://www.cytron.io/p-edubit-training-and-project-kit-for-microbit?tracking=b-py)
![enter image description here](https://my.cytron.io/image/cache/catalog/products/EDUBIT/EDUBIT-labels-800-lq-800x800.png)

**Python  editor  for micro:bit**

**Step 1: Open  Python Editor**

Open Python editor at: [https://python.microbit.org/v/3](https://python.microbit.org/v/3)

**Step  2:  Add module**

Download MicroPython module from GitHub: [https://github.com/Bhavithiran97/micropython-edubit](https://github.com/Bhavithiran97/micropython-edubit)

Click on the Project button in the editor
![1](https://user-images.githubusercontent.com/34527010/203694241-21b79e50-3cc3-4509-8689-19e81a590936.png)


Click Create file button and creaate 'edubit.py' file
![2](https://user-images.githubusercontent.com/34527010/203694225-62b59f16-ef46-4d5d-a6f7-7b9c4a8333fd.png)


Click Open button and add 'edubit.py' file
![3](https://user-images.githubusercontent.com/34527010/203694232-4045f5db-0243-4fe6-8f6f-3af727d49345.png)

Click the right button  in pop up and choose 'Replace file edubit.py'
![4](https://user-images.githubusercontent.com/34527010/203694236-a834704e-8162-44d7-970e-183ecddf7c03.png)

## **Add `from edubit import *` at the top of your program**

## RGB Bit

 - This kit has 4x NeoPixels (WS2812B programmable RGB LEDs)
   built-in.
 - EDU:BIT's built-in neopixel works with the default neopixel module that comes with 	  MicroPython on the BBC micro:bit.
 - Use `import neopixel` at the top of your program

Create a NeoPixel strip at pin P1 with 7 LEDs
```python
from edubit import *
import neopixel

np = neopixel.NeoPixel(pin13, 4)
```
Show color red on all RGB pixels
```python
from edubit import *
import neopixel

np = neopixel.NeoPixel(pin13, 4)
for LED in range(4):
	np[LED] = (255,0,0)
np.show()
```
Show specific color on each RGB pixels
```python
from edubit import *
import neopixel

np = neopixel.NeoPixel(pin13, 4)
#rainbow color
np[0]= 255,0,0    #red
np[1]= 255,255,0  #yellow
np[2]= 0,255,0    #green
np[3]= 75,0,130   #indigo
```
clear all RGB pixels
```python
np.clear()
```
**RGB values for commonly used colors**
 - red = 255,0,0
 - orange = 255,164,0
 - yellow = 255,255,0
 - green = 0,255,0
 - blue = 0,0,255
 - indigo = 75,0,130
 - violet = 138,43,226
 - purple = 255,0,255
 - white = 255,255,255
 - black = 0,0,0

Find more information about Neopixel's MicroPython module here: [https://microbit-micropython.readthedocs.io/en/latest/neopixel.html#module-neopixel](https://microbit-micropython.readthedocs.io/en/latest/neopixel.html#module-neopixel)

## Music Bit
 - EDU:BIT's built-in piezo buzzer works with the default music module that comes with 	  MicroPython on the BBC micro:bit.
 - Use `import music` at the top of your program

Play built-in melodies
```python
from edubit import *
import music

music.play(music.DADADADUM)
```
Play custom notes
```python
from edubit import *
import music

#starting tune of "Twinkle Twinkle Little Star"
tune=["C4:1","C4:1","G4:1","G4:1","A4:1","A4:1","G4:1"]
music.set_tempo(ticks=2)
music.play(tune)
```
## Digital IO

Read digital pin 9
```python
from edubit import *

while True:
    if pin9.read_digital():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
```

Write digital on pin 12
```python
from edubit import *

while True:
    pin12.write_digital(1)
    sleep(500)
    pin12.write_digital(0)
    sleep(500)
```
Find more information about analog MicroPython module here: [https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html#module-microbit](https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html#module-microbit)

## Analog IO

Read analog pin 1
```python
from edubit import *

while True:
    if pin1.read_analog() > 500:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
```
Write analog on pin 2
```python
from edubit import *

while True:
    pin12.write_analog(511)
```
Find more information about analog MicroPython module here: [https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html#pulse-width-modulation](https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html#pulse-width-modulation)

## DC Motors

```python
from edubit import *

while True:
	#Move forward at full speed
	run_motor(Motor_All, Direction_Forward, speed=255) 
	sleep(1000)
	
	#Move backward at half speed
	run_motor(Motor_All, Direction_Backward, speed=128) 
	sleep(1000)
	
	#Turn left at full speed
	run_motor(Motor_M1, Direction_Backward, speed=255 )
	run_motor(Motor_M2, Direction_Forward, speed=255 )
	sleep(1000)
	
	#Turn right at half speed
	run_motor(Motor_M1, Direction_Forward, speed=128 )
	run_motor(Motor_M2, Direction=Backward, speed=128 )
	sleep(1000)
	
	#Brake both motors
	brake_motor(Motor_All)
	sleep(1000)
```

## Servos

Rotate Servo 1 to 0 degree when button A is pressed, rotate Servo 1 to 180 degrees when button B is pressed, disable Servo 1 when button A+B pressed
```python
from edubit import *

while True:
	#Disable all servo when button A and B pressed
	if button_a.is_pressed() and button_b.is_pressed():
		disable_servo(Servo_All)
		
	#Set servo 1 to position 0 degree (min)
	elif button_a.is_pressed():
		sets_servo_position(Servo_S1, position=0 )
		
	#Set servo 1 to position 180 degree (max)
	elif button_b.is_pressed():
		sets_servo_position(Servo_S1, position=180 )
```
## Traffic Light Bit

Blink the all LEDs
```python
from edubit import *

while True:
	set_led(LED_All, 0)
	sleep(1000)
	set_led(LED_All, 1)
	sleep(1000)
```
Show running light on the LEDs.
```python
from edubit import *

while True:
	set_led(LED_Red, 1)
	set_led(LED_Yellow, 0)
	set_led(LED_Green, 0)
	sleep(200)
	set_led(LED_Red, 0)
	set_led(LED_Yellow, 1)
	set_led(LED_Green, 0)
	sleep(200)
	set_led(LED_Red, 0)
	set_led(LED_Yellow, 0)
	set_led(LED_Green, 1)
	sleep(200)
```
## Sound Bit

Show sound level
```python
from edubit import *

while True:
	display.scroll(read_sound_sensor())
```
Show sad face when it's too noisy
```python
from edubit import *

while True:
	if read_sound_sensor() > 512:
		display.show(Image.SAD)
```
Count claps
```python
from edubit import *

count = 0
while True:
	if read_sound_sensor() > 512:
		count += 1
		display.scroll(count)
```
## Potientio Bit

Show potentiometer value
```python
from edubit import *

while True:
	display.scroll(read_pot_value())
```
Show heart shape when the potentiometer is turned to the max
```python
from edubit import *

while True:
	if read_pot_value() > 1000:
		display.show(Image.HAPPY)
```
## IR Bit

Show the IR sensor state
```python
from edubit import *

while True:
	display.scroll(read_IR_sensor())
```
Show a target symbol when an object is detected
```python
from edubit import *

while True:
	if is_IR_sensor_triggered():
		display.show(Image.TARGET)
	else:
		display.clear()
```
## Power

Show power input voltage
```python
from edubit import *

while True:
	display.scroll(read_Vin())
```
Show sad face if the voltage is low
```python
from edubit import *

while True:
	if is_low_batt():
		display.show(Image.SAD)
```
Show sad face if over voltage
```python
from edubit import *

while True:
	if is_overvoltage():
		display.show(Image.SAD)
```
**Reset REKA:BIT**

Add `power_monitor()` function in a *while loop* to reset the REKA:BIT. 
The motors will not be reset after toggling if this function is not used because the PIC microcontroller in REKA:BIT will not reset without this function.
```python
from edubit import *

while True:
	power_monitor()
	run_motor(Motor_All, Direction_Forward, speed=255) 
	sleep(1000) 
```

