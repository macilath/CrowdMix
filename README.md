# CrowdMix


## Where Turkers Mix Things Up

Our project is an experimentation into the musical knowledge and preferences of a crowd of workers. This project, given a set of musical tracks as input, will rely on turkers to produce a new song by piecing together snippets from the input tracks.


Built on Python 2.7.6

This project requires the following libraries:
+ [boto](https://github.com/boto/boto)
+ [pydub](https://github.com/jiaaro/pydub/)

### Creating the HIT
In order to create the HIT, use the Python script 'AMTscript.py' in the 'amt' directory. This script should wait for the HIT to be reviewable, and then accept or reject accordingly. If for some reason the script is interrupted and closes early, run 'AMTpay.py' in the 'amt' directory. 

### Website
Our system uses a website/webserver to handle everything a turker does during their assignment. The files in the 'web' directory will need to be added to your own webserver that has CGI and Python enabled. The index of the webpage will be at '/cgi-bin/welcome.py'.
