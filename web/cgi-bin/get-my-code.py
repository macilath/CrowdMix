#!/usr/bin/env python

import audio_join
import random
import cgi
import os
import cgitb; cgitb.enable()  # for troubleshooting - TODO disable during deployment. showing your internals is a major security flaw

def deleteIfThere(file):
 	if os.path.isfile(file):
		os.remove(file)

form = cgi.FieldStorage()

#--------Saving the result
choice_made = form.getvalue("choice_made")
audio_join.finalize(choice_made)

#--------Delete all the temp files
for i in range(20):
	deleteIfThere(form.getvalue(str(i)))

# ---------------Code Gen - give them one from a pre-selected set

codeset = ["CG6H5","X38T1","S1W59","D2K9K","DCURP","KJHCY","KSSIZ","YYLMB","47NQK","WILIM"]
code = random.choice(codeset)

#----------------------------------HTML GEN
print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Here's Your Code!</title>
    <!-- <link rel="stylesheet" href="style.css"> -->
  </head>
  <body> 
    <div align="center">
    <h1>Your code is:"""
print code
print """</h1>
      <p>You're done! Now, go back to Amazon mechanical turk to claim your reward!</p>
    </div>
  </body>
</html>
"""