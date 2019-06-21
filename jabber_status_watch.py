from subprocess import Popen, PIPE
from blynclight import BlyncLight, BlyncLightNotFound
import sys, signal, getopt
import datetime

def signal_handler(signal, frame):
    print("\nShutting down program...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

Full_Command_Line_Options = sys.argv
Arg_List = Full_Command_Line_Options[1:]
unixOptions = "ho:v"
gnuOptions = ["help", "output=", "verbose"]
verbosity = False

try:
    arguments, values = getopt.getopt(Arg_List, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
        print ("Verbose Output enabled...")
        verbosity = True
    elif currentArgument in ("-h", "--help"):
        print ("-v = Verbose output")
        sys.exit(0)

red, blue, green, yellow, purple = (255, 0, 0), (0, 255, 0), (0, 0, 255), (254, 220, 86), (153,0,255)
Status_Color = {"Available": green, "Away": yellow,"Busy": red,"On a Call": red, "Presenting": red, "In a meeting": red, "Do Not Disturb": purple}
Status_Flash = {"Available": False, "Away": False,"Busy": False,"On a Call": True, "Presenting": True, "In a meeting": True,"Do Not Disturb": False}
Status_Flash_Speed = {"Available": False, "Away": False,"Busy": False,"On a Call": "Fast", "Presenting": "Slow", "In a meeting": "Slow", "Do Not Disturb": False}

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
        if verbosity == True:
            print ("----------------------------------")
            print ("Jabber status changed from:",str(Previous_Jabber_Status)," to:",str(Current_Jabber_Status))
            print ("----------------------------------")
            now = datetime.datetime.now()
            print ("Time:",now.strftime("%Y-%m-%d %H:%M:%S"))
        Previous_Jabber_Status = Current_Jabber_Status
        # Need to catch if status is blank "" and default to a color.
        Light_Color = Status_Color.get(str(Current_Jabber_Status))
        Light_Flash = Status_Flash.get(str(Current_Jabber_Status))
        Light_Flash_Speed = Status_Flash_Speed.get(str(Current_Jabber_Status))
        #fix for issue 2, Type Error thrown when Jabber window is in the non-active "Space"
        try:
            light.on = True
            light.bright = True
            light.color= Light_Color
            light.flash = Light_Flash
            if verbosity == True:
                print ("Light Color:",str(Light_Color))
                print ("Light Flash:",str(Light_Flash))
                print ("Light Flash Speed:",str(Light_Flash_Speed))
                print ("Light Status:\n",str(light))
        except TypeError:
            if verbosity == True:
                print ("Jabber Window in the background space, so we can't pull the status. Continuing.")
            pass
