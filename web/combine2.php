<?php
//Reading relevant POST variables
$sel1 = $_POST['group1'];
$sel2 = $_POST['group2'];
$combo_num = 4 * intval($sel1) + intval($sel2) + 4; //4x4 index calculation, +4 to get past the 4 uncombined pieces
$song1 = $_POST['0'];
$song2 = $_POST['1'];
$song3 = $_POST['2'];
$song4 = $_POST['3'];
$current_combo = $_POST[strval($combo_num)];
$reload_count = $_POST['reload_count'];
//
echo '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Combine 2 Music Clips and Get Paid!</title>
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 700px;
      }
      .container-narrow > hr {
        margin: 30px 0;
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
    <link href="bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="bootstrap/assets/js/html5shiv.js"></script>
    <![endif]-->
  </head>
  <body>
    <!-- instructions -->
    <div align="center">
    <h1>Instructions</h1>
    <p> On this webpage, you will be given four random sound bits to listen to.<br> 
After listening to all of the clips, you will choose two clips, using the radio buttons, that sound appealing to you.<br> These two clips will be combined and added with other clips to make a new song.<br> 
When you have selected two clips using the radio buttons below, click the Load My New Choice button to confirm your selection.<br>
When you are satisfied with your choices and you have already clicked the Load My New Choice button, click the Submit My Decision and Get My Code! button.<br>
After clicking the Submit button, you will be given a code to input in to the box on the Amazon Mechancial Turk HIT page.<br> Once you have put the code in box, submit the hit and wait for approval.<br>
<br><span style="color: red;">If the clips are not loading and you used the Back/Forward button on your browser, click the welcome link again: <a href = "http://www.crowdmix.net/cgi-bin/welcome.py">CrowdMix Welcome</a></span><br></p>
    </div>
    
    <!-- Music Clips -->
    <div align="center">
    <h2>Music Clips</h2><br>
    <p>Music Clip #0: <br>
    <audio controls>
      <source src="';
echo $song1;
echo '" type="audio/wav">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip #1: <br>
    <audio controls>
      <source src="';
echo $song2;
echo '" type="audio/wav">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip #2: <br>
    <audio controls>
      <source src="';
echo $song3;
echo '" type="audio/wav">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip #3: <br>
    <audio controls>
      <source src="';
echo $song4;
echo '" type="audio/wav">
      Your browser does not support this audio format.
    </audio>
    </div>
    
    <div class="row-fluid marketing">
    
    <div class="span6">
    <!-- Music Clip selection boxes -->
    <form action="combine2.php" method="POST" /> 
    <h2>Your First Music Clip Selection</h2><br>
    <input type="radio" name="group1" value="0"> 0<br>
    <input type="radio" name="group1" value="1"> 1<br>
    <input type="radio" name="group1" value="2"> 2<br>
    <input type="radio" name="group1" value="3"> 3<br>
    </div>

    <div class="span6">
    <h2>Your Second Music Clip Selection</h2><br>
    <input type="radio" name="group2" value="0"> 0<br>
    <input type="radio" name="group2" value="1"> 1<br>
    <input type="radio" name="group2" value="2"> 2<br>
    <input type="radio" name="group2" value="3"> 3<br>
    </div>
    
    </div>';
echo "    <input type=\"hidden\" name=\"0\" value=\"".$_POST['0']."\" />
    <input type=\"hidden\" name=\"1\" value=\"".$_POST['1']."\" />
    <input type=\"hidden\" name=\"2\" value=\"".$_POST['2']."\" />
    <input type=\"hidden\" name=\"3\" value=\"".$_POST['3']."\" />
    <input type=\"hidden\" name=\"4\" value=\"".$_POST['4']."\" />
    <input type=\"hidden\" name=\"5\" value=\"".$_POST['5']."\" />
    <input type=\"hidden\" name=\"6\" value=\"".$_POST['6']."\" />
    <input type=\"hidden\" name=\"7\" value=\"".$_POST['7']."\" />
    <input type=\"hidden\" name=\"8\" value=\"".$_POST['8']."\" />
    <input type=\"hidden\" name=\"9\" value=\"".$_POST['9']."\" />
    <input type=\"hidden\" name=\"10\" value=\"".$_POST['10']."\" />
    <input type=\"hidden\" name=\"11\" value=\"".$_POST['11']."\" />
    <input type=\"hidden\" name=\"12\" value=\"".$_POST['12']."\" />
    <input type=\"hidden\" name=\"13\" value=\"".$_POST['13']."\" />
    <input type=\"hidden\" name=\"14\" value=\"".$_POST['14']."\" />
    <input type=\"hidden\" name=\"15\" value=\"".$_POST['15']."\" />
    <input type=\"hidden\" name=\"16\" value=\"".$_POST['16']."\" />
    <input type=\"hidden\" name=\"17\" value=\"".$_POST['17']."\" />
    <input type=\"hidden\" name=\"18\" value=\"".$_POST['18']."\" />
    <input type=\"hidden\" name=\"19\" value=\"".$_POST['19']."\" />
    <input type=\"hidden\" name=\"reload_count\" value=\"".($reload_count+1)."\" />
    <div class=\"jumbotron\">
    ";
echo '    <input class="btn btn-large btn-success" type="submit" value="Load My New Choice" />
    </div>
    </form>
    
    <!-- combined Music Clip player -->
    <div align="center">
    <h2>Combined Music Clip - ';
echo '#'.$sel1.' + #'.$sel2;
echo '</h2><br>
    <audio controls>
      <source src="';
echo $current_combo;
echo '" type="audio/wav">
      Your browser does not support this audio format.
    </audio>
    </div>
    
    <!-- submit button -->
    <form action="cgi-bin/get-my-code.py" method="POST">
    <input type="hidden" name="0" value="'.$_POST['0'].'" />
    <input type="hidden" name="1" value="'.$_POST['1'].'" />
    <input type="hidden" name="2" value="'.$_POST['2'].'" />
    <input type="hidden" name="3" value="'.$_POST['3'].'" />
    <input type="hidden" name="4" value="'.$_POST['4'].'" />
    <input type="hidden" name="5" value="'.$_POST['5'].'" />
    <input type="hidden" name="6" value="'.$_POST['6'].'" />
    <input type="hidden" name="7" value="'.$_POST['7'].'" />
    <input type="hidden" name="8" value="'.$_POST['8'].'" />
    <input type="hidden" name="9" value="'.$_POST['9'].'" />
    <input type="hidden" name="10" value="'.$_POST['10'].'" />
    <input type="hidden" name="11" value="'.$_POST['11'].'" />
    <input type="hidden" name="12" value="'.$_POST['12'].'" />
    <input type="hidden" name="13" value="'.$_POST['13'].'" />
    <input type="hidden" name="14" value="'.$_POST['14'].'" />
    <input type="hidden" name="15" value="'.$_POST['15'].'" />
    <input type="hidden" name="16" value="'.$_POST['16'].'" />
    <input type="hidden" name="17" value="'.$_POST['17'].'" />
    <input type="hidden" name="18" value="'.$_POST['18'].'" />
    <input type="hidden" name="19" value="'.$_POST['19'].'" />
    <input type="hidden" name="reload_count" value="'.$reload_count.'" />
      <input type="hidden" name="choice_made" value="';
echo $current_combo;
echo '" />
    <div class="jumbotron">
    <font color="red">Make sure the #s of the clips you chose are displaying. If not, click "Load My New Choice" first!</font><br>
    <input class="btn btn-large btn-success" type="Submit" value="Submit My Decision and Get My Code!" /> 
    </div>
    </form>
        <!-- Javascript that makes the CSS work -->
    <script src="bootstrap/assets/js/jquery.js"></script>
    <script src="bootstrap/assets/js/bootstrap-transition.js"></script>
    <script src="bootstrap/assets/js/bootstrap-alert.js"></script>
    <script src="bootstrap/assets/js/bootstrap-modal.js"></script>
    <script src="bootstrap/assets/js/bootstrap-dropdown.js"></script>
    <script src="bootstrap/assets/js/bootstrap-scrollspy.js"></script>
    <script src="bootstrap/assets/js/bootstrap-tab.js"></script>
    <script src="bootstrap/assets/js/bootstrap-tooltip.js"></script>
    <script src="bootstrap/assets/js/bootstrap-popover.js"></script>
    <script src="bootstrap/assets/js/bootstrap-button.js"></script>
    <script src="bootstrap/assets/js/bootstrap-collapse.js"></script>
    <script src="bootstrap/assets/js/bootstrap-carousel.js"></script>
    <script src="bootstrap/assets/js/bootstrap-typeahead.js"></script>
  </body>
</html>';
?>