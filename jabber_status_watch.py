from subprocess import Popen, PIPE
from blynclight import BlyncLight, BlyncLightNotFound
import sys, signal
import datetime

def signal_handler(signal, frame):
    print("\nShutting down program...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

red, blue, green, yellow, purple = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (153,0,255)
Status_Color = {"Available": green, "Away": yellow,"Busy": red,"On a Call": red, "Presenting": red, "In a meeting": red, "Do Not Disturb": purple}
Status_Flash = {"Available": False, "Away": False,"Busy": False,"On a Call": True, "Presenting": True, "In a meeting": True,"Do Not Disturb": False}
Status_Flash_Speed = {"Available": False, "Away": False,"Busy": False,"On a Call": "Fast", "Presenting": "Slow", "In a meeting": "Slow", "Do Not Disturb": "Slow"}

Previous_Jabber_Status = "NONE"
Current_Jabber_Status = ""

try:
    light = BlyncLight.get_light()
except BlyncLightNotFound as error:
        print(f"{error}")
        exit(-1)

while (True):
    script = '''
        tell application "System Events" to tell process "Cisco Jabber"
            get value of text field 1 of window "Cisco Jabber"
        end tell'''
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)

    Current_Jabber_Status = str(stdout).strip()

    if Previous_Jabber_Status != Current_Jabber_Status :
        print ("----------------------------------")
        print ("Jabber status changed from:",str(Previous_Jabber_Status)," to:",str(Current_Jabber_Status))
        print ("----------------------------------")
        Previous_Jabber_Status = Current_Jabber_Status
        now = datetime.datetime.now()
        print ("Time:",now.strftime("%Y-%m-%d %H:%M:%S"))
        # Need to catch if status is blank "" and default to a color.
        Light_Color = Status_Color.get(str(Current_Jabber_Status))
        Light_Flash = Status_Flash.get(str(Current_Jabber_Status))
        Light_Flash_Speed = Status_Flash_Speed.get(str(Current_Jabber_Status))

        print ("Light Color:",str(Light_Color))
        print ("Light Flash:",str(Light_Flash))
        print ("Light Flash Speed:",str(Light_Flash_Speed))

        light.on = True
        light.bright = True
        light.color= Light_Color
        light.flash = Light_Flash

        print ("Light Status:\n",str(light))
