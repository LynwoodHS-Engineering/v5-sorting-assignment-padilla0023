#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
pot = Encoder(brain.three_wire_port.a)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       Guillermo Padilla
#   Created:
#   Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
def update_display():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Potentiometer Value:")
    brain.screen.set_cursor(2, 1)
    brain.screen.print(pot.value())
    brain.screen.set_pen_color(Color.RED)
    brain.screen.draw_circle(230, 50, int(pot.value() / 4095 * 460), 20)
while True:
    update_display()
    wait(100, MSEC)
