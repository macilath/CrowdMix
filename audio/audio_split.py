#!/usr/bin/python
from pydub import AudioSegment

print "Loading audio files..."
mars = AudioSegment.from_mp3("original/gustav_holst_the_planets_mars.mp3")
jupiter = AudioSegment.from_mp3("original/gustav_holst_the_planets_jupiter.mp3")
saturn = AudioSegment.from_mp3("original/gustav_holst_the_planets_saturn.mp3")
uranus = AudioSegment.from_mp3("original/gustav_holst_the_planets_uranus.mp3")

def slice_into_bits(song, song_name_str):
	print ("Splitting " + song_name_str + ", this may take some time...") 
	last_4_seconds = song[4000:]
	first_4_seconds = song[:4000]
	song_length = round(1000 * (song.frame_count() / song.frame_rate))
	
	#remember, milliseconds
	for i in range(4000, int(song_length), 4000):
		new_bit = song[i:i+4000]
		new_bit_name = "bits/" + song_name_str + str(i) + "-" + str(i+4000) + ".mp3"
		new_bit.export(new_bit_name, format="mp3")
	 
	last_bit_name = "bits/" + song_name_str + str(song_length - 4000) + "-" + str(song_length) + ".mp3"
	first_bit_name = "bits/" + song_name_str + str(0) + "-" + str(4000) + ".mp3"	
	last_4_seconds.export(last_bit_name, format="mp3")
	first_4_seconds.export(first_bit_name, format="mp3")
	return

slice_into_bits(mars, "mars")
slice_into_bits(jupiter, "jupiter")
slice_into_bits(saturn, "saturn")
slice_into_bits(uranus, "uranus")
