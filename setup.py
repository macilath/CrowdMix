#!/usr/bin/python

# Sets up the CrowdMix project
import os
import sys

# Install dependencies
print ("CrowdMix requires the following dependencies: \nFFMPEG & libavcodec-extra-53, pip, boto, and pydub")
print ("CrowdMix can install these for you, using apt-get and pip, or you can install them manually.")
print ("Do you want CrowdMix to install these dependencies? (You will need to be a sudo-er.)")
ans = raw_input('[Y/N]: ')
if ans == 'Y' or ans == 'y':
	# ffmpeg & libavcodec-extra-53(apt-get)
#	os.system("sudo apt-get install ffmpeg")
#	os.system("sudo apt-get install libavcodec-extra-53")
	os.system("sudo apt-get install python-pip")
	# boto (pip)
	os.system("sudo pip install boto")
	# pydub (pip)
	os.system("sudo pip install pydub")
else: 
	print ("Okay, skipping that.")

print ("\n")
# Add AMT credentials

# Add website hostname

# Call to audio splitter
os.system("cd audio && python audio_split.py")

# Call to Turk poster

# Verification stuff, posting of bits on webpage, etc.
