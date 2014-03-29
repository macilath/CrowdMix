#!/usr/bin/python

import random
import string
import shutil
from pydub import AudioSegment

# Assume that we are building a clip progressively, that is, adding on to a clip previously made. 
# Except for the first time, of course

#This file gets imported so the 2 parameters are the names of the input files
#finalizing is a separate function as that is only done after the user makes a selection. All combinations are made before the user makes a selection

def randString(length = 10):
  #taken from 'https://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits'
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def joinWAV(primary_file, add_on_file, rslt_path):
#All 3 parameters are full relative or absolute paths with extensions e.g. "../a/b/name.wav"
# Load audio files
  base_audio = AudioSegment.from_wav(primary_file)
  add_on_audio = AudioSegment.from_wav(add_on_file)
# TODO: Determine optimal crossfading
  result_song = base_audio.append(add_on_audio, crossfade=2000)
  result_song.export(rslt_path, format="wav")

def finalize(filepath):
# Determine length of song, if > 5 minutes, add to final folder, else move it to the chunks folder
  result_song = AudioSegment.from_wav(filepath)
  song_length = round(1000 * (result_song.frame_count() / result_song.frame_rate))
  if song_length > 300000:
    result_song.export("../turk/completed_remixes/" + randString() + "_final.wav", format="wav")
  else:
    result_song.export("../turk/chunks/" + randString() + ".wav", format="wav")