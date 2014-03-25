#!/usr/bin/env python

# ---------------Insert python code gen stuff here

code = "FILL IN THIS VAR WITH YOUR CODE GEN SCRIPT RESULT"

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
      <p>More instructions go here - tell them to go back to the turk page & fill it in to get credit</p>
    </div>
  </body>
</html>
"""