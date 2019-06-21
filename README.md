# MacJabberBlync
Mac Jabber Blync

After a corporate upgrade from Skype for Business to Jabber 12.x, my <a  href="https://embrava.com">Embrava Blync Light</a> stopped working. Needing a little practice with Python, I put together this script.   Nothing fancy nor complete.  More of a learning experience for me.

Requires:
- Python 3.7.X
- AppleScript
- HIDAPI
- <a href="https://github.com/JnyJny/blynclight">blynclight</a> Python Module >= 0.4.7


I installed Python3 and HIDAP via Brew.  Then pyhidapi and blynclight via pip3:
- brew install python3
- brew install hidapi
- pip3 install blynclight

TODOs:
- Add verbose mode to suppress output
- Add some command line options
- Figure out a wrapper to run at login
- Check to ensure Jabber is running prior to checking for Status
- 100 other things to learn on...
