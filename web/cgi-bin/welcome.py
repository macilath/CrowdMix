#!/usr/bin/env python
from os import path
import glob
import shutil
import random
import string

#Purpose: This page first runs a python script to select 4 random mp3s from the SRC_FOLDER.
#Then it auto-generates all 16 combinations and saves them in the SAVE_FOLDER.
#HTML is then generated which passes all 20 of these filenames to the next page by POST

#GLOBALS 
SRC_FOLDER = '../turk/chunks/'
SAVE_FOLDER = '../turk/temp_chunks/'
FILES = []
COMBINED_FILES = []

def addHiddenTag(name, value):
	return '<input type="hidden" name="' + name + '" value="' + value + '" />'

def nameWOExt(filename):
	#hack - assumes all .mp3 so just cut off the last 4 characters
	return filename[:-4]

def rand_subset(n, ls):
  #may choose the same object twice if the list is too small
  #n must not be larger than ls
  if(n > len(ls)):
    n = len(ls)
  return [random.choice(ls) for i in range(0,n)]

def rand_string(length = 10):
  #taken from 'https://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits'
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def get_filenames(folder, pattern):
  #ex: get_filenames('C:/Documents and Settings', '*.txt')
  return glob.glob(path.join(folder, pattern))

def concatMP3(file1, file2, output_filename):
  #writes the output to the location which is output_filename
  #does not modify file1, file2
  destination = open(output_filename,'wb')
  shutil.copyfileobj(open(file1,'rb'), destination)
  shutil.copyfileobj(open(file2,'rb'), destination)
  destination.close()

def select_chunks():
  #chooses 4 not-necessarily-unique mp3s, which are < 5 min. from 
  #TODO - only choose <5 min clips
  all_filenames = get_filenames(SRC_FOLDER, '*.mp3')
  return rand_subset(4, all_filenames)

def gen_all_combinations(save_path, filenames):
    combined_filenames = []
    #2 levels of loops is correct - we want all orderings which is n^2
    for file1 in filenames:
      for file2 in filenames:
        #concat the mp3's into rslt_name, then store the string rslt_name
        rslt_name = save_path + rand_string() + '.mp3'
        concatMP3(file1, file2, rslt_name)
        combined_filenames.append(rslt_name)
    return combined_filenames

#-------------------------- Python Main - executes all the code above to set GLOBALs
FILES = select_chunks()
COMBINED_FILES = gen_all_combinations(SAVE_FOLDER, select_chunks())

#-------------------------- HTML generation
print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Welcome!</title>
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }
    </style>
    <link href="../bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../bootstrap/assets/js/html5shiv.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="jumbotron">
    <h1>Welcome!</h1>
    <p class="lead">This website requires HTML5 and javascript. If you have problems try updating or switching browsers.</p>
    <form action="combine2.php" method="POST" /> """

#add a ton of hidden fields to this form which was the whole point of this page
for i, v in enumerate(FILES + COMBINED_FILES):
	print "      ", addHiddenTag(str(i), v)

print """\
      <input type="hidden" name="group1" value="0">
      <input type="hidden" name="group2" value="0">
      <input class="btn btn-large btn-success" type="Submit" value="Get Started" />
    </form>
    </div>
    <!-- Javascript that makes the CSS work -->
    <script src="../bootstrap/assets/js/jquery.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-transition.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-alert.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-modal.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-dropdown.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-scrollspy.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-tab.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-tooltip.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-popover.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-button.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-collapse.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-carousel.js"></script>
    <script src="../bootstrap/assets/js/bootstrap-typeahead.js"></script>
  </body>
</html>
"""
