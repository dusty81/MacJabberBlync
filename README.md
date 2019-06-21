# MacJabberBlync
Mac Jabber Blync

After a corporate upgrade from Skype for Business to Jabber 12.x, my <a  href="https://embrava.com">Embrava Blync Light</a> stopped working. Needing a little practice with Python, I put together this script.   Nothing fancy nor complete.  More of a learning experience for me.

Requires:
- <a href='https://www.cisco.com/c/en/us/products/unified-communications/jabber/index.html'>Cisco Jabber</a> for Mac 12.6.0 (tested)
- Python 3.7.X (via <a href=https://brew.sh>Brew</a>)
- AppleScript
- HIDAPI (via <a href=https://brew.sh>Brew</a>)
- <a href="https://github.com/JnyJny/blynclight">blynclight</a> Python Module >= 0.4.7


I installed Python3 and HIDAP via Brew and then blynclight via pip3:
- brew install python3
- brew install hidapi
- pip3 install blynclight

How to run:
- Ensure that Jabber is open and running and the main Jabber window is open
- In the MacOS terminal execute, cd <DIR TO SCRIPT>; python3 ./jabber_status_watch.py
- <CONTROL+C> to exit

TODOs:
- Add verbose mode to enable / suppress output
- Add some command line options
- Make it easier to run / configure for end-users
- Figure out a wrapper to run at login
- Check to ensure Jabber is running prior to checking for Status
- 100 other things to learn on...
