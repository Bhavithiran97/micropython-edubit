from microbit import *
from utime import sleep_ms

I2C_ADDRESS = 0x08

REG_ADD_REVISION = 0
REG_ADD_SERVO_1 = 1
REG_ADD_SERVO_2 = 2
REG_ADD_SERVO_3 = 3
REG_ADD_M1A = 4
REG_ADD_M1B = 5
REG_ADD_M2A = 6
REG_ADD_M2B = 7
REG_ADD_LB_UTH = 8
REG_ADD_LB_LTH = 9
REG_ADD_OV_TH = 10
REG_ADD_VIN = 11
REG_ADD_PWR_STATE = 12
REG_ADD_LB_STATE = 13
REG_ADD_OV_STATE = 14

S1 = REG_ADD_SERVO_1
S2 = REG_ADD_SERVO_2
S3 = REG_ADD_SERVO_3

M1 = 0
M2 = 1
All = 1000

Forward = 0
Backward = 1

Red = pin14
Yellow = pin15
Green = pin16

SOUND_BIT_PIN = pin1
POTENTIO_BIT_PIN = pin2
IR_BIT_PIN = pin8

flag = 0

def limit(value,min,max):
    if value < min:
        value = min
    elif value > max:
        value = max
    return value

def i2cRead(register):
    buf = bytearray(1)
    buf[0] = register
    value = 0
    i2c.write(I2C_ADDRESS,buf,True)
    value = i2c.read(I2C_ADDRESS,1)
    #value = int.from_bytes(value, "little")
    return value[0]

def i2cWrite(register,data):
    buffer = bytearray(2)
    buffer[0] = register
    buffer[1] = data
    i2c.write(I2C_ADDRESS,buffer)


def init():
    global flag
    global oldPowerState


    if flag == 0:
        oldPowerState = is_power_on()
        flag = 1

    if is_power_on():
        if oldPowerState == False:
            brake_motor(M1)
            brake_motor(M2)
            disable_servo(S1)
            disable_servo(S2)
            disable_servo(S3)
            reset()
        oldPowerState = True
    else:
        oldPowerState = False
    sleep_ms(200)

def brake_motor(motorChannel):
    if motorChannel == M1:
        i2cWrite(REG_ADD_M1A, 0)
        i2cWrite(REG_ADD_M1B, 0)

    elif motorChannel == M2:
        i2cWrite(REG_ADD_M2A, 0)
        i2cWrite(REG_ADD_M2B, 0)

    elif motorChannel == All:
        i2cWrite(REG_ADD_M1A, 0)
        i2cWrite(REG_ADD_M1B, 0)
        i2cWrite(REG_ADD_M2A, 0)
        i2cWrite(REG_ADD_M2B, 0)

def run_motor(motorChannel,direction,speed):
    speed = limit(speed,0,255)
    if motorChannel == M1:
        if direction == Forward:
            i2cWrite(REG_ADD_M1A,speed)
            i2cWrite(REG_ADD_M1B,0)
        else:
            i2cWrite(REG_ADD_M1A,0)
            i2cWrite(REG_ADD_M1B,speed)
    elif motorChannel == M2:
        if direction == Forward:
            i2cWrite(REG_ADD_M2A,speed)
            i2cWrite(REG_ADD_M2B,0)
        else:
            i2cWrite(REG_ADD_M2A,0)
            i2cWrite(REG_ADD_M2B,speed)
    elif motorChannel == All:
        if direction == Forward:
            i2cWrite(REG_ADD_M1A,speed)
            i2cWrite(REG_ADD_M1B,0)
            i2cWrite(REG_ADD_M2A,speed)
            i2cWrite(REG_ADD_M2B,0)
        else:
            i2cWrite(REG_ADD_M1A,0)
            i2cWrite(REG_ADD_M1B,speed)
            i2cWrite(REG_ADD_M2A,0)
            i2cWrite(REG_ADD_M2B,speed)

def disable_servo(servo):
    if servo == All:
        i2cWrite(S1,0)
        i2cWrite(S2,0)
        i2cWrite(S3,0)
    else:
        i2cWrite(servo,0)

def sets_servo_position(servo,position):
    position = limit(position,0,180)

    pulseWidth = int(position * 20 / 18 + 50)
    if servo == All:
        i2cWrite(S1,pulseWidth)
        i2cWrite(S2,pulseWidth)
        i2cWrite(S3,pulseWidth)
    else:
        i2cWrite(servo,pulseWidth)

def is_power_on():
    if i2cRead(REG_ADD_PWR_STATE) != 0:
        return True
    else:
        return False

def is_low_batt():
    if i2cRead(REG_ADD_LB_STATE) != 0:
        return True
    else:
        return False

def is_overvoltage():
    if i2cRead(REG_ADD_OV_STATE) != 0:
        return True
    else:
        return False

def read_Vin():
    return i2cRead(REG_ADD_VIN) / 10

def set_led(color,state):
    if color == Red:
        Red.write_digital(state)
    if color == Yellow:
        Yellow.write_digital(state)
    if color == Green:
        Green.write_digital(state)
    if color == All:
        Red.write_digital(state)
        Yellow.write_digital(state)
        Green.write_digital(state)

def read_sound_sensor():
    return SOUND_BIT_PIN.read_analog()

def read_pot_value():
    return POTENTIO_BIT_PIN.read_analog()

def read_IR_sensor():
    return IR_BIT_PIN.read_digital()

def is_IR_sensor_triggered():
    if IR_BIT_PIN.read_digital() != 0:
        return True
    else:
        return False
