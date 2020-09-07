
# [EDU:BIT](https://www.cytron.io/p-edubit-training-and-project-kit-for-microbit?tracking=b-py) Extension for MicroPython
EDU:BIT is a beginner-friendly [micro:bit](https://www.cytron.io/p-micro-bit-board?tracking=b-py) kit specially designed to encourage kids to explore STEAM and learn coding.
This MicroPython library provides extension for [EDU:BIT Training & Project Kit for micro:bit](https://www.cytron.io/p-edubit-training-and-project-kit-for-microbit?tracking=b-py)
![enter image description here](https://my.cytron.io/image/cache/catalog/products/EDUBIT/EDUBIT-labels-800-lq-800x800.png)

## SOFTWARE SETUP

**MU EDITOR**

**Step 1: Download and install MU  editor**

Download MU editor at: [https://codewith.mu/en/download](https://codewith.mu/en/download)

Click on the downloaded file to install MU editor

**Step  2:  Add module**

Download MicroPython module from GitHub: [https://github.com/Bhavithiran97/micropython-edubit](https://github.com/Bhavithiran97/micropython-edubit)

Copy edubit.py file and paste it in your computer's mu_code folder
-   On Windows, the path is: C:\Users\<username>\mu_code
-   On Macintosh, the path is: Macintosh HD>Users>username>mu_code

![11](https://user-images.githubusercontent.com/34527010/92342452-7e01fc80-f0f3-11ea-8f7c-b4930f0fd36f.PNG)

![12](https://user-images.githubusercontent.com/34527010/92342454-7e9a9300-f0f3-11ea-9fa4-378d9f7ccee2.PNG)

Connect EDU:BIT to your computer using a USB cable and open MU editor.

Click in the Files button in the MU editor

![13](https://user-images.githubusercontent.com/34527010/92342457-7f332980-f0f3-11ea-9bee-8227931190a8.jpg)

A file panel will appear in the bottom of the editor
![14](https://user-images.githubusercontent.com/34527010/92342460-7f332980-f0f3-11ea-8eb3-6623a53c842b.PNG)

Drag and drop edubit.py from the right panel to left panel
![15](https://user-images.githubusercontent.com/34527010/92342447-7c383900-f0f3-11ea-8ea4-20e7ad4f876c.PNG)

**Python  editor  for micro:bit**

**Step 1: Open  Python Editor**

Open Python editor at: [https://python.microbit.org/v/2.0](https://python.microbit.org/v/2.0)

**Step  2:  Add module**

Download MicroPython module from GitHub: [https://github.com/Bhavithiran97/micropython-edubit](https://github.com/Bhavithiran97/micropython-edubit)

Click on the Load/Save button in the editor

![](https://hackster.imgix.net/uploads/attachments/1164090/6_BsE5rr4ssh.png?auto=compress%2Cformat&w=740&h=555&fit=max)

Click Show File (1) and Add file button

![](https://hackster.imgix.net/uploads/attachments/1164091/7_VLW2b9g3nf.png?auto=compress%2Cformat&w=740&h=555&fit=max)

Add edubit.py to the editor
![16](https://user-images.githubusercontent.com/34527010/92342562-c6b9b580-f0f3-11ea-8cae-24990d6f5fc3.PNG)

## RGB Bit

 - This kit has 4x NeoPixels (WS2812B programmable RGB LEDs)
   built-in.
 - EDU:BIT's built-in neopixel works with the default neopixel module that comes with 	  MicroPython on the BBC micro:bit.
 - Use `import neopixel` at the top of your program

Create a NeoPixel strip at pin P1 with 7 LEDs
```python
import neopixel
np = neopixel.NeoPixel(pin13, 4)
```
Show color red on all RGB pixels
```python
import neopixel
np = neopixel.NeoPixel(pin13, 4)
for LED in range(4):
	np[LED] = (255,0,0)
np.show()
```
Show specific color on each RGB pixels
```python
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
import music
music.play(music.DADADADUM)
```
Play custom notes
```python
import music
#starting tune of "Twinkle Twinkle Little Star"
tune=["C4:1","C4:1","G4:1","G4:1","A4:1","A4:1","G4:1"]
music.set_tempo(ticks=2)
music.play(tune)
```
Find more information about music MicroPython module here: [https://microbit-micropython.readthedocs.io/en/latest/music.html](https://microbit-micropython.readthedocs.io/en/latest/music.html)

***Add these lines for the following modules***
 - Use `from edubit import *` at the top of your program
 - Use `init()` inside a `while True` loop to monitor the power switch and reset microbit when power cycled.


## DC Motors

Run Motor 1 forward at 50% speed when button A is pressed, brake the motor when button B is pressed.
```python
from edubit import *
while True:
	init()
	if button_a.is_pressed():
		run_motor(M1,Forward, speed=128 )
	elif button_b.is_pressed():
		brake_motor(M1)
```

## Servos

Rotate Servo 1 to 0 degree when button A is pressed, rotate Servo 1 to 180 degrees when button B is pressed, disable Servo 1 when button A+B pressed
```python
from edubit import *
while True:
	init()
	if button_a.is_pressed() and button_b.is_pressed():
		disable_servo(S1)
	elif button_a.is_pressed():
		sets_servo_position(S1, position=0 )
	elif button_b.is_pressed():
		sets_servo_position(S1, position=180 )
```

## Traffic Light Bit

Blink the all LEDs
```python
from edubit import *
while True:
	init()
	set_led(All, 0)
	sleep(1000)
	set_led(All, 1)
	sleep(1000)
```
Show running light on the LEDs.
```python
from edubit import *
while True:
	init()
	set_led(Red, 1)
	set_led(Yellow, 0)
	set_led(Green, 0)
	sleep(200)
	set_led(Red, 0)
	set_led(Yellow, 1)
	set_led(Green, 0)
	sleep(200)
	set_led(Red, 0)
	set_led(Yellow, 0)
	set_led(Green, 0)
	sleep(200)
```
## Sound Bit

Show sound level
```python
from edubit import *
while True:
	init()
	display.scroll(read_sound_sensor())
```
Show sad face when it's too noisy
```python
from edubit import *
while True:
	init()
	if read_sound_sensor() > 512:
		display.show(Image.SAD)
```
Count claps
```python
from edubit import *
count = 0
while True:
	init()
	if read_sound_sensor() > 512:
		count += 1
		display.scroll(count)
```
## Potientio Bit

Show potentiometer value
```python
from edubit import *
while True:
	init()
	display.scroll(read_pot_value())
```
Show heart shape when the potentiometer is turned to the max
```python
from edubit import *
while True:
	init()
	if read_pot_value() > 1000:
		display.show(Image.HAPPY)
```
## IR Bit

Show the IR sensor state
```python
from edubit import *
while True:
	init()
	display.scroll(read_IR_sensor())
```
Show a target symbol when an object is detected
```python
from edubit import *
while True:
	init()
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
	init()
	display.scroll(read_Vin())
```
Show sad face if the voltage is low
```python
from edubit import *
while True:
	init()
	if is_low_batt():
		display.show(Image.SAD)
```
Show sad face if over voltage
```python
from edubit import *
while True:
	init()
	if is_overvoltage():
		display.show(Image.SAD)
```
