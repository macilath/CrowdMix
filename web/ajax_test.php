<?php
//Reading relevant POST variables
$sel1 = $_POST['group1'];
$sel2 = $_POST['group2'];
$combo_num = 4 * intval($sel1) + intval($sel2) + 4; //4x4 index calculation, +4 to get past the 4 uncombined pieces

echo '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Combine 2 Music Clips and Get Paid!</title>
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script>
    function updateClip(int, groupNum) {
	var xmlhttp;
	if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
 		 xmlhttp=new XMLHttpRequest();
 	 } else {// code for IE6, IE5
 		 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  	}
	xmlhttp.onreadystatechange=function() {
 		if (xmlhttp.readyState==4 && xmlhttp.status==200) { 
 			if(groupNum == 1) {	 
  	  			document.getElementById("val1").innerHTML=xmlhttp.responseText;
  	  		} else {
  	  			document.getElementById("val2").innerHTML=xmlhttp.responseText;
  	  		}
  		}
  	}
	xmlhttp.open("GET","echo.php?val="+int,true);
	xmlhttp.send();
    }
    </script>
  </head>
  <body>
    
    <div class="row-fluid marketing">
    
    <div class="span6">
    <!-- Music Clip selection boxes -->
    <form action="combine2.php" method="POST" /> 
    <h2>My Selection for the First Music Clip</h2><br>
    <input type="radio" name="group1" value="0" onclick="updateClip(this.value, 1)"> 0<br>
    <input type="radio" name="group1" value="1" onclick="updateClip(this.value, 1)"> 1<br>
    <input type="radio" name="group1" value="2" onclick="updateClip(this.value, 1)"> 2<br>
    <input type="radio" name="group1" value="3" onclick="updateClip(this.value, 1)"> 3<br>
    </div>

    <div class="span6">
    <h2>My Selection for the Second Music Clip</h2><br>
    <input type="radio" name="group2" value="0" onclick="updateClip(this.value, 2)"> 0<br>
    <input type="radio" name="group2" value="1" onclick="updateClip(this.value, 2)"> 1<br>
    <input type="radio" name="group2" value="2" onclick="updateClip(this.value, 2)"> 2<br>
    <input type="radio" name="group2" value="3" onclick="updateClip(this.value, 2)"> 3<br>
    </div>
    
    </div>';
echo '   
    </form>
    
    <!-- combined Music Clip player -->
    <div align="center">
    <h2>Combined Music Clip - ';
echo '#<span id="val1" />'.$sel1.'</span> + #<span id="val2">'.$sel2;
echo '</span></h2><br>
    </div>
  </body>
</html>';
?>