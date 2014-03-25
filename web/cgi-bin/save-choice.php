<?php
$filename = $_POST['choice_made'];
copy($filename, '../turk/chunks/'.basename($filename));
echo '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Saving choice...please wait</title>
  </head>
  <body>
    <p>Please wait, you should be redirected in less than 1 second</p>
    <script>
      window.location.replace("http://allekant.com/cgi-bin/get-my-code.py");
    </script>
  </body>
</html>';
?>