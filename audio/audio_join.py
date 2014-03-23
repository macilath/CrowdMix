#!/usr/bin/python
import argparse
from pydub import AudioSegment

# Assume that we are building a clip progressively, that is, adding on to a clip previously made. 
# Except for the first time, of course

# Read the input files from the command line
# TODO: Option for crossfading (default=true)
parser = argparse.ArgumentParser(description="This script joins two MP3 Audio Files, and finalizes them if length is greater than 5 minutes.")
parser.add_argument('-p', '--primary', help="Primary File Name", required=True)
parser.add_argument('-a', '--addon', help="Add-on File Name", required=True)
args = parser.parse_args()

primary_file = args.primary
add_on_file = args.addon

# TODO: Error checking - see if bits/ is included in filename or not..
# Load audio files
base_audio = AudioSegment.from_mp3(primary_file)
add_on_audio = AudioSegment.from_mp3(add_on_file)

# TODO: Determine optimal crossfading
result_song = base_audio.append(add_on_audio, crossfade=2000)

# Determine length of song, if > 5 minutes, add to final folder
song_length = round(1000 * (result_song.frame_count() / result_song.frame_rate))
if song_length > 300000:
	result_song.export("final/final_song.mp3", format="mp3")
else:
	result_song.export("bits/building.mp3", format="mp3")
