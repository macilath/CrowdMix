#!/usr/bin/env python
#import cgi
#import cgitb; cgitb.enable()  # for troubleshooting, TODO rm during deployment, major security flaw

from pydub import AudioSegment

print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>"""
print "Loading audio files..."

mars = AudioSegment.from_wav("../turk/source_music/gustav_holst_the_planets_mars.wav")
jupiter = AudioSegment.from_wav("../turk/source_music/gustav_holst_the_planets_jupiter.wav")
saturn = AudioSegment.from_wav("../turk/source_music/gustav_holst_the_planets_saturn.wav")
uranus = AudioSegment.from_wav("../turk/source_music/gustav_holst_the_planets_uranus.wav")

def slice_into_bits(song, song_name_str):
	print ("Splitting " + song_name_str + ", this may take some time...") 
	last_4_seconds = song[4000:]
	first_4_seconds = song[:4000]
	song_length = round(1000 * (song.frame_count() / song.frame_rate))
	
	#remember, milliseconds
	for i in range(4000, int(song_length), 4000):
		new_bit = song[i:i+4000]
		new_bit_name = "../turk/chunks/" + song_name_str + str(i) + "-" + str(i+4000) + ".wav"
		new_bit.export(new_bit_name, format="wav")
	 
	last_bit_name = "../turk/chunks/" + song_name_str + str(song_length - 4000) + "-" + str(song_length) + ".wav"
	first_bit_name = "../turk/chunks/" + song_name_str + str(0) + "-" + str(4000) + ".wav"	
	last_4_seconds.export(last_bit_name, format="wav")
	first_4_seconds.export(first_bit_name, format="wav")
	return

slice_into_bits(mars, "mars")
slice_into_bits(jupiter, "jupiter")
slice_into_bits(saturn, "saturn")
slice_into_bits(uranus, "uranus")

print "Done"
print """\
  </body>
</html>"""