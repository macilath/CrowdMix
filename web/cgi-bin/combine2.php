<?php
//Reading relevant POST variables
//$sel1 = $_POST['group1'];
//$sel2 = $_POST['group2'];
//$combo_num = 4 * intval($sel1) + intval($sel2) + 4 //4x4 index calculation, +4 to get past the 4 uncombined pieces
$song1 = $_POST['0'];
$song2 = $_POST['1'];
$song3 = $_POST['2'];
$song4 = $_POST['3'];
//$current_combo = $_POST[strval($combo_num)];
$current_combo = $_POST['4'];
//
echo '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Combine 2 Music Clips and Get Paid!</title>
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
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
    <link href="../bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../bootstrap/assets/js/html5shiv.js"></script>
    <![endif]-->
  </head>
  <body>
    <!-- temp TODO remove -->
    <p>TODO: (optional, recommended) Apply some CSS</p><br>
    <p>TODO: (optional) AJAX it up so that the user doesn\'t have to press the \'Load my new choice\'" button.</p><br>
    <p>TODO: (optional) Autoplay combined clip on page load.</p><br>
    <p>TODO: (optional) Deletion of the generated non-chosen files.</p><br>
    <p>TODO: (optional, not recommended, too unlikely) Regenerate random filename when the name is already taken.</p><br>
    <p>TODO: (important) Save the user\'s choice.</p><br>
    <p>TODO: (important) UI for the \'Get your code\' page.</p><br>
    <p>TODO: (important) Fix the formula for calculating which radio button choices correspond to which piece.</p><br>
    <p>TODO: (important?) Add the functionality that prevents choosing > 5 min. length songs.</p><br>
    
    <!-- instructions -->
    <div align="center">
    <h1>Instructions</h1>
    <p> - Put task instructions here + say which browsers are supported <br>HTML5 is required</p>
    </div>
    
    <!-- Music Clips -->
    <div align="center">
    <h2>Music Clips</h2><br>
    <p>Music Clip A: <br>
    <audio controls>
      <source src="';
echo $song1;
echo '" type="audio/mpeg">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip B: <br>
    <audio controls>
      <source src="';
echo $song2;
echo '" type="audio/mpeg">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip C: <br>
    <audio controls>
      <source src="';
echo $song3;
echo '" type="audio/mpeg">
      Your browser does not support this audio format.
    </audio>
    <br>
    <p>Music Clip D: <br>
    <audio controls>
      <source src="';
echo $song4;
echo '" type="audio/mpeg">
      Your browser does not support this audio format.
    </audio>
    </div>
    
    <div class="row-fluid marketing">
    
    <div class="span6">
    <!-- Music Clip selection boxes -->
    <form action="combine2.php" method="POST" /> 
    <h2>My Selection for the First Music Clip</h2><br>
    <input type="radio" name="group1" value="0" checked> A<br>
    <input type="radio" name="group1" value="1"> B<br>
    <input type="radio" name="group1" value="2"> C<br>
    <input type="radio" name="group1" value="3"> D<br>
    </div>

    <div class="span6">
    <h2>My Selection for the Second Music Clip</h2><br>
    <input type="radio" name="group2" value="0" checked> A<br>
    <input type="radio" name="group2" value="1"> B<br>
    <input type="radio" name="group2" value="2"> C<br>
    <input type="radio" name="group2" value="3"> D<br>
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
    <input type=\"hidden\" name=\"12\" value=\"".$_POST['16']."\" />
    <input type=\"hidden\" name=\"13\" value=\"".$_POST['17']."\" />
    <input type=\"hidden\" name=\"14\" value=\"".$_POST['18']."\" />
    <input type=\"hidden\" name=\"15\" value=\"".$_POST['19']."\" />
    <div class=\"jumbotron\">
    ";
echo '    <input class="btn btn-large btn-success" type="submit" value="Load My New Choice" />
    </div>
    </form>
    
    <!-- combined Music Clip player -->
    <div align="center">
    <h2>Combined Music Clip - Need to debug indexing</h2><br>
    <audio controls>
      <source src="';
echo $current_combo;
echo '" type="audio/mpeg">
      Your browser does not support this audio format.
    </audio>
    </div>
    
    <!-- submit button -->
    <form action="save-choice.php" method="POST">
      <input type="hidden" name="choice_made" value="';
echo $current_combo;
echo '" />
    <div class="jumbotron">
    <input class="btn btn-large btn-success" type="Submit" value="Submit My Decision and Get My Code!" /> 
    </div>
    </form>
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
</html>';
?>